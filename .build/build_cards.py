"""Build cards SVG reusing banner visual system.
Cards: pure typographic (no icons, no logos). Clean, consistent with banner.
"""
import pathlib

ROOT = pathlib.Path(r"D:\Dev\github_personal\Raul-Olivares-TD")
JBM_B64 = pathlib.Path(r"C:\Users\Usuario\AppData\Local\Temp\opencode\jetbrains\jbm_b64.txt").read_text().strip()

DARK_BG = "#0D1117"; DARK_CARD = "#161B22"; DARK_TEXT = "#F0F6FC"
DARK_BLUE = "#3776AB"; DARK_ORANGE = "#FF4713"; DARK_MUTE = "#7D8590"
LIGHT_BG = "#F6F8FA"; LIGHT_CARD = "#FFFFFF"; LIGHT_TEXT = "#1F2328"
LIGHT_MUTE = "#656D76"

def style_block():
    return f'''  <style>
    @font-face {{ font-family:"JBM"; src:url(data:font/ttf;base64,{JBM_B64}) format("truetype"); font-weight:400; }}
    .mono {{ font-family:"JBM",ui-monospace,Consolas,Menlo,monospace; }}
    .sans {{ font-family:-apple-system,BlinkMacSystemFont,"Segoe UI",system-ui,sans-serif; }}
    .cardback {{ fill:{DARK_CARD}; stroke:{DARK_BLUE}; }}
    .title {{ fill:{DARK_TEXT}; }}
    .sub {{ fill:{DARK_BLUE}; }}
    .pillbg {{ fill:{DARK_BG}; }}
    .pillborder {{ stroke:{DARK_ORANGE}; }}
    .pilltxt {{ fill:{DARK_ORANGE}; }}
    .accent {{ stroke:{DARK_ORANGE}; }}
    @media (prefers-color-scheme: light) {{
      .cardback {{ fill:{LIGHT_CARD}; stroke:{LIGHT_TEXT}; }}
      .title {{ fill:{LIGHT_TEXT}; }}
      .sub {{ fill:{DARK_BLUE}; }}
      .pillbg {{ fill:{LIGHT_BG}; }}
    }}
  </style>'''

def tech_card(label, subtitle):
    """Pure typographic tech card (240x120). Centered stacked text, no top gap."""
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 240 120" width="100%" height="auto" role="img" aria-label="{label}">
  <title>{label}</title>
{style_block()}
  <rect class="cardback" x="2" y="2" width="236" height="116" rx="8" ry="8" stroke-width="0.9"/>
  <line class="accent" x1="105" y1="42" x2="135" y2="42" stroke-width="1.2"/>
  <text class="sans title" x="120" y="64" text-anchor="middle" font-size="17" font-weight="600" letter-spacing="1">{label}</text>
  <text class="mono sub" x="120" y="88" text-anchor="middle" font-size="9" letter-spacing="1.5">{subtitle}</text>
</svg>'''

def case_card(num, title, stack_lines, oneliner):
    """Case study card (280x160). CASE pill, title, multi-line tech stack, oneliner."""
    if isinstance(stack_lines, str):
        stack_lines = [stack_lines]
    n = len(stack_lines)
    title_y = 62
    base = 82
    step = 16
    stack_svg = ""
    for i, ln in enumerate(stack_lines):
        stack_svg += f'<text class="mono sub" x="140" y="{base + i*step}" text-anchor="middle" font-size="9" letter-spacing="1.2">{ln}</text>\n  '
    oneliner_y = base + n*step + 6
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 280 160" width="100%" height="auto" role="img" aria-label="Case {num}">
  <title>Case {num} &#8212; {title}</title>
{style_block()}
  <rect class="cardback" x="2" y="2" width="276" height="156" rx="8" ry="8" stroke-width="0.9"/>
  <rect class="pillbg pillborder" x="110" y="14" width="60" height="18" rx="9" ry="9" stroke-width="0.9"/>
  <text class="mono pilltxt" x="140" y="26" text-anchor="middle" font-size="9" letter-spacing="1.5">CASE {num}</text>
  <circle cx="140" cy="42" r="1.5" fill="{DARK_ORANGE}"/>
  <text class="sans title" x="140" y="{title_y}" text-anchor="middle" font-size="15" font-weight="600" letter-spacing="0.8">{title}</text>
  {stack_svg}<text class="sans" x="140" y="{oneliner_y}" text-anchor="middle" font-size="10" fill="{DARK_MUTE}">{oneliner}</text>
</svg>'''

