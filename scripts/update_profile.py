import json
import os
import re
import sys
import urllib.request
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
ASSETS = ROOT / "assets"
README = ROOT / "README.md"
FONT = "'Segoe UI', 'Noto Sans TC', sans-serif"
PALETTE = ["#ff4d5e", "#ffb86b", "#b57bff", "#5ad1c1", "#6aa5ff", "#a3a3b8"]
RECENT_COUNT = 5
LANGUAGE_COUNT = 5
DESCRIPTION_LIMIT = 90
EMOJI = re.compile("[\U0001F000-\U0001FAFF☀-➿️‍]")


def require_env(name):
    value = os.environ.get(name)
    if not value:
        sys.exit(f"missing environment variable: {name}")
    return value


def api(path, token):
    request = urllib.request.Request(
        f"https://api.github.com{path}",
        headers={
            "Authorization": f"Bearer {token}",
            "Accept": "application/vnd.github+json",
            "X-GitHub-Api-Version": "2022-11-28",
        },
    )
    with urllib.request.urlopen(request) as response:
        return json.load(response)


def fetch_repos(owner, token):
    repos = []
    page = 1
    while True:
        batch = api(f"/users/{owner}/repos?type=owner&per_page=100&page={page}", token)
        repos.extend(batch)
        if len(batch) < 100:
            return repos
        page += 1


def stats_svg(repo_total, star_total, followers, languages):
    total = sum(count for _, count in languages)
    bar_x = 40
    bar_width = 720
    cursor = bar_x
    segments = []
    legend = []
    for index, (name, count) in enumerate(languages):
        width = bar_width * count / total
        color = PALETTE[index % len(PALETTE)]
        segments.append(f'<rect x="{cursor:.1f}" y="144" width="{width:.1f}" height="14" fill="{color}"/>')
        cursor += width
        column = index % 3
        row = index // 3
        x = bar_x + column * 240
        y = 198 + row * 26
        percent = 100 * count / total
        legend.append(
            f'<circle cx="{x + 6}" cy="{y - 5}" r="6" fill="{color}"/>'
            f'<text x="{x + 20}" y="{y}" class="legend">{name} {percent:.0f}%</text>'
        )
    metrics = [(repo_total, "公開儲存庫"), (star_total, "Stars"), (followers, "Followers")]
    metric_nodes = []
    for index, (value, label) in enumerate(metrics):
        x = bar_x + index * 240
        metric_nodes.append(
            f'<text x="{x}" y="64" class="num">{value}</text>'
            f'<text x="{x}" y="90" class="label">{label}</text>'
        )
    height = 198 + ((len(languages) - 1) // 3) * 26 + 28
    return f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 {height}" width="800" height="{height}" role="img" aria-label="GitHub 活動統計">
  <title>GitHub 活動統計</title>
  <defs>
    <style>
      .card {{ fill: #fff6ef; stroke: #ecd6d0; }}
      .num {{ font: 700 36px {FONT}; fill: #2a1530; }}
      .label {{ font: 400 15px {FONT}; fill: #5a4660; }}
      .legend {{ font: 400 14px {FONT}; fill: #2a1530; }}
      .cap {{ font: 600 13px {FONT}; fill: #c2410c; letter-spacing: 2px; }}
      @media (prefers-color-scheme: dark) {{
        .card {{ fill: #1b1428; stroke: #3a2848; }}
        .num {{ fill: #fff4ec; }}
        .label {{ fill: #d9c9d8; }}
        .legend {{ fill: #fff4ec; }}
        .cap {{ fill: #ffb86b; }}
      }}
    </style>
    <clipPath id="round"><rect x="{bar_x}" y="144" width="{bar_width}" height="14" rx="7"/></clipPath>
  </defs>
  <rect x="1" y="1" width="798" height="{height - 2}" rx="16" class="card" stroke-width="1"/>
  {''.join(metric_nodes)}
  <text x="{bar_x}" y="134" class="cap">LANGUAGES BY REPOSITORY</text>
  <g clip-path="url(#round)">{''.join(segments)}</g>
  {''.join(legend)}
</svg>
"""


def recent_block(repos, owner):
    candidates = [
        repo
        for repo in repos
        if not repo["private"]
        and not repo["fork"]
        and repo["name"] != owner
        and (repo["description"] or "").strip()
    ]
    candidates.sort(key=lambda repo: repo["pushed_at"], reverse=True)
    lines = ["| 更新日 | 專案 | 說明 |", "| --- | --- | --- |"]
    for repo in candidates[:RECENT_COUNT]:
        description = EMOJI.sub("", repo["description"]).strip()
        if len(description) > DESCRIPTION_LIMIT:
            description = description[:DESCRIPTION_LIMIT].rsplit(" ", 1)[0].rstrip(",;:") + "..."
        description = description.replace("|", "/")
        lines.append(f"| {repo['pushed_at'][:10]} | [{repo['name']}]({repo['html_url']}) | {description} |")
    return "\n".join(lines)


def replace_block(text, marker, content):
    pattern = re.compile(rf"(<!--{marker}:START-->)(.*?)(<!--{marker}:END-->)", re.DOTALL)
    if not pattern.search(text):
        sys.exit(f"marker not found: {marker}")
    return pattern.sub(lambda match: f"{match.group(1)}\n{content}\n{match.group(3)}", text)


def main():
    owner = require_env("OWNER")
    token = require_env("GITHUB_TOKEN")
    repos = fetch_repos(owner, token)
    public = [repo for repo in repos if not repo["private"] and not repo["fork"]]
    languages = Counter(repo["language"] for repo in public if repo["language"])
    top_languages = languages.most_common(LANGUAGE_COUNT)
    stars = sum(repo["stargazers_count"] for repo in public)
    followers = api(f"/users/{owner}", token)["followers"]
    ASSETS.joinpath("stats.svg").write_text(
        stats_svg(len(public), stars, followers, top_languages), encoding="utf-8"
    )
    text = README.read_text(encoding="utf-8")
    text = replace_block(text, "RECENT", recent_block(repos, owner))
    README.write_text(text, encoding="utf-8")


if __name__ == "__main__":
    main()
