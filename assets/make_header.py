"""Generate the profile header (dark and light) as dependency-free SVG.

Right panel: Black-Scholes call prices C(K, tau) against strike for four
maturities. Background: one seeded geometric Brownian motion path.
Run:  python3 assets/make_header.py
"""
import math
import random

W, H = 1280, 330
MONO = "ui-monospace, SFMono-Regular, 'SF Mono', Menlo, Consolas, 'Liberation Mono', monospace"
SANS = "-apple-system, BlinkMacSystemFont, 'Segoe UI', 'Noto Sans', Helvetica, Arial, sans-serif"

THEMES = {
    "dark": dict(bg0="#0d1117", bg1="#111b2e", border="#30363d", grid="#1b2433", bar="#161b22",
                 title="#8b949e", prompt="#3fb950", name="#f0f6fc", sub="#58a6ff", chip_bg="#0d1117",
                 chip_border="#30363d", chip_text="#c9d1d9", axis="#484f58", label="#8b949e",
                 path="#58a6ff", curves=["#58a6ff", "#3fb950", "#d2a8ff", "#ffa657"]),
    "light": dict(bg0="#ffffff", bg1="#eef3fb", border="#d0d7de", grid="#e6ebf1", bar="#f6f8fa",
                  title="#57606a", prompt="#1a7f37", name="#1f2328", sub="#0969da", chip_bg="#ffffff",
                  chip_border="#d0d7de", chip_text="#424a53", axis="#8c959f", label="#57606a",
                  path="#0969da", curves=["#0969da", "#1a7f37", "#8250df", "#bc4c00"]),
}

CHIPS = ["constrained deep learning", "cross-sectional alpha", "reinforcement learning",
         "market microstructure", "differentiable optimization"]


def norm_cdf(x):
    return 0.5 * (1.0 + math.erf(x / math.sqrt(2.0)))


def bs_call(s, k, tau, sigma, r=0.01):
    d1 = (math.log(s / k) + (r + 0.5 * sigma * sigma) * tau) / (sigma * math.sqrt(tau))
    d2 = d1 - sigma * math.sqrt(tau)
    return s * norm_cdf(d1) - k * math.exp(-r * tau) * norm_cdf(d2)


def call_curves(x0, y0, w, h):
    """Polylines of C(K) for four maturities, scaled into the box (x0, y0, w, h)."""
    s, sigma = 100.0, 0.22
    ks = [70 + 60 * i / 60 for i in range(61)]
    taus = [0.05, 0.25, 0.6, 1.2]
    cmax = bs_call(s, ks[0], taus[-1], sigma)
    out = []
    for tau in taus:
        pts = []
        for k in ks:
            c = bs_call(s, k, tau, sigma)
            x = x0 + (k - ks[0]) / (ks[-1] - ks[0]) * w
            y = y0 + h - c / cmax * h
            pts.append(f"{x:.1f},{y:.1f}")
        out.append(" ".join(pts))
    return out


def gbm_path(x0, x1, y_mid, amp, n=220, seed=7):
    rnd = random.Random(seed)
    level, vals = 0.0, []
    for _ in range(n):
        level += rnd.gauss(0.0006, 0.012)
        vals.append(level)
    lo, hi = min(vals), max(vals)
    pts = []
    for i, v in enumerate(vals):
        x = x0 + (x1 - x0) * i / (n - 1)
        y = y_mid + amp * (0.5 - (v - lo) / (hi - lo))
        pts.append(f"{x:.1f},{y:.1f}")
    return " ".join(pts)


