#!/usr/bin/env python3
"""Draw the profile README's banner (assets/banner-light.svg and assets/banner-dark.svg).

The fonts are the subsets used by the homepage (repo hey-chillax.github.io, assets/fonts), inlined so the banner
renders the same in every browser when GitHub shows it as an <img>. The project pictures next to it
(assets/card-*.svg) are exported by the homepage's figure script:

    python3 tools/make_banner.py --fonts ../hey-chillax.github.io/assets/fonts
    (cd ../hey-chillax.github.io && python3 tools/make_figures.py --export /tmp/cards --embed-fonts --only card-opd card-scr \
        && python3 tools/make_figures.py --export /tmp/cards --theme dark --embed-fonts --only card-opd card-scr)
    cp /tmp/cards/en/card-opd.svg assets/card-opd-light.svg; cp /tmp/cards/en/card-opd-dark.svg assets/  # same for card-scr
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
W, H = 880, 200


def faces(font_dir):
    out = []
    for family, weight, name in [('YZ Serif', 600, 'YZSerif-Semibold.woff2'), ('YZ Sans', 400, 'YZSans-Regular.woff2'),
                                 ('YZ Sans', 600, 'YZSans-Semibold.woff2')]:
        data = base64.b64encode((font_dir / name).read_bytes()).decode()
        out.append(f"@font-face{{font-family:'{family}';font-weight:{weight};src:url(data:font/woff2;base64,{data}) format('woff2')}}")
    return ''.join(out)


def width(s, size, per_char):
    return sum(per_char.get(ch, 0.5) for ch in s) * size


def banner(theme, font_dir):
    c = THEMES[theme]
    sans = "'YZ Sans', 'Source Sans 3', -apple-system, 'Segoe UI', Helvetica, Arial, sans-serif"
    serif = "'YZ Serif', 'Source Serif 4', Georgia, serif"
    # approximate advance widths of the pill labels (YZ Sans Semibold, em units)
    per = {ch: 0.52 for ch in 'abcdeghknopqsuvxyz'}
    per.update({ch: 0.27 for ch in 'filjtr '}); per.update({ch: 0.6 for ch in 'ABCDEGHKNOPQRSUVXYZ'}); per.update({'L': 0.48, 'M': 0.75, 'T': 0.55, 'w': 0.74, 'm': 0.82})
    parts = [f'<rect x="1" y="1" width="{W - 2}" height="{H - 2}" rx="14" fill="{c["card"]}" stroke="{c["stroke"]}"/>',
             f'<text x="40" y="84" font-family="{serif}" font-weight="600" font-size="46" fill="{c["ink"]}" letter-spacing="-0.4">Yi Zhang</text>',
             f'<text x="42" y="118" font-family="{sans}" font-size="17" fill="{c["muted"]}">M.S. student · Nanjing University · Class of 2028</text>']
    x = 40
    for label in ['LLM post-training', 'Multimodal LLMs', 'Agentic RL']:
        w = width(label, 13.5, per) + 26
        parts.append(f'<rect x="{x}" y="140" width="{w:.0f}" height="28" rx="14" fill="{c["pill"]}" stroke="{c["pill_line"]}"/>')
        parts.append(f'<text x="{x + w / 2:.1f}" y="158.5" text-anchor="middle" font-family="{sans}" font-weight="600" font-size="13.5" fill="{c["accent"]}">{label}</text>')
        x += w + 10
    # motif: an answer as a paragraph of word-chips, two passages written by the teacher (as on the homepage)
    rows = [[34, 18, 46, 26, 40, 22, 30], [28, 44, 20, 32, 48, 36, 26], [40, 24, 30, 52, 22, 34, 28], [30, 46, 22, 38, 40]]
    teacher = {(1, 3), (1, 4), (1, 5), (3, 2), (3, 3)}
    y0, x0 = 52, 586
    for r, row in enumerate(rows):
        xx = x0
        for col, w in enumerate(row):
            if xx + w > W - 36:
                break
            t = (r, col) in teacher
            parts.append(f'<rect x="{xx}" y="{y0 + r * 26}" width="{w}" height="11" rx="5.5" fill="{c["chip_t"] if t else c["chip"]}"/>')
            xx += w + 6
    style = f'<style>{faces(font_dir)}</style>'
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" role="img" '
            f'aria-label="Yi Zhang, M.S. student at Nanjing University: LLM post-training, multimodal LLMs, agentic RL">'
            + style + ''.join(parts) + '</svg>\n')


def main():
    ap = argparse.ArgumentParser(description=__doc__.split('\n\n')[0])
    ap.add_argument('--fonts', required=True, type=pathlib.Path, help="the homepage's assets/fonts directory")
    args = ap.parse_args()
    for theme in THEMES:
        (ROOT / 'assets' / f'banner-{theme}.svg').write_text(banner(theme, args.fonts), encoding='utf-8')
    print('wrote assets/banner-light.svg and assets/banner-dark.svg')


if __name__ == '__main__':
    main()
