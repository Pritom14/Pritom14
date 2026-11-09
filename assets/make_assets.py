"""Generates the profile's SVG assets (hero, terminal, project cards, footer)."""
import sys
from pathlib import Path
from xml.sax.saxutils import escape as x

OUT = Path(sys.argv[1])
BG, PANEL, BAR, LINE = "#0B0F17", "#111827", "#0D1117", "#243042"
TEXT, SOFT, MUTED = "#E6EDF3", "#C9D1D9", "#8B949E"
ORANGE, TEAL, VIOLET, AMBER = "#FF6B35", "#2DD4BF", "#A78BFA", "#FBBF24"
SANS = "-apple-system,BlinkMacSystemFont,'Segoe UI','Helvetica Neue',Helvetica,Arial,sans-serif"
MONO = "ui-monospace,SFMono-Regular,Menlo,Consolas,'Liberation Mono',monospace"


def svg(w, h, body, style="", label=""):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" '
            f'role="img" aria-label="{x(label)}" xml:space="preserve"><style>text{{font-family:{SANS}}} .m{{font-family:{MONO}}} {style}</style>{body}</svg>')


def hero():
    tag = ["› I keep 4.3M+ provider records flowing at HiLabs",
           "› I ship PRs to a fleet of coding agents",
           "› I make vision LLMs cheaper",
           "› I break payment webhooks before prod does"]
    rot = "".join(f'<text class="m t t{i}" x="48" y="216" font-size="18" fill="{ORANGE}">{x(t)}</text>' for i, t in enumerate(tag))
    pills, px = "", 48
    for p in ["Python", "Go", "Java", "data pipelines", "AI agents", "LLM infra"]:
        w = int(len(p) * 7.4 + 26)
        pills += (f'<rect x="{px}" y="246" width="{w}" height="28" rx="14" fill="none" stroke="{LINE}"/>'
                  f'<text x="{px + w / 2}" y="265" font-size="13" fill="{MUTED}" text-anchor="middle">{x(p)}</text>')
        px += w + 8
    nodes = [(660, 92, TEAL), (742, 60, ORANGE), (822, 104, TEAL), (690, 196, ORANGE), (800, 214, TEAL)]
    hub = (748, 140)
    edges = "".join(f'<line class="e" x1="{a}" y1="{b}" x2="{hub[0]}" y2="{hub[1]}" stroke="{c}" style="animation-delay:{i * .3}s"/>'
                    for i, (a, b, c) in enumerate(nodes))
    dots = "".join(f'<circle class="n" cx="{a}" cy="{b}" r="9" fill="{BG}" stroke="{c}" stroke-width="2.5" style="animation-delay:{i * .45}s"/>'
                   for i, (a, b, c) in enumerate(nodes))
    merge = (f'<circle cx="{hub[0]}" cy="{hub[1]}" r="22" fill="{PANEL}" stroke="{ORANGE}" stroke-width="2.5"/>'
             f'<g transform="translate({hub[0] - 9},{hub[1] - 11})" fill="none" stroke="{TEXT}" stroke-width="2.2" stroke-linecap="round">'
             f'<circle cx="3" cy="3" r="2.6"/><circle cx="3" cy="19" r="2.6"/><circle cx="15" cy="11" r="2.6"/>'
             f'<path d="M3 5.6v10.8M3 7c0 4 4 4 9.4 4"/></g>')
    style = (".t{opacity:0;animation:rot 12s infinite} .t0{animation-delay:0s} .t1{animation-delay:3s} .t2{animation-delay:6s} .t3{animation-delay:9s}"
             "@keyframes rot{0%{opacity:0;transform:translateY(6px)}4%,22%{opacity:1;transform:none}26%,100%{opacity:0}}"
             ".e{stroke-width:2;stroke-dasharray:6 7;animation:flow 1.6s linear infinite}@keyframes flow{to{stroke-dashoffset:-26}}"
             ".n{animation:pulse 2.4s ease-in-out infinite}@keyframes pulse{50%{stroke-width:5}}"
             ".g{animation:glow 6s ease-in-out infinite}@keyframes glow{50%{opacity:.55}}"
             ".c{animation:blink 1.1s steps(1) infinite}@keyframes blink{50%{opacity:0}}")
    body = (f'<defs><pattern id="grid" width="24" height="24" patternUnits="userSpaceOnUse"><path d="M24 0H0V24" fill="none" stroke="#ffffff" stroke-opacity=".045"/></pattern>'
            f'<radialGradient id="g1"><stop offset="0" stop-color="{ORANGE}" stop-opacity=".32"/><stop offset="1" stop-color="{ORANGE}" stop-opacity="0"/></radialGradient>'
            f'<radialGradient id="g2"><stop offset="0" stop-color="{TEAL}" stop-opacity=".22"/><stop offset="1" stop-color="{TEAL}" stop-opacity="0"/></radialGradient>'
            f'<clipPath id="r"><rect width="900" height="300" rx="18"/></clipPath></defs>'
            f'<g clip-path="url(#r)"><rect width="900" height="300" fill="{BG}"/><rect width="900" height="300" fill="url(#grid)"/>'
            f'<circle class="g" cx="760" cy="40" r="260" fill="url(#g1)"/><circle class="g" cx="80" cy="320" r="240" fill="url(#g2)" style="animation-delay:3s"/></g>'
            f'<text class="m" x="48" y="70" font-size="14" fill="{ORANGE}">~/pritom<tspan class="c" fill="{TEXT}"> ▍</tspan></text>'
            f'<text x="46" y="126" font-size="52" font-weight="800" fill="{TEXT}" letter-spacing="-1">Pritom Mazumdar</text>'
            f'<text x="48" y="162" font-size="17" fill="{MUTED}">Technical Lead @ HiLabs  ·  open-source builder  ·  Bengaluru</text>'
            f'{rot}{pills}{edges}{dots}{merge}')
    return svg(900, 300, body, style, "Pritom Mazumdar, Technical Lead at HiLabs, open-source builder, Bengaluru")


