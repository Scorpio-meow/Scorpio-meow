import base64
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
ASSETS = ROOT / "assets"
FONT = "'Segoe UI', 'Noto Sans TC', sans-serif"

HERO_THEMES = {
    "hero.svg": {
        "bg_from": "#14101f",
        "bg_to": "#2a1530",
        "star": "#ffffff",
        "disc": "#fff4ec",
        "title": "#fff4ec",
        "sub": "#d9c9d8",
        "tag": "#ffb86b",
    },
    "hero-light.svg": {
        "bg_from": "#fff6ef",
        "bg_to": "#f8dfe6",
        "star": "#c98aa0",
        "disc": "#ffffff",
        "title": "#2a1530",
        "sub": "#5a4660",
        "tag": "#c2410c",
    },
}

TEXT_THEMES = {
    "": {"heading": "#2a1530", "footer": "#5a4660"},
    "-dark": {"heading": "#fff4ec", "footer": "#d9c9d8"},
}

HEADINGS = {
    "h-featured": "精選作品",
    "h-how": "我怎麼做",
    "h-skills": "Agent Skills",
    "h-stats": "GitHub 活動",
    "h-tech": "常用技術",
    "h-lab": "Miao Lab",
    "h-contact": "聯絡與回饋",
}

ACCENT = (
    '<linearGradient id="accent" x1="0" y1="0" x2="1" y2="0">'
    '<stop offset="0" stop-color="#ff4d5e"/><stop offset="1" stop-color="#ffb86b"/>'
    "</linearGradient>"
)


def hero(theme, logo_b64):
    return f"""<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" viewBox="0 0 1200 320" width="1200" height="320" role="img" aria-labelledby="t d">
  <title id="t">Scorpio-meow</title>
  <desc id="d">天蠍喵喵：黑貓與蠍尾吉祥物的個人橫幅</desc>
  <defs>
    <linearGradient id="bg" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0" stop-color="{theme['bg_from']}"/>
      <stop offset="1" stop-color="{theme['bg_to']}"/>
    </linearGradient>
    {ACCENT}
    <style>
      .title {{ font: 700 64px {FONT}; fill: {theme['title']}; }}
      .sub {{ font: 400 24px {FONT}; fill: {theme['sub']}; }}
      .tag {{ font: 600 16px {FONT}; fill: {theme['tag']}; letter-spacing: 3px; }}
      .mascot {{ animation: bob 4s ease-in-out infinite; }}
      @keyframes bob {{ 0%, 100% {{ transform: translateY(0); }} 50% {{ transform: translateY(-6px); }} }}
      @media (prefers-reduced-motion: reduce) {{ .mascot {{ animation: none; }} }}
    </style>
  </defs>
  <rect width="1200" height="320" rx="20" fill="url(#bg)"/>
  <g fill="{theme['star']}" opacity="0.5">
    <circle cx="90" cy="60" r="2"/><circle cx="450" cy="40" r="1.5"/><circle cx="560" cy="70" r="1.5"/>
    <circle cx="700" cy="30" r="2"/><circle cx="820" cy="110" r="1.5"/><circle cx="960" cy="50" r="2"/>
    <circle cx="1120" cy="90" r="1.5"/><circle cx="1060" cy="260" r="2"/>
  </g>
  <circle cx="270" cy="160" r="122" fill="{theme['disc']}"/>
  <circle cx="270" cy="160" r="122" fill="none" stroke="url(#accent)" stroke-width="5"/>
  <image class="mascot" x="160" y="50" width="220" height="220" href="data:image/png;base64,{logo_b64}" xlink:href="data:image/png;base64,{logo_b64}"/>
  <text x="560" y="130" class="tag">AI ENGINEER PORTFOLIO</text>
  <text x="560" y="205" class="title">Scorpio-meow</text>
  <text x="560" y="250" class="sub">天蠍喵喵 · 把 AI 接進真實工作流程</text>
  <rect x="560" y="268" width="180" height="4" rx="2" fill="url(#accent)"/>
</svg>
"""


def heading(text, color):
    return f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 720 48" width="720" height="48" role="img" aria-label="{text}">
  <title>{text}</title>
  <defs>
    <linearGradient id="bar" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0" stop-color="#ff4d5e"/><stop offset="1" stop-color="#ffb86b"/>
    </linearGradient>
  </defs>
  <rect x="0" y="5" width="8" height="38" rx="4" fill="url(#bar)"/>
  <text x="24" y="35" font-family="{FONT}" font-size="30" font-weight="700" fill="{color}">{text}</text>
</svg>
"""


def footer(color):
    return f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 110" width="1200" height="110" role="img" aria-label="Scorpio-meow 頁尾">
  <title>Scorpio-meow</title>
  <defs>
    {ACCENT}
  </defs>
  <path d="M 0 70 C 200 70 260 30 420 30 S 560 76 600 76" fill="none" stroke="url(#accent)" stroke-width="6" stroke-linecap="round" opacity="0.9"/>
  <path d="M 1200 70 C 1000 70 940 30 780 30 S 640 76 600 76" fill="none" stroke="url(#accent)" stroke-width="6" stroke-linecap="round" opacity="0.9"/>
  <path d="M 600 76 L 592 60 L 608 60 Z" fill="#ff4d5e"/>
  <text x="600" y="102" text-anchor="middle" font-family="{FONT}" font-size="18" font-weight="600" letter-spacing="2" fill="{color}">SCORPIO-MEOW · 天蠍喵喵</text>
</svg>
"""


def main():
    logo_b64 = base64.b64encode((ASSETS / "logo-256.png").read_bytes()).decode()
    for name, theme in HERO_THEMES.items():
        (ASSETS / name).write_text(hero(theme, logo_b64), encoding="utf-8")
    for suffix, colors in TEXT_THEMES.items():
        for name, text in HEADINGS.items():
            (ASSETS / f"{name}{suffix}.svg").write_text(heading(text, colors["heading"]), encoding="utf-8")
        (ASSETS / f"footer{suffix}.svg").write_text(footer(colors["footer"]), encoding="utf-8")


if __name__ == "__main__":
    main()