def build(theme):
    t = THEMES[theme]
    px, py, pw, ph = 860, 96, 360, 170  # chart box
    curves = call_curves(px, py, pw, ph)
    parts = [
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" role="img" '
        f'aria-label="Chien-Cheng (Eric) Chu: quantitative research, machine learning, derivatives pricing">',
        '<defs>',
        f'<linearGradient id="bg" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="{t["bg0"]}"/>'
        f'<stop offset="1" stop-color="{t["bg1"]}"/></linearGradient>',
        f'<pattern id="grid" width="40" height="40" patternUnits="userSpaceOnUse">'
        f'<path d="M40 0H0V40" fill="none" stroke="{t["grid"]}" stroke-width="1"/></pattern>',
        f'<linearGradient id="fade" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="{t["path"]}" stop-opacity="0"/>'
        f'<stop offset="0.35" stop-color="{t["path"]}" stop-opacity="0.35"/>'
        f'<stop offset="1" stop-color="{t["path"]}" stop-opacity="0.05"/></linearGradient>',
        f'<clipPath id="card"><rect x="1" y="1" width="{W-2}" height="{H-2}" rx="14"/></clipPath>',
        '</defs>',
        f'<g clip-path="url(#card)">',
        f'<rect width="{W}" height="{H}" fill="url(#bg)"/>',
        f'<rect width="{W}" height="{H}" fill="url(#grid)"/>',
        f'<polyline points="{gbm_path(0, W, 210, 150)}" fill="none" stroke="url(#fade)" stroke-width="1.6"/>',
        f'<rect width="{W}" height="38" fill="{t["bar"]}"/>',
        f'<line x1="0" y1="38" x2="{W}" y2="38" stroke="{t["border"]}"/>',
        '<circle cx="24" cy="19" r="6" fill="#ff5f56"/><circle cx="44" cy="19" r="6" fill="#ffbd2e"/>'
        '<circle cx="64" cy="19" r="6" fill="#27c93f"/>',
        f'<text x="{W/2}" y="24" text-anchor="middle" font-family="{MONO}" font-size="13" fill="{t["title"]}">'
        'eric@quant: ~/research</text>',
        '</g>',
        f'<rect x="1" y="1" width="{W-2}" height="{H-2}" rx="14" fill="none" stroke="{t["border"]}" stroke-width="1.5"/>',
        # left column
        f'<text x="48" y="86" font-family="{MONO}" font-size="15" fill="{t["prompt"]}">$ whoami</text>',
        f'<text x="48" y="140" font-family="{SANS}" font-size="46" font-weight="700" fill="{t["name"]}">'
        'Chien-Cheng (Eric) Chu</text>',
        f'<text x="48" y="176" font-family="{MONO}" font-size="17" fill="{t["sub"]}">'
        'quantitative research · machine learning · derivatives pricing</text>',
    ]
    # chips, two rows
    x, y = 48, 204
    for chip in CHIPS:
        w = int(len(chip) * 7.9 + 24)
        if x + w > 800:
            x, y = 48, y + 36
        parts.append(f'<rect x="{x}" y="{y}" width="{w}" height="26" rx="13" fill="{t["chip_bg"]}" '
                     f'stroke="{t["chip_border"]}"/>')
        parts.append(f'<text x="{x + w/2:.1f}" y="{y + 17.5}" text-anchor="middle" font-family="{MONO}" '
                     f'font-size="13" fill="{t["chip_text"]}">{chip}</text>')
        x += w + 10
    parts.append(f'<text x="48" y="{H - 24}" font-family="{MONO}" font-size="15" fill="{t["prompt"]}">$ '
                 f'<tspan fill="{t["name"]}">▍<animate attributeName="opacity" values="1;1;0;0" dur="1.2s" '
                 'repeatCount="indefinite"/></tspan></text>')
    # right chart
    parts.append(f'<line x1="{px}" y1="{py + ph}" x2="{px + pw}" y2="{py + ph}" stroke="{t["axis"]}"/>')
    parts.append(f'<line x1="{px}" y1="{py - 6}" x2="{px}" y2="{py + ph}" stroke="{t["axis"]}"/>')
    sx = px + (100 - 70) / 60 * pw
    parts.append(f'<line x1="{sx:.1f}" y1="{py}" x2="{sx:.1f}" y2="{py + ph}" stroke="{t["axis"]}" '
                 'stroke-dasharray="3 5"/>')
    for pts, color in zip(curves, t["curves"]):
        parts.append(f'<polyline points="{pts}" fill="none" stroke="{color}" stroke-width="2.2" '
                     'stroke-linejoin="round" stroke-linecap="round"/>')
    parts.append(f'<text x="{px}" y="{py - 16}" font-family="{MONO}" font-size="13" fill="{t["label"]}">'
                 'C(K, τ) · ∂C/∂K ≤ 0 · ∂²C/∂K² ≥ 0</text>')
    parts.append(f'<text x="{px + pw}" y="{py + ph + 20}" text-anchor="end" font-family="{MONO}" font-size="13" '
                 f'fill="{t["label"]}">strike K</text>')
    parts.append(f'<text x="{sx:.1f}" y="{py + ph + 20}" text-anchor="middle" font-family="{MONO}" font-size="13" '
                 f'fill="{t["label"]}">S</text>')
    parts.append('</svg>')
    return "\n".join(parts)


if __name__ == "__main__":
    import os
    here = os.path.dirname(os.path.abspath(__file__))
    for theme in THEMES:
        with open(os.path.join(here, f"header-{theme}.svg"), "w", encoding="utf-8") as fh:
            fh.write(build(theme))
        print("wrote", f"header-{theme}.svg")