def terminal():
    O, T, M, C = ORANGE, TEXT, MUTED, TEAL
    lines = [
        [("$ ", O), ("whoami", T)],
        [("Pritom Mazumdar · Technical Lead @ HiLabs", T)],
        [("  ↳ ", C), ("I own the pipeline platform that feeds healthcare provider data", M)],
        [("    ", M), ("(4.3M+ records) into credentialing: self-healing runs, ~99% complete", M)],
        [("  ↳ ", C), ("before: Microsoft · Zomato · Oolka (founding eng) · ConverzAI · Apptio", M)],
        [],
        [("$ ", O), ("cat now.txt", T)],
        [("  → ", C), ("Agent Orchestrator: fleets of coding agents, task → merged PR", T)],
        [("  → ", C), ("token0 · carbon-layer · aside: open source, built in public", T)],
        [("$ ", O), ("▍", T)],
    ]
    rows = ""
    for i, segs in enumerate(lines):
        y = 78 + i * 25
        cls = "l c" if i == len(lines) - 1 else "l"
        # SVG collapses leading spaces, so indentation is an x offset (one monospace cell is 0.6em = 9px)
        indent = len(segs[0][0]) - len(segs[0][0].lstrip(" ")) if segs else 0
        segs = [(segs[0][0].lstrip(" "), segs[0][1])] + segs[1:] if segs else segs
        spans = "".join(f'<tspan fill="{c}">{x(s)}</tspan>' for s, c in segs if s)
        rows += f'<text class="m {cls}" x="{28 + indent * 9}" y="{y}" font-size="15" style="animation-delay:{i * .28:.2f}s">{spans}</text>'
    h = 78 + len(lines) * 25 + 8
    body = (f'<rect width="900" height="{h}" rx="14" fill="{PANEL}" stroke="{LINE}"/>'
            f'<path d="M0 14a14 14 0 0 1 14-14h872a14 14 0 0 1 14 14v22H0z" fill="{BAR}"/>'
            f'<circle cx="24" cy="18" r="6" fill="#FF5F57"/><circle cx="44" cy="18" r="6" fill="#FEBC2E"/><circle cx="64" cy="18" r="6" fill="#28C840"/>'
            f'<text class="m" x="450" y="23" font-size="13" fill="{MUTED}" text-anchor="middle">pritom@bengaluru: ~</text>{rows}')
    style = (".l{animation:in .45s ease-out both}@keyframes in{from{opacity:0;transform:translateX(-8px)}}"
             ".c{animation:in .45s ease-out both,blink 1.1s steps(1) 3.2s infinite}@keyframes blink{50%{opacity:0}}")
    return svg(900, h, body, style, "whoami: Pritom Mazumdar, Technical Lead at HiLabs")