def snippet_card(num, title, oneliner):
    """Public snippet card (280x110)."""
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 280 110" width="100%" height="auto" role="img" aria-label="Snippet {num}">
  <title>Snippet {num} &#8212; {title}</title>
{style_block()}
  <rect class="cardback" x="2" y="2" width="276" height="106" rx="8" ry="8" stroke-width="0.9"/>
  <text class="mono pilltxt" x="20" y="28" font-size="9" letter-spacing="1.5">SNIPPET {num}</text>
  <line class="accent" x1="20" y1="36" x2="64" y2="36" stroke-width="1.2"/>
  <text class="sans title" x="140" y="62" text-anchor="middle" font-size="15" font-weight="600" letter-spacing="0.5">{title}</text>
  <text class="sans" x="140" y="86" text-anchor="middle" font-size="10" fill="{DARK_MUTE}">{oneliner}</text>
</svg>'''

def divider():
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 600 20" width="100%" height="auto" role="img" aria-label="divider">
  <style>
    @media (prefers-color-scheme: light) {{ .line {{ stroke:{LIGHT_TEXT}; }} .n {{ fill:{DARK_BLUE}; }} }}
  </style>
  <path id="dpath" d="M 60 10 H 540" fill="none"/>
  <line class="line" x1="60" y1="10" x2="285" y2="10" stroke="{DARK_BLUE}" stroke-width="0.6" opacity="0.5"/>
  <circle class="n" cx="280" cy="10" r="2.4" fill="{DARK_BLUE}">
    <animate attributeName="r" values="2.4;3.6;2.4" dur="3.4s" repeatCount="indefinite"/>
  </circle>
  <circle cx="300" cy="10" r="2.4" fill="{DARK_ORANGE}">
    <animate attributeName="opacity" values="0.5;1;0.5" dur="3.4s" begin="0.4s" repeatCount="indefinite"/>
  </circle>
  <circle cx="320" cy="10" r="2.4" fill="{DARK_BLUE}">
    <animate attributeName="r" values="2.4;3.6;2.4" dur="3.4s" begin="0.8s" repeatCount="indefinite"/>
  </circle>
  <line class="line" x1="315" y1="10" x2="540" y2="10" stroke="{DARK_BLUE}" stroke-width="0.6" opacity="0.5"/>
  <circle r="1.6" fill="{DARK_ORANGE}">
    <animateMotion dur="5s" begin="1.2s" repeatCount="indefinite">
      <mpath href="#dpath"/>
    </animateMotion>
  </circle>
</svg>'''

cards = {
    "cards/python.svg":         tech_card("Python",     "CORE LANGUAGE"),
    "cards/houdini.svg":        tech_card("Houdini",     "DCC · TOOL DEV"),
    "cards/usd.svg":            tech_card("USD",         "HYDRA · LAYERS"),
    "cards/qt.svg":             tech_card("Qt / PySide", "PYSIDE6 · UI"),
    "cards/usd-tech.svg":       tech_card("USD",         "HYDRA · LAYERS"),
    "cards/git.svg":            tech_card("Git",         "VERSION CONTROL"),
    "cards/automation.svg":     tech_card("Automation",  "WORKFLOWS · CI"),
    "cards/tool-dev.svg":       tech_card("Tool Development", "DCC · SCRIPTING"),
    "cards/pipeline-arch.svg":  tech_card("Pipeline Architecture", "DESIGN · SCALING"),
    "cards/case-01.svg":        case_card("01", "Showreel",  ["Python · Houdini · Flow · Qt · PDG", "Google Drive · Discord"], "Personal pipeline &amp; tooling showcase."),
    "cards/case-02.svg":        case_card("02", "FXDailies", ["Python · Houdini · Kitsu", "Clean Architecture · MVC", "Factory Patterns"], "Real project used by 20+ artists."),
    "divider.svg":              divider(),
}

errors = 0
for path, content in cards.items():
    out = ROOT / path
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(content, encoding="utf-8")
    try:
        import xml.dom.minidom as m
        m.parseString(content)
        status = "OK"
    except Exception as e:
        status = f"ERR: {e}"
        errors += 1
    print(f"{path:38s} {len(content):7d}B  {status}")
print(f"--- {len(cards)} cards  | {errors} errors")