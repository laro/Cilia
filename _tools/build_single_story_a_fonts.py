#!/usr/bin/env python3
"""
Build self-hosted web fonts with the single-story "a" baked in.

Jost and Nunito Sans have a single-story "a" only as stylistic set `ss01`,
which the Google-Fonts/Fontsource web subsets strip. This script takes the
full variable fonts from github.com/google/fonts (pinned commit), maps all
a-letters (a, ä, à, å, ā, ą, ...) directly to their ss01 glyphs, pins every
axis except `wght`, and writes latin + latin-ext woff2 subsets (same
unicode-ranges as Fontsource) to assets/fonts/.

Usage (needs: pip install fonttools brotli):
    python3 _tools/build_single_story_a_fonts.py <empty download dir>
"""
import io
import sys
import unicodedata
import urllib.request
from pathlib import Path

from fontTools import subset
from fontTools.ttLib import TTFont
from fontTools.varLib import instancer

GOOGLE_FONTS_COMMIT = "7af0d90b4d532ffa4b041937b560c6df4e7b1e95"
FONTS = {
    # css file prefix: (path in google/fonts, axis pins besides wght)
    "jost": ("ofl/jost/Jost[wght].ttf", {}),
    "nunito-sans": (
        "ofl/nunitosans/NunitoSans[YTLC,opsz,wdth,wght].ttf",
        {"wdth": 100, "opsz": 12, "YTLC": 500},
    ),
}
SUBSETS = {
    "latin": "U+0000-00FF,U+0131,U+0152-0153,U+02BB-02BC,U+02C6,U+02DA,U+02DC,U+0304,U+0308,U+0329,U+2000-206F,U+20AC,U+2122,U+2191,U+2193,U+2212,U+2215,U+FEFF,U+FFFD",
    "latin-ext": "U+0100-02BA,U+02BD-02C5,U+02C7-02CC,U+02CE-02D7,U+02DD-02FF,U+0304,U+0308,U+0329,U+1D00-1DBF,U+1E00-1E9F,U+1EF2-1EFF,U+2020,U+20A0-20AB,U+20AD-20C0,U+2113,U+2C60-2C7F,U+A720-A7FF",
}
OUT_DIR = Path(__file__).resolve().parent.parent / "assets" / "fonts"


def parse_ranges(spec):
    cps = []
    for part in spec.split(","):
        lo, _, hi = part.removeprefix("U+").partition("-")
        cps.extend(range(int(lo, 16), int(hi or lo, 16) + 1))
    return cps


def ss01_mapping(font):
    gsub = font["GSUB"].table
    mapping = {}
    for rec in gsub.FeatureList.FeatureRecord:
        if rec.FeatureTag != "ss01":
            continue
        for li in rec.Feature.LookupListIndex:
            for st in gsub.LookupList.Lookup[li].SubTable:
                st = getattr(st, "ExtSubTable", st)
                mapping.update(getattr(st, "mapping", {}) or {})
    return mapping


def is_a_letter(cp):
    base = unicodedata.normalize("NFD", chr(cp))[0]
    return base in ("a", "а")  # Latin a, Cyrillic a


def bake_single_story_a(font):
    subst = ss01_mapping(font)
    changed = set()
    for table in font["cmap"].tables:
        if not table.isUnicode():
            continue
        for cp, glyph in list(table.cmap.items()):
            if is_a_letter(cp) and glyph in subst:
                table.cmap[cp] = subst[glyph]
                changed.add(chr(cp))
    if "a" not in changed:
        sys.exit("ss01 does not replace 'a' in this font")
    return changed


def main(download_dir):
    download_dir = Path(download_dir)
    download_dir.mkdir(parents=True, exist_ok=True)
    for prefix, (gf_path, pins) in FONTS.items():
        src = download_dir / Path(gf_path).name
        if not src.exists():
            url = f"https://raw.githubusercontent.com/google/fonts/{GOOGLE_FONTS_COMMIT}/{gf_path}"
            print("download", url)
            urllib.request.urlretrieve(url.replace("[", "%5B").replace("]", "%5D"), src)
        font = TTFont(src)
        if pins:
            font = instancer.instantiateVariableFont(font, pins)
        print(prefix, "single-story:", "".join(sorted(bake_single_story_a(font))))
        buf = io.BytesIO()
        font.save(buf)
        for name, ranges in SUBSETS.items():
            opts = subset.Options()
            opts.flavor = "woff2"
            opts.layout_features = ["*"]
            opts.name_IDs = ["*"]
            opts.notdef_outline = True
            sub = TTFont(io.BytesIO(buf.getvalue()))  # fresh copy per subset
            s = subset.Subsetter(opts)
            s.populate(unicodes=parse_ranges(ranges))
            s.subset(sub)
            out = OUT_DIR / f"{prefix}-{name}-wght-normal.woff2"
            sub.flavor = "woff2"
            sub.save(out)
            print("  wrote", out.relative_to(OUT_DIR.parent.parent), out.stat().st_size, "bytes")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    main(sys.argv[1])