ICONS = {  # 44x44 line icons, drawn here so the cards don't rely on emoji
    "fleet": lambda c: (f'<g fill="none" stroke="{c}" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round">'
                        f'<rect x="3" y="5" width="12" height="10" rx="3"/><rect x="29" y="5" width="12" height="10" rx="3"/><rect x="3" y="29" width="12" height="10" rx="3"/>'
                        f'<path d="M15 10h6a3 3 0 0 1 3 3v6M29 10h-2M15 34h6a3 3 0 0 0 3-3v-6"/><circle cx="33" cy="33" r="6"/><path d="M30.5 33l2 2 3.5-4"/></g>'),
    "chaos": lambda c: (f'<g fill="none" stroke="{c}" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round">'
                        f'<path d="M22 3l15 6v11c0 10-6.5 17-15 21C13.5 37 7 30 7 20V9z"/><path d="M24 10l-6 11h7l-4 11"/></g>'),
    "shrink": lambda c: (f'<g fill="none" stroke="{c}" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round">'
                         f'<rect x="3" y="3" width="38" height="38" rx="5" stroke-dasharray="4 4"/><rect x="16" y="16" width="18" height="18" rx="3"/>'
                         f'<path d="M7 7l8 8M15 9v6H9"/><circle cx="22" cy="22" r="2"/><path d="M17 31l5-5 4 4 3-3 5 5"/></g>'),
    "aside": lambda c: (f'<g fill="none" stroke="{c}" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round">'
                        f'<path d="M3 8a4 4 0 0 1 4-4h16a4 4 0 0 1 4 4v12a4 4 0 0 1-4 4H12l-6 5v-5.3A4 4 0 0 1 3 20z"/><path d="M9 11h12M9 17h8"/>'
                        f'<rect x="31" y="4" width="10" height="20" rx="2.5"/><path d="M33.5 9h5M33.5 13h5"/><path d="M14 34h27M14 40h18"/></g>'),
}


def card(title, tag, desc, metric, mlabel, icon, accent):
    d = "".join(f'<text x="28" y="{166 + i * 21}" font-size="14.5" fill="{SOFT}">{x(t)}</text>' for i, t in enumerate(desc))
    body = (f'<defs><linearGradient id="a" x1="0" x2="1"><stop offset="0" stop-color="{accent}"/><stop offset="1" stop-color="{accent}" stop-opacity="0"/></linearGradient>'
            f'<radialGradient id="gl" cx="1" cy="0" r="1"><stop offset="0" stop-color="{accent}" stop-opacity=".18"/><stop offset="1" stop-color="{accent}" stop-opacity="0"/></radialGradient></defs>'
            f'<rect x=".5" y=".5" width="299" height="309" rx="14" fill="{PANEL}" stroke="{LINE}"/><rect x=".5" y=".5" width="299" height="309" rx="14" fill="url(#gl)"/>'
            f'<rect x="20" y="0" width="160" height="3" fill="url(#a)"/>'
            f'<g transform="translate(28,30)">{ICONS[icon](accent)}</g>'
            f'<text x="272" y="50" font-size="18" fill="{accent}" text-anchor="end">↗</text>'
            f'<text x="28" y="110" font-size="22" font-weight="700" fill="{TEXT}">{x(title)}</text>'
            f'<text class="m" x="28" y="132" font-size="12" fill="{MUTED}">{x(tag)}</text>{d}'
            f'<line x1="28" y1="234" x2="272" y2="234" stroke="{LINE}"/>'
            f'<text x="28" y="268" font-size="28" font-weight="800" fill="{accent}" letter-spacing="-.5">{x(metric)}</text>'
            f'<text x="28" y="290" font-size="12.5" fill="{MUTED}">{x(mlabel)}</text>')
    return svg(300, 310, body, "", f"{title}: {' '.join(desc)} {metric} {mlabel}")


def footer():
    body = (f'<defs><linearGradient id="f" x1="0" x2="1"><stop offset="0" stop-color="{TEAL}" stop-opacity="0"/><stop offset=".5" stop-color="{ORANGE}"/>'
            f'<stop offset="1" stop-color="{VIOLET}" stop-opacity="0"/></linearGradient></defs><rect y="8" width="900" height="2" fill="url(#f)"/>'
            f'<text class="m" x="450" y="44" font-size="14" fill="{MUTED}" text-anchor="middle">// thanks for scrolling. now go send a webhook twice and see what breaks.</text>')
    return svg(900, 60, body, "", "Thanks for scrolling")


OUT.mkdir(parents=True, exist_ok=True)
(OUT / "hero.svg").write_text(hero())
(OUT / "whoami.svg").write_text(terminal())
(OUT / "footer.svg").write_text(footer())
cards = {
    "card-carbon.svg": ("carbon-layer", "python · pypi · docker", ["Chaos tests for payment webhooks:", "duplicates, out-of-order events", "and forged signatures."], "~150", "handlers scanned, 9 double-charge", "chaos", ORANGE),
    "card-token0.svg": ("token0", "python · pypi · litellm", ["Resizes, crops or OCRs images", "before they reach GPT, Claude", "or Gemini."], "765→85", "tokens on a phone photo", "shrink", VIOLET),
    "card-aside.svg": ("aside", "python · self-hosted", ["Ad server for AI chat apps: a", "sponsored card beside the answer;", "the chat stays on your server."], "v0.3", "live demo: Rasoi AI", "aside", AMBER),
}
for name, args in cards.items():
    (OUT / name).write_text(card(*args))
print("wrote", sorted(p.name for p in OUT.iterdir()))
