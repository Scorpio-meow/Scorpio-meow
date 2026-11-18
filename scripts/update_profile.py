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
PALETTE = ["#ff4d5e", "#ffb86b", "#b57bff", "#5ad1c1", "#6aa5ff"]
RECENT_COUNT = 5
LANGUAGE_COUNT = 5
CARD_WIDTH = 800
BAR_X = 40
BAR_WIDTH = 720
STATS_THEMES = {
    "stats.svg": {"card": "#fff6ef", "stroke": "#ecd6d0", "text": "#2a1530", "cap": "#c2410c"},
    "stats-dark.svg": {"card": "#1b1428", "stroke": "#3a2848", "text": "#fff4ec", "cap": "#ffb86b"},
}


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


def stats_svg(repo_total, languages, theme):
    total = sum(count for _, count in languages)
    column = BAR_WIDTH / LANGUAGE_COUNT
    cursor = BAR_X
    segments = []
    legend = []
    for index, (name, count) in enumerate(languages):
        width = BAR_WIDTH * count / total
        color = PALETTE[index]
        segments.append(f'<rect x="{cursor:.1f}" y="54" width="{width:.1f}" height="14" fill="{color}"/>')
        cursor += width
        x = BAR_X + index * column
        legend.append(
            f'<circle cx="{x + 6:.0f}" cy="95" r="6" fill="{color}"/>'
            f'<text x="{x + 20:.0f}" y="100" font-family="{FONT}" font-size="14" fill="{theme["text"]}">'
            f"{name} {100 * count / total:.0f}%</text>"
        )
    return f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {CARD_WIDTH} 124" width="{CARD_WIDTH}" height="124" role="img" aria-label="公開儲存庫的語言分布">
  <title>公開儲存庫的語言分布</title>
  <defs>
    <clipPath id="round"><rect x="{BAR_X}" y="54" width="{BAR_WIDTH}" height="14" rx="7"/></clipPath>
  </defs>
  <rect x="1" y="1" width="{CARD_WIDTH - 2}" height="122" rx="16" fill="{theme['card']}" stroke="{theme['stroke']}" stroke-width="1"/>
  <text x="{BAR_X}" y="38" font-family="{FONT}" font-size="14" font-weight="600" letter-spacing="1" fill="{theme['cap']}">{repo_total} 個公開儲存庫 · 依主要語言</text>
  <g clip-path="url(#round)">{''.join(segments)}</g>
  {''.join(legend)}
</svg>
"""


def recent_line(repos, owner):
    candidates = [
        repo
        for repo in repos
        if not repo["private"] and not repo["fork"] and repo["name"] != owner
    ]
    candidates.sort(key=lambda repo: repo["pushed_at"], reverse=True)
    items = [
        f"[{repo['name']}]({repo['html_url']})（{repo['pushed_at'][5:10]}）"
        for repo in candidates[:RECENT_COUNT]
    ]
    return "近期更新：" + " · ".join(items)


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
    for name, theme in STATS_THEMES.items():
        ASSETS.joinpath(name).write_text(stats_svg(len(public), top_languages, theme), encoding="utf-8")
    text = README.read_text(encoding="utf-8")
    text = replace_block(text, "RECENT", recent_line(repos, owner))
    README.write_text(text, encoding="utf-8")


if __name__ == "__main__":
    main()
