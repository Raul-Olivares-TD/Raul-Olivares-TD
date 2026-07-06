import base64, pathlib

ROOT = pathlib.Path(r"D:\Dev\github_personal\Raul-Olivares-TD")
b64 = pathlib.Path(r"C:\Users\Usuario\AppData\Local\Temp\opencode\jetbrains\jbm_b64.txt").read_text().strip()

SVG = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 320" width="100%" height="auto" role="img" aria-label="Raul Olivares - Pipeline Technical Director">
  <title>Raul Olivares - Pipeline Technical Director</title>
  <desc>Personal banner: Pipeline Technical Director specialising in production software for VFX, animation and games.</desc>

  <style>
    @font-face {{
      font-family: "JBM";
      src: url(data:font/ttf;base64,{b64}) format("truetype");
      font-weight: 400;
      font-style: normal;
    }}
    .mono {{ font-family: "JBM", ui-monospace, "Cascadia Code", "Source Code Pro", Menlo, Consolas, monospace; }}
    .sans {{ font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", system-ui, "Helvetica Neue", Arial, sans-serif; }}
    @media (prefers-color-scheme: light) {{
      .bg {{ fill: #F6F8FA; }}
      .grid {{ stroke: #1F2328; }}
      .node {{ fill: #3776AB; }}
      .title {{ fill: #1F2328; }}
      .sub {{ fill: #3776AB; }}
      .tag {{ fill: #424A53; }}
      .foot {{ fill: #656D76; }}
      .rule {{ stroke: #1F2328; }}
    }}
  </style>

  <!-- Background -->
  <rect class="bg" x="0" y="0" width="1200" height="320" fill="#0D1117"/>

  <!-- Blueprint grid pattern -->
  <defs>
    <pattern id="grid" width="80" height="80" patternUnits="userSpaceOnUse">
      <path class="grid" d="M 80 0 L 0 0 0 80" fill="none" stroke="#F0F6FC" stroke-width="0.5" opacity="0.06"/>
      <circle cx="0" cy="0" r="1.6" fill="#3776AB" opacity="0.18"/>
    </pattern>
    <!-- travelling data packet path -->
    <path id="pipe" d="M 120 270 H 1080"/>
  </defs>

  <rect x="0" y="0" width="1200" height="320" fill="url(#grid)"/>

  <!-- Corner blueprint ticks -->
  <g stroke="#3776AB" stroke-width="1" opacity="0.45" fill="none">
    <path d="M 40 40 H 72 M 40 40 V 72"/>
    <path d="M 1160 40 H 1128 M 1160 40 V 72"/>
    <path d="M 40 280 H 72 M 40 280 V 248"/>
    <path d="M 1160 280 H 1128 M 1160 280 V 248"/>
  </g>

  <!-- Top technical label -->
  <text class="mono" x="600" y="58" text-anchor="middle" font-size="11" letter-spacing="6" fill="#3776AB" opacity="0.0">
    PIPELINE  ·  VFX  ·  ANIMATION  ·  GAMES
    <animate attributeName="opacity" from="0" to="0.8" dur="0.6s" begin="0s" fill="freeze"/>
  </text>

  <!-- Name -->
  <text class="sans title" x="600" y="128" text-anchor="middle" font-size="58" font-weight="600" letter-spacing="10" fill="#F0F6FC" opacity="0">
    RAUL OLIVARES
    <animate attributeName="opacity" from="0" to="1" dur="0.7s" begin="0.15s" fill="freeze"/>
  </text>

  <!-- Role -->
  <text class="mono sub" x="600" y="166" text-anchor="middle" font-size="16" letter-spacing="8" fill="#3776AB" opacity="0">
    PIPELINE  TECHNICAL  DIRECTOR
    <animate attributeName="opacity" from="0" to="1" dur="0.6s" begin="0.55s" fill="freeze"/>
  </text>

  <!-- Short rule -->
  <line class="rule" x1="555" y1="184" x2="645" y2="184" stroke="#FF4713" stroke-width="1.5" opacity="0">
    <animate attributeName="opacity" from="0" to="0.9" dur="0.4s" begin="0.85s" fill="freeze"/>
  </line>

  <!-- Tagline -->
  <text class="sans tag" x="600" y="210" text-anchor="middle" font-size="15" letter-spacing="0.5" fill="#9DA7B3" opacity="0">
    Building production software for artists and studios.
    <animate attributeName="opacity" from="0" to="1" dur="0.6s" begin="1s" fill="freeze"/>
  </text>

  <!-- Tech footer -->
  <text class="mono foot" x="600" y="238" text-anchor="middle" font-size="12" letter-spacing="4" fill="#7D8590" opacity="0">
    PYTHON&#160;&#160;·&#160;&#160;USD&#160;&#160;·&#160;&#160;QT&#160;&#160;·&#160;&#160;GIT
    <animate attributeName="opacity" from="0" to="0.85" dur="0.5s" begin="1.25s" fill="freeze"/>
  </text>

  <!-- Pipeline ribbon -->
  <g opacity="0">
    <animate attributeName="opacity" from="0" to="1" dur="0.5s" begin="1.4s" fill="freeze"/>
    <use href="#pipe" stroke="#3776AB" stroke-width="1" opacity="0.35" fill="none"/>
    <!-- nodes along the pipe -->
    <circle cx="120"  cy="270" r="3" fill="#3776AB">
      <animate attributeName="r" values="3;5;3" dur="3.0s" begin="1.5s" repeatCount="indefinite"/>
      <animate attributeName="opacity" values="0.6;1;0.6" dur="3.0s" begin="1.5s" repeatCount="indefinite"/>
    </circle>
    <circle cx="440"  cy="270" r="3" fill="#3776AB">
      <animate attributeName="r" values="3;5;3" dur="3.0s" begin="2.1s" repeatCount="indefinite"/>
      <animate attributeName="opacity" values="0.6;1;0.6" dur="3.0s" begin="2.1s" repeatCount="indefinite"/>
    </circle>
    <circle cx="760"  cy="270" r="3" fill="#FF4713">
      <animate attributeName="r" values="3;5;3" dur="3.0s" begin="2.7s" repeatCount="indefinite"/>
      <animate attributeName="opacity" values="0.6;1;0.6" dur="3.0s" begin="2.7s" repeatCount="indefinite"/>
    </circle>
    <circle cx="1080" cy="270" r="3" fill="#3776AB">
      <animate attributeName="r" values="3;5;3" dur="3.0s" begin="3.3s" repeatCount="indefinite"/>
      <animate attributeName="opacity" values="0.6;1;0.6" dur="3.0s" begin="3.3s" repeatCount="indefinite"/>
    </circle>
    <!-- travelling data packet -->
    <circle r="2.6" fill="#FF4713">
      <animateMotion dur="4.2s" begin="1.6s" repeatCount="indefinite" rotate="auto">
        <mpath href="#pipe"/>
      </animateMotion>
    </circle>
  </g>
</svg>
'''

out = ROOT / "banner.svg"
out.write_text(SVG, encoding="utf-8")
print(f"written {out}  ({len(SVG)} bytes)")