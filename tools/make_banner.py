#!/usr/bin/env python3
"""Draw the profile README's banner: assets/banner-light.svg and banner-dark.svg, and banner-narrow.svg for phones.

The fonts are the subsets used by the homepage (repo hey-chillax.github.io, assets/fonts), inlined so the banner
renders the same in every browser when GitHub shows it as an <img>. The banner holds only the name, affiliation and
research directions; everything a reader may want to copy or search (status, links, results) stays in the README text.

    python3 tools/make_banner.py --fonts ../hey-chillax.github.io/assets/fonts
"""
import argparse
import base64
import pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
THEMES = {   # GitHub's own page colours, with the homepage accent
    'light': dict(card='#ffffff', stroke='#d0d7de', ink='#1f2328', muted='#59636e', accent='#2d5a96',
                  pill='#eef3fa', pill_line='#c8d6ea', chip='#c9cfd6', chip_t='#2d5a96'),
    'dark': dict(card='#161b22', stroke='#30363d', ink='#e6edf3', muted='#9198a1', accent='#8db1e6',
                 pill='#19222f', pill_line='#2f4566', chip='#3a414b', chip_t='#5b8fd6'),
}
W, H = 880, 184


def faces(font_dir):
    out = []
    for family, weight, name in [('YZ Serif', 600, 'YZSerif-Semibold.woff2'), ('YZ Sans', 400, 'YZSans-Regular.woff2'),
                                 ('YZ Sans', 600, 'YZSans-Semibold.woff2')]:
        data = base64.b64encode((font_dir / name).read_bytes()).decode()
        out.append(f"@font-face{{font-family:'{family}';font-weight:{weight};src:url(data:font/woff2;base64,{data}) format('woff2')}}")
    return ''.join(out)


def width(s, size, per_char):
    return sum(per_char.get(ch, 0.5) for ch in s) * size


def icon(kind, cx, cy, c):
    """Small line icons in the accent colour."""
    st = f'fill="{c["pill"]}" stroke="{c["accent"]}" stroke-width="1.6" stroke-linejoin="round" stroke-linecap="round"'
    ln = f'fill="none" stroke="{c["accent"]}" stroke-width="1.6" stroke-linejoin="round" stroke-linecap="round"'
    if kind == 'slate':   # clapperboard: the board, and the striped clapstick hinged at its top-left corner
        hx, hy = cx - 10, cy - 3.2
        return (f'<rect x="{cx - 10}" y="{cy - 3}" width="20" height="12.5" rx="2.5" {st}/>'
                f'<g transform="rotate(-14 {hx} {hy})"><rect x="{cx - 10}" y="{cy - 7.6}" width="20" height="4.4" rx="1.2" {st}/>'
                f'<path d="M{cx - 5.2},{cy - 7.6} l-2.6,4.4 M{cx + 0.4},{cy - 7.6} l-2.6,4.4 M{cx + 6},{cy - 7.6} l-2.6,4.4" {ln}/></g>'
                f'<path d="M{cx - 10},{cy + 1.2} H{cx + 10}" {ln}/>')
    if kind == 'image':
        return (f'<rect x="{cx - 10}" y="{cy - 8}" width="20" height="16" rx="3" {st}/>'
                f'<path d="M{cx - 7},{cy + 5} L{cx - 2},{cy - 1} L{cx + 2},{cy + 3} L{cx + 4},{cy + 1} L{cx + 7},{cy + 5}" {ln}/>'
                f'<circle cx="{cx + 4}" cy="{cy - 3.5}" r="1.6" fill="{c["accent"]}"/>')
    if kind == 'relay':
        return (f'<path d="M{cx - 8},{cy - 1} A8,7 0 0 1 {cx + 7},{cy - 3}" {ln}/><path d="M{cx + 3},{cy - 7} L{cx + 7},{cy - 3} L{cx + 2},{cy - 1}" {ln}/>'
                f'<path d="M{cx + 8},{cy + 1} A8,7 0 0 1 {cx - 7},{cy + 3}" {ln}/><path d="M{cx - 3},{cy + 7} L{cx - 7},{cy + 3} L{cx - 2},{cy + 1}" {ln}/>')
    if kind == 'robot':
        return (f'<rect x="{cx - 9}" y="{cy - 5}" width="18" height="13" rx="3.5" {st}/>'
                f'<circle cx="{cx - 3.5}" cy="{cy + 1}" r="1.7" fill="{c["accent"]}"/><circle cx="{cx + 3.5}" cy="{cy + 1}" r="1.7" fill="{c["accent"]}"/>'
                f'<path d="M{cx},{cy - 5} V{cy - 9}" {ln}/><circle cx="{cx}" cy="{cy - 10}" r="1.6" fill="{c["accent"]}"/>')
    if kind == 'bolt':
        return f'<path d="M{cx + 2},{cy - 10} L{cx - 6},{cy + 2} L{cx},{cy + 2} L{cx - 2},{cy + 10} L{cx + 6},{cy - 2} L{cx},{cy - 2} Z" {st}/>'
    raise ValueError(kind)


ITEMS = [('slate', 'Multimodal LLMs'), ('relay', 'Post-training · SFT → RL → OPD'), ('robot', 'Agentic RL'), ('bolt', 'Efficient inference')]
SANS = "'YZ Sans', 'Source Sans 3', -apple-system, 'Segoe UI', Helvetica, Arial, sans-serif"
SERIF = "'YZ Serif', 'Source Serif 4', Georgia, serif"


def banner_narrow(font_dir):
    """The stacked banner the README shows on screens under 600 px. One file for both themes: the colours are CSS
    variables switched by prefers-color-scheme inside the SVG (GitHub's own theme switch only rewrites
    prefers-color-scheme sources, so the width-based source cannot also carry the theme)."""
    L, D = THEMES['light'], THEMES['dark']
    w, h = 440, 318
    var = lambda c: ';'.join(f'--{k}:{c[k]}' for k in ('card', 'stroke', 'ink', 'muted', 'accent', 'pill'))
    css = (faces(font_dir) + f':root{{{var(L)}}}@media (prefers-color-scheme: dark){{:root{{{var(D)}}}}}'
           '.card{fill:var(--card);stroke:var(--stroke)}.ink{fill:var(--ink)}.muted{fill:var(--muted)}.rule{stroke:var(--stroke)}'
           # the icons are drawn with the light colours; these rules repaint them in the current theme
           f'[fill="{L["pill"]}"]{{fill:var(--pill)}}[stroke="{L["accent"]}"]{{stroke:var(--accent)}}[fill="{L["accent"]}"]{{fill:var(--accent)}}')
    parts = [f'<rect class="card" x="1" y="1" width="{w - 2}" height="{h - 2}" rx="14"/>',
             f'<text class="ink" x="28" y="70" font-family="{SERIF}" font-weight="600" font-size="46" letter-spacing="-0.5">Yi Zhang</text>',
             f'<text class="muted" x="29" y="104" font-family="{SANS}" font-size="18">M.S. student · Nanjing University</text>',
             f'<text class="muted" x="29" y="129" font-family="{SANS}" font-size="18">Class of 2028</text>',
             f'<line class="rule" x1="28" y1="154" x2="{w - 28}" y2="154"/>']
    for i, (kind, label) in enumerate(ITEMS):
        y = 188 + i * 35
        parts.append(icon(kind, 47, y, L))
        parts.append(f'<text class="ink" x="72" y="{y + 6.5}" font-family="{SANS}" font-weight="600" font-size="19">{label}</text>')
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" height="{h}" role="img" '
            f'aria-label="Yi Zhang, M.S. student at Nanjing University. Multimodal LLMs, post-training, agentic RL, efficient inference.">'
            f'<style>{css}</style>' + ''.join(parts) + '</svg>\n')


def banner(theme, font_dir):
    c = THEMES[theme]
    sans, serif = SANS, SERIF
    parts = [f'<rect x="1" y="1" width="{W - 2}" height="{H - 2}" rx="14" fill="{c["card"]}" stroke="{c["stroke"]}"/>',
             f'<text x="40" y="92" font-family="{serif}" font-weight="600" font-size="50" fill="{c["ink"]}" letter-spacing="-0.5">Yi Zhang</text>',
             f'<text x="42" y="130" font-family="{sans}" font-size="19" fill="{c["muted"]}">M.S. student · Nanjing University · Class of 2028</text>',
             f'<line x1="500" y1="34" x2="500" y2="{H - 34}" stroke="{c["stroke"]}"/>']
    for i, (kind, label) in enumerate(ITEMS):
        y = 54 + i * 34
        parts.append(icon(kind, 538, y, c))
        parts.append(f'<text x="562" y="{y + 6}" font-family="{sans}" font-weight="600" font-size="17" fill="{c["ink"]}">{label}</text>')
    style = f'<style>{faces(font_dir)}</style>'
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" role="img" '
            f'aria-label="Yi Zhang, M.S. student at Nanjing University. Multimodal LLMs, post-training, agentic RL, efficient inference.">'
            + style + ''.join(parts) + '</svg>\n')


def main():
    ap = argparse.ArgumentParser(description=__doc__.split('\n\n')[0])
    ap.add_argument('--fonts', required=True, type=pathlib.Path, help="the homepage's assets/fonts directory")
    args = ap.parse_args()
    for theme in THEMES:
        (ROOT / 'assets' / f'banner-{theme}.svg').write_text(banner(theme, args.fonts), encoding='utf-8')
    (ROOT / 'assets' / 'banner-narrow.svg').write_text(banner_narrow(args.fonts), encoding='utf-8')
    print('wrote assets/banner-light.svg, assets/banner-dark.svg and assets/banner-narrow.svg')


if __name__ == '__main__':
    main()
