#!/usr/bin/env python3
"""Pembuat laporan Bab I-III (docx + PDF), regresi harmonik k = 1, curah hujan bulanan Kota Mataram 2020-2025.
Satu berkas mandiri (gabungan dari skrip lama buat_laporan*.py dan buat_pdf_harmonik.py); hanya metode yang dipakai.
Tabel 2.1 dan Daftar Pustaka dibaca dari vault (03 Artikel/, 02 Laporan/); angka dari data_mentah/*.csv.
Teks bab ditulis di dalam skrip ini dan harus sama dengan vault (02 Laporan/).
Keluaran: hasil/Laporan_RegresiHarmonik_Bab1-3.docx dan .pdf (PDF dibuat LibreOffice untuk nomor halaman daftar isi).
Jangan dijalankan jika tidak disuruh (vault: Aturan Kerja).
Jalankan dari folder statistika:  .venv/bin/python vault/Statistika-RegresiHarmonik/build/buat_docx.py
"""
import json
import re
import subprocess
from pathlib import Path
import numpy as np
import pandas as pd
from docx import Document
from docx.enum.section import WD_SECTION
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.enum.text import WD_ALIGN_PARAGRAPH, WD_TAB_ALIGNMENT, WD_TAB_LEADER
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.shared import Cm, Pt, RGBColor
import hashlib
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
matplotlib.use("Agg")

ROOT = Path(__file__).resolve().parents[3]

HASIL = ROOT / "hasil"

df = pd.read_csv(ROOT / "data_mentah" / "curah_hujan_bulanan_bps_bmkg.csv").sort_values(["tahun", "bulan"])

y = df.curah_hujan_mm.to_numpy()

def f(x, d=2):
    return f"{x:.{d}f}".replace(".", ",")

def roman(n):
    out = ""
    for v, s in [(10, "x"), (9, "ix"), (5, "v"), (4, "iv"), (1, "i")]:
        while n >= v:
            out += s; n -= v
    return out

n = len(y)

# Nama dan NIM dibaca dari build/anggota.json (lokal, di-.gitignore karena repo publik).
# Format: [{"nama": "...", "nim": "..."}, ...]
ANGGOTA = [(a["nama"], a["nim"]) for a in json.loads((Path(__file__).with_name("anggota.json")).read_text(encoding="utf-8"))]

def render(docx):
    subprocess.run(["soffice", "--headless", "--convert-to", "pdf", "--outdir", str(docx.parent), str(docx)], check=True, capture_output=True, timeout=240)
    txt = subprocess.run(["pdftotext", "-layout", str(docx.with_suffix(".pdf")), "-"], capture_output=True, text=True, check=True).stdout
    return txt.split("\f")[:-1] if txt.endswith("\f") else txt.split("\f")

def pagemap(pages_txt, entries):
    norm = [re.sub(r"\s+", " ", t) for t in pages_txt]
    lines = [[re.sub(r"\s+", " ", l).strip() for l in t.splitlines()] for t in pages_txt]
    body = next(i for i, ls in enumerate(lines) if "BAB I" in ls and i > 1)
    out = {}
    for _, t in entries["front"]:
        i = next(i for i in range(1, body) if t in lines[i]); out[t] = roman(i)
    keys = [t for _, t in entries["toc"]] + entries["fig"] + entries["tab"] + entries["lamp"]
    for t in keys:
        key = re.sub(r"\s+", " ", t)
        i = next((i for i in range(body, len(norm)) if key in norm[i]), None)
        assert i is not None, f"tidak ketemu di PDF: {t}"
        out[t] = str(i - body + 1)
    return out, body

LAMP = HASIL / "lampiran"

LAMPIRAN_A = [(2020, 2021, 78), (2021, 2022, 84), (2022, 2023, 79), (2023, 2024, 80), (2024, 2025, 73), (2025, 2026, 73)]

VAULT = ROOT / "vault" / "Statistika-RegresiHarmonik"

OUT_H = HASIL / "Laporan_RegresiHarmonik_Bab1-3.docx"

LOGO = VAULT / "Berkas" / "logo_ubg.png"

KER = HASIL / "grafik" / "kerangka_harmonik.png"

_rb = df.groupby("bulan").curah_hujan_mm.mean()

_wet = df[df.bulan.isin([11, 12, 1, 2, 3, 4])].curah_hujan_mm.mean()

_dry = df[~df.bulan.isin([11, 12, 1, 2, 3, 4])].curah_hujan_mm.mean()

c1 = lambda x: f"{x:.1f}".replace(".", ",")

c2 = lambda x: f"{x:.2f}".replace(".", ",")

CITE = {"Astuti 2018": "Astuti dkk. (2018)", "Kusdarwati 2023": "Kusdarwati (2023)", "Anandari 2022": "Anandari dkk. (2022)",
        "Syendra Wanti 2026": "Syendra Wanti dkk. (2026)", "Susilokarti 2016": "Susilokarti dkk. (2016)", "Darmawan 2017": "Darmawan dkk. (2017)",
        "Tulak 2022": "Tulak dkk. (2022)", "Zega 2025": "Zega & Mardiningsih (2025)", "Habinuddin 2019": "Habinuddin dkk. (2019)",
        "Purnama 2021": "Purnama (2021)", "Kotarumalos 2025": "Kotarumalos dkk. (2025)", "Hadinata 2026": "Hadinata dkk. (2026)",
        "Aulia Putri 2026": "Aulia Putri dkk. (2026)", "Azmi 2020": "Azmi dkk. (2020)", "Permata 2024": "Permata dkk. (2024)"}

_t21 = (VAULT / "03 Artikel" / "Tabel 2.1 Penelitian Terdahulu.md").read_text(encoding="utf-8")

TERDAHULU_H = [(CITE[k], d, m, h) for _, k, d, m, h in re.findall(r"^\| (\d+) \| \[\[(.+?)\]\] \| (.*?) \| (.*?) \| (.*?) \|$", _t21, re.M)]

_dp = (VAULT / "02 Laporan" / "Daftar Pustaka.md").read_text(encoding="utf-8")

PUSTAKA_H = [re.sub(r"\*(.+?)\*", r"<i>\1</i>", e.strip()) for e in _dp.split("\n\n") if re.search(r"\((\d{4}|t\.t\.)\)\.", e)]

def gambar_kerangka_harmonik():
    kotak = [("Data curah hujan bulanan\nKota Mataram, 72 bulan\n(BPS, asal BMKG)", 0, 1),
             ("Statistik deskriptif", 1, 1),
             ("Fitur sin dan cos\nperiode 12 bulan;\nOLS dari 72 bulan\ndan uji F", 2, 1),
             ("Kecocokan model:\nR² dan RMSE;\nplot data dan\nnilai duga", 2, 0),
             ("Amplitudo dan fase;\nramalan 12 bulan\ntahun 2026", 1, 0)]
    f, a = plt.subplots(figsize=(7.0, 3.2)); a.set_xlim(-0.55, 2.55); a.set_ylim(-0.5, 1.5); a.axis("off")
    for t, x, r in kotak:
        a.add_patch(FancyBboxPatch((x - 0.40, r - 0.30), 0.80, 0.60, boxstyle="round,pad=0.02", fc="#FFFFFF", ec="#1F2A36", lw=1.6))
        a.text(x, r, t, ha="center", va="center", fontsize=9.0, color="#111111")
    arrow = dict(arrowstyle="-|>", color="#1F2A36", lw=2.6, mutation_scale=24, shrinkA=0, shrinkB=0)
    for (x1, y1), (x2, y2) in [((0.43, 1), (0.57, 1)), ((1.43, 1), (1.57, 1)), ((2, 0.67), (2, 0.33)), ((1.57, 0), (1.43, 0))]:
        a.annotate("", xy=(x2, y2), xytext=(x1, y1), arrowprops=arrow)
    f.tight_layout(); f.savefig(KER, dpi=200); plt.close(f)

XL_JUDUL = ["Sheet Data: matriks tahun × bulan, rata-rata, dan pembandingan dengan rata-rata BPS",
            "Sheet Data: grafik rata-rata per bulan dan deret waktu 72 bulan",
            "Sheet Ringkasan: mean, median, modus, simpangan baku, minimum, maksimum, dan jumlah data",
            "Sheet Ringkasan: rata-rata musim, rata-rata per bulan, dan ringkasan 72 data"]  # ponytail: pasangkan urut dengan harmonik_excel_*.png; ubah bila tangkapan berbeda


def _bm_name(txt):
    return "_Toc" + str(int(hashlib.md5(re.sub(r"\s+", " ", txt).encode()).hexdigest()[:8], 16))


class Builder:
    def __init__(self, entries=None, pages=None):
        self.entries = entries            # None = lintasan kumpul
        self.pages = pages or {}
        self.found = dict(toc=[], fig=[], tab=[], lamp=[], front=[])
        self.d = Document()
        self._style()
        self.sec_body = None

    def _style(self):
        d = self.d
        sec = d.sections[0]
        sec.page_width, sec.page_height = Cm(21), Cm(29.7)
        sec.left_margin, sec.right_margin, sec.top_margin, sec.bottom_margin = Cm(4), Cm(3), Cm(3), Cm(3)
        for nm, size, bold, ital in [("Normal", 12, False, False), ("Heading 1", 12, True, False), ("Heading 2", 12, True, False), ("Heading 3", 12, True, True)]:
            st = d.styles[nm]
            st.font.name, st.font.size, st.font.bold, st.font.italic = "Times New Roman", Pt(size), bold, ital
            st.font.color.rgb = RGBColor(0, 0, 0)
            rf = st.element.get_or_add_rPr().get_or_add_rFonts()
            for a in list(rf.attrib):
                if "Theme" in a: del rf.attrib[a]
            for a in ("ascii", "hAnsi", "eastAsia", "cs"): rf.set(qn(f"w:{a}"), "Times New Roman")
        n = d.styles["Normal"].paragraph_format
        n.space_after, n.space_before, n.line_spacing = Pt(0), Pt(0), 1.5
        h1 = d.styles["Heading 1"].paragraph_format
        h1.alignment, h1.space_before, h1.space_after, h1.page_break_before, h1.keep_with_next = WD_ALIGN_PARAGRAPH.CENTER, Pt(0), Pt(18), True, True
        h1.line_spacing = 1.5
        for nm in ("Heading 2", "Heading 3"):
            h = d.styles[nm].paragraph_format
            h.space_before, h.space_after, h.keep_with_next, h.line_spacing = Pt(12), Pt(6), True, 1.5

    def runs(self, p, text, size=None):
        for tok in re.split(r"(_\{[^}]*\}|\^\{[^}]*\}|<i>.*?</i>|<b>.*?</b>)", text):
            if not tok: continue
            if tok.startswith("_{"): r = p.add_run(tok[2:-1]); r.font.subscript = True
            elif tok.startswith("^{"): r = p.add_run(tok[2:-1]); r.font.superscript = True
            elif tok.startswith("<i>"): r = p.add_run(tok[3:-4]); r.italic = True
            elif tok.startswith("<b>"): r = p.add_run(tok[3:-4]); r.bold = True
            else: r = p.add_run(tok)
            if size: r.font.size = Pt(size)

    def runs_url(self, p, text, size=None):
        """Seperti runs, tetapi URL dibuat hyperlink eksternal yang bisa diklik (garis bawah, biru)."""
        from docx.opc.constants import RELATIONSHIP_TYPE as RT
        for tok in re.split(r"(https?://\S+)", text):
            if not tok: continue
            if not tok.startswith("http"):
                self.runs(p, tok, size); continue
            url = tok.rstrip(".,;)")
            rid = p.part.relate_to(url, RT.HYPERLINK, is_external=True)
            h = OxmlElement("w:hyperlink"); h.set(qn("r:id"), rid); h.set(qn("w:history"), "1")
            r = OxmlElement("w:r"); rpr = OxmlElement("w:rPr")
            u = OxmlElement("w:u"); u.set(qn("w:val"), "single"); c = OxmlElement("w:color"); c.set(qn("w:val"), "0563C1")
            rpr.append(c); rpr.append(u)
            if size:
                sz = OxmlElement("w:sz"); sz.set(qn("w:val"), str(int(size * 2))); rpr.append(sz)
            r.append(rpr); tx = OxmlElement("w:t"); tx.text = url; tx.set(qn("xml:space"), "preserve"); r.append(tx)
            h.append(r); p._p.append(h)
            if len(tok) > len(url): self.runs(p, tok[len(url):], size)

    def para(self, text, indent=True, align="j", after=0, keep=False, size=None, spacing=None):
        p = self.d.add_paragraph()
        pf = p.paragraph_format
        pf.alignment = {"j": WD_ALIGN_PARAGRAPH.JUSTIFY, "c": WD_ALIGN_PARAGRAPH.CENTER, "l": WD_ALIGN_PARAGRAPH.LEFT}[align]
        if indent: pf.first_line_indent = Cm(1.25)
        pf.space_after = Pt(after); pf.keep_with_next = keep
        if spacing: pf.line_spacing = spacing
        self.runs(p, text, size)
        return p

    def lst(self, items, numbered=True):
        for i, t in enumerate(items, 1):
            p = self.d.add_paragraph()
            pf = p.paragraph_format
            pf.alignment, pf.left_indent, pf.first_line_indent = WD_ALIGN_PARAGRAPH.JUSTIFY, Cm(1.9), Cm(-0.65)
            self.runs(p, (f"{i}. " if numbered else "- ") + t)

    def eq(self, text):
        p = self.d.add_paragraph(); p.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p.paragraph_format.space_after = Pt(6); self.runs(p, text); return p

    def h1(self, text, kind="toc", multiline=None):
        p = self.d.add_paragraph(style="Heading 1")
        if multiline:
            p.add_run(multiline[0]); p.add_run().add_break(); p.add_run(multiline[1])
            self.found[kind].append((1, f"{multiline[0]} {multiline[1]}"))
        else:
            p.add_run(text); self.found[kind].append((1, text))
        return p

    def h2(self, num, text):
        self.d.add_paragraph(f"{num}  {text}", style="Heading 2"); self.found["toc"].append((2, f"{num}  {text}"))

    def table(self, header, rows, widths, align=None, size=10, bold_last=False):
        t = self.d.add_table(rows=1, cols=len(header)); t.style = "Table Grid"; t.alignment = WD_TABLE_ALIGNMENT.CENTER
        t.autofit = False
        align = align or ["l"] + ["r"] * (len(header) - 1)

        def cell(c, text, bold=False, shade=False, al="l"):
            c.text = ""
            p = c.paragraphs[0]; p.paragraph_format.line_spacing = 1.0
            p.paragraph_format.alignment = {"l": WD_ALIGN_PARAGRAPH.LEFT, "r": WD_ALIGN_PARAGRAPH.RIGHT, "c": WD_ALIGN_PARAGRAPH.CENTER}[al]
            self.runs(p, str(text), size)
            for r in p.runs: r.bold = bold or None
            if shade:
                sh = OxmlElement("w:shd"); sh.set(qn("w:val"), "clear"); sh.set(qn("w:fill"), "D9D9D9"); c._tc.get_or_add_tcPr().append(sh)

        for i, h in enumerate(header): cell(t.rows[0].cells[i], h, True, True, "c")
        trPr = t.rows[0]._tr.get_or_add_trPr(); th = OxmlElement("w:tblHeader"); th.set(qn("w:val"), "true"); trPr.append(th)
        for ri, row in enumerate(rows):
            cs = t.add_row().cells
            for i, v in enumerate(row): cell(cs[i], v, bold_last and ri == len(rows) - 1, False, align[i])
        for row in t.rows[:-1]:
            for c in row.cells:
                for pp in c.paragraphs: pp.paragraph_format.keep_with_next = True
        for row in t.rows:
            cant = OxmlElement("w:cantSplit"); cant.set(qn("w:val"), "true"); row._tr.get_or_add_trPr().append(cant)
            for i, w in enumerate(widths): row.cells[i].width = Cm(w)
        sp = self.d.add_paragraph(); sp.paragraph_format.line_spacing = 1.0; sp.paragraph_format.space_after = Pt(4)
        return t

    def _pgnum(self, sec, fmt, start):
        for e in sec._sectPr.findall(qn("w:pgNumType")): sec._sectPr.remove(e)
        el = OxmlElement("w:pgNumType"); el.set(qn("w:fmt"), fmt); el.set(qn("w:start"), str(start)); sec._sectPr.append(el)

    def _footer_page(self, sec):
        sec.footer.is_linked_to_previous = False
        p = sec.footer.paragraphs[0]; p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        for t, txt in (("begin", None), (None, " PAGE "), ("end", None)):
            r = p.add_run(); r.font.size = Pt(11)
            if t: fc = OxmlElement("w:fldChar"); fc.set(qn("w:fldCharType"), t); r._r.append(fc)
            else: it = OxmlElement("w:instrText"); it.set(qn("xml:space"), "preserve"); it.text = txt; r._r.append(it)

    def new_section(self, fmt):
        sec = self.d.add_section(WD_SECTION.NEW_PAGE)
        self._pgnum(sec, fmt, 1); self._footer_page(sec); return sec

    def pg(self, key):
        return self.pages.get(key, "0")



class Ringkas(Builder):
    sampai = 5
    grafik3 = False
    kerangka = False
    def _style(self):
        super()._style()
        st = self.d.styles
        st["Normal"].paragraph_format.line_spacing = 1.15
        h = st["Heading 1"].paragraph_format
        h.page_break_before, h.space_before, h.space_after, h.line_spacing = True, Pt(0), Pt(14), 1.15
        for nm in ("Heading 2", "Heading 3"):
            g = st[nm].paragraph_format
            g.space_before, g.space_after, g.line_spacing = Pt(8), Pt(3), 1.15

    def h1(self, text, kind="toc", multiline=None, brk=None):
        p = super().h1(text, kind, multiline)
        # judul BAB selalu halaman baru; Abstrak, Kata Pengantar, dan daftar-daftar ikut brk (default tidak)
        p.paragraph_format.page_break_before = bool(multiline) if brk is None else brk
        return p

    def table(self, header, rows, widths, align=None, size=10, bold_last=False):
        tot = sum(widths)
        if tot > 14.0: widths = [w * 14.0 / tot for w in widths]  # muat dalam lebar teks 14 cm
        t = super().table(header, rows, widths, align, size, bold_last)
        for col, w in zip(t.columns, widths): col.width = Cm(w)  # kisi tabel (dipakai LibreOffice)
        return t



class Revisi(Ringkas):
    sampai = 3
    def _fld(self, p, kind=None, instr=None):
        run = p.add_run()
        if kind: fc = OxmlElement("w:fldChar"); fc.set(qn("w:fldCharType"), kind); run._r.append(fc)
        if instr is not None:
            it = OxmlElement("w:instrText"); it.set(qn("xml:space"), "preserve"); it.text = f" {instr} "; run._r.append(it)

    def caption(self, label, nomor, judul, before=True, gaya=None):
        """Keterangan berupa teks biasa dengan gaya khusus; daftar tabel/gambar = TOC \\t gaya ini."""
        gaya = gaya or f"Keterangan {label}"
        p = self.d.add_paragraph(style=gaya)
        pf = p.paragraph_format
        pf.alignment = WD_ALIGN_PARAGRAPH.CENTER if label == "Gambar" else WD_ALIGN_PARAGRAPH.LEFT
        pf.keep_with_next = before; pf.line_spacing = 1.0; pf.space_before, pf.space_after = Pt(8 if before else 2), Pt(4 if before else 10)
        b = p.add_run(f"{label} {nomor}"); b.bold = True
        p.add_run(f" {judul}")
        ol = OxmlElement("w:outlineLvl"); ol.set(qn("w:val"), "2"); p._p.get_or_add_pPr().append(ol)  # panel Navigation (level 3); tidak masuk TOC \\o "1-2"
        if gaya == f"Keterangan {label}":
            self.found["fig" if label == "Gambar" else "tab"].append(f"{label} {nomor} {judul}")
        return p

    def tab_caption(self, nomor, judul):
        self.caption("Tabel", nomor, judul)

    def figure(self, nomor, judul, fname, w=13, sumber=None, path=None, gaya=None):
        p = self.d.add_paragraph(); pf = p.paragraph_format
        pf.alignment = WD_ALIGN_PARAGRAPH.CENTER; pf.keep_with_next = True; pf.line_spacing = 1.0; pf.space_before = Pt(6)
        p.add_run().add_picture(str(path or HASIL / "grafik" / fname), width=Cm(w))
        self.caption("Gambar", nomor, judul, before=bool(sumber), gaya=gaya)
        if sumber:
            s = self.d.add_paragraph(); s.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.CENTER
            s.paragraph_format.line_spacing = 1.0; s.paragraph_format.space_after = Pt(10)
            self.runs(s, sumber, 10)

    def _style(self):
        super()._style()
        st = self.d.styles
        for nm in ("Keterangan Tabel", "Keterangan Gambar", "Keterangan Lampiran"):
            c = st.add_style(nm, 1); c.base_style = st["Normal"]
            c.font.name, c.font.size, c.font.bold, c.font.italic = "Times New Roman", Pt(11), False, False
        for nm in ("TOC 1", "TOC 2", "TOC 3", "Table of Figures"):
            try:
                s = st[nm]
            except KeyError:
                s = st.add_style(nm, 1)
            s.font.name, s.font.size = "Times New Roman", Pt(12 if nm == "TOC 1" else 11.5)
            s.paragraph_format.line_spacing, s.paragraph_format.space_after = 1.15, Pt(3)
            if nm == "TOC 2": s.paragraph_format.left_indent = Cm(0.75)
            if nm == "TOC 3": s.paragraph_format.left_indent = Cm(1.5)
            s.paragraph_format.tab_stops.add_tab_stop(Cm(14), WD_TAB_ALIGNMENT.RIGHT, WD_TAB_LEADER.DOTS)

    def h2l(self, text):
        self.d.add_paragraph(text, style="Heading 2"); self.found["toc"].append((2, text))



class Harmonik(Revisi):
    """Revisi + daftar isi/tabel/gambar yang bisa diklik (hyperlink ke bookmark di judul/keterangan)."""
    _bm_id = 0
    def _bookmark(self, p, txt):
        Harmonik._bm_id += 1
        st = OxmlElement("w:bookmarkStart"); st.set(qn("w:id"), str(Harmonik._bm_id)); st.set(qn("w:name"), _bm_name(txt))
        en = OxmlElement("w:bookmarkEnd"); en.set(qn("w:id"), str(Harmonik._bm_id))
        ppr = p._p.pPr
        (ppr.addnext(st) if ppr is not None else p._p.insert(0, st)); p._p.append(en)

    def h1(self, text, kind="toc", multiline=None, brk=None):
        p = super().h1(text, kind, multiline, brk); self._bookmark(p, self.found[kind][-1][1]); return p

    def h2(self, num, text):
        super().h2(num, text); self._bookmark(self.d.paragraphs[-1], self.found["toc"][-1][1])

    def h2l(self, text):
        super().h2l(text); self._bookmark(self.d.paragraphs[-1], self.found["toc"][-1][1])

    def figure(self, nomor, judul, fname, w=13, sumber=None, path=None, gaya=None):
        n0 = len(self.d.paragraphs)
        w = min(w, 13.3)  # LibreOffice menggeser gambar ±0,3 cm; 13,3 cm aman di dalam lebar teks 14 cm
        super().figure(nomor, judul, fname, w, sumber, path, gaya)
        pf = self.d.paragraphs[n0].paragraph_format  # paragraf gambar: tanpa indentasi agar tidak keluar margin kanan
        pf.first_line_indent = pf.left_indent = pf.right_indent = Cm(0)

    def caption(self, label, nomor, judul, before=True, gaya=None):
        p = super().caption(label, nomor, judul, before, gaya)
        if gaya in (None, f"Keterangan {label}"): self._bookmark(p, f"{label} {nomor} {judul}")
        return p

    def field(self, instr, items):
        items = items or [("Klik kanan lalu pilih Update Field.", "Normal")]
        for k, (txt, sty) in enumerate(items):
            p = self.d.add_paragraph(style=sty)
            if k == 0: self._fld(p, "begin"); self._fld(p, instr=instr); self._fld(p, "separate")
            if sty == "Normal":
                p.add_run(txt)
            else:
                h = OxmlElement("w:hyperlink"); h.set(qn("w:anchor"), _bm_name(txt)); h.set(qn("w:history"), "1")
                for part in (txt, None, self.pg(txt)):
                    r = OxmlElement("w:r")
                    if part is None: r.append(OxmlElement("w:tab"))
                    else:
                        t = OxmlElement("w:t"); t.set(qn("xml:space"), "preserve"); t.text = part; r.append(t)
                    h.append(r)
                p._p.append(h)
            if k == len(items) - 1: self._fld(p, "end")

    def build(self):
        d = self.d
        # ===== sampul =====
        for _ in range(2): d.add_paragraph()
        self.para("<b>ANALISIS CURAH HUJAN BULANAN KOTA MATARAM TAHUN\u00a02020\u20112025 DAN PERAMALAN TAHUN\u00a02026 DENGAN MODEL REGRESI HARMONIK</b>", indent=False, align="c", after=24)
        self.para("Dosen Pengampu:", indent=False, align="c")
        self.para("Siti Soraya, M.Si", indent=False, align="c", after=30)
        p = d.add_paragraph(); p.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p.add_run().add_picture(str(LOGO), width=Cm(4.5))
        d.add_paragraph()
        self.para("Disusun Oleh:", indent=False, align="c")
        for nm, nim in ANGGOTA: self.para(f"{nm} ({nim})", indent=False, align="c")
        for _ in range(3): d.add_paragraph()
        for t in ("PROGRAM STUDI S1 ILMU KOMPUTER", "FAKULTAS TEKNIK", "UNIVERSITAS BUMIGORA", "2026/2027"):
            self.para(f"<b>{t}</b>", indent=False, align="c")
        d.sections[0].footer.is_linked_to_previous = False

        # ===== abstrak (4 paragraf) =====
        self.new_section("lowerRoman")
        self.h1("ABSTRAK", "front")
        self.para(f"Curah hujan Kota Mataram berpola musiman: rata-rata Desember 2020-2025 sebesar {c1(_rb[12])} mm, sedangkan Juli hanya {c1(_rb[7])} mm. "
                  "Besarnya curah hujan bulanan berdampak pada pertanian, ketersediaan air, dan risiko banjir maupun kekeringan, sehingga diperlukan model yang dapat menggambarkan dan meramalkan pola musimannya.")
        self.para("Penelitian ini bertujuan mengetahui hasil peramalan curah hujan bulanan Kota Mataram tahun 2026 dengan model regresi harmonik.")
        self.para("Data sekunder berupa 72 pengamatan bulanan Januari 2020 sampai Desember 2025 dari Tabel 1.2.1 publikasi <i>Kota Mataram dalam Angka</i> 2021 sampai 2026 (data asal BMKG). "
                  "Seluruh 72 data dipakai menyusun model. Tahapannya statistik deskriptif, "
                  "pembentukan variabel sinus dan kosinus berperiode 12 bulan, estimasi <i>Ordinary Least Squares</i> dengan uji F, "
                  "penilaian kecocokan model dengan R^{2} dan RMSE, lalu peramalan 12 bulan tahun 2026.")
        self.para("Laporan ini memuat Bab I sampai Bab III. Hasil yang akan diperoleh berupa persamaan regresi harmonik dengan amplitudo dan fase musiman, nilai R^{2} dan RMSE, serta ramalan curah hujan bulanan Januari sampai Desember 2026.")
        self.para("<b>Kata kunci:</b> curah hujan, Kota Mataram, deret waktu, regresi harmonik, deret Fourier, RMSE", indent=False)

        # ===== kata pengantar =====
        self.h1("KATA PENGANTAR", "front", brk=True)
        self.para("Puji syukur kami panjatkan ke hadirat Tuhan Yang Maha Esa sehingga laporan tugas mata kuliah Statistika berjudul \"Analisis Curah Hujan Bulanan Kota Mataram Tahun 2020-2025 dan Peramalan Tahun 2026 dengan Model Regresi Harmonik\" dapat diselesaikan. "
                  "Laporan ini disusun untuk tugas Program Studi S1 Ilmu Komputer, Fakultas Teknik, Universitas Bumigora.")
        self.para("Laporan memuat Bab I Pendahuluan, Bab II Kajian Pustaka, dan Bab III Metode Penelitian. Seluruh data curah hujan bersumber dari BMKG dan dimuat dalam publikasi resmi BPS Kota Mataram; "
                  "tidak ada angka yang diisi atau diperkirakan sendiri. Hal yang tidak lazim pada sumber data dicatat pada Bab III.")
        self.para("Penulis berterima kasih kepada Ibu Siti Soraya, M.Si selaku dosen pengampu atas arahan dan koreksi selama konsultasi, serta terbuka terhadap masukan untuk perbaikan laporan ini.")
        self.para("Mataram, November 2026", indent=False, align="l")
        self.para("Penulis", indent=False, align="l")

        # ===== daftar isi / tabel / gambar (field Word) =====
        self.h1("DAFTAR ISI", "front", brk=True)
        e = self.entries or {}
        self.field('TOC \\o "1-2" \\h \\z \\u', [(t, "TOC 1" if lv == 1 else "TOC 2") for lv, t in e.get("front", []) + e.get("toc", [])])
        self.h1("DAFTAR TABEL", "front", brk=True)
        self.field('TOC \\h \\z \\t "Keterangan Tabel,1"', [(t, "Table of Figures") for t in e.get("tab", [])])
        self.h1("DAFTAR GAMBAR", "front", brk=True)
        self.field('TOC \\h \\z \\t "Keterangan Gambar,1"', [(t, "Table of Figures") for t in e.get("fig", [])])

        # ===== BAB I =====
        self.new_section("decimal")
        self.h1(None, multiline=("BAB I", "PENDAHULUAN"))
        self.h2("1.1", "Latar Belakang")
        for t in [
            "Curah hujan adalah unsur iklim yang berpengaruh pada pertanian (Hadinata dkk., 2026), pengelolaan sumber daya air, dan risiko bencana hidrometeorologi (Aulia Putri dkk., 2026). "
            "Curah hujan tinggi dalam waktu lama dapat memicu banjir dan tanah longsor (Aulia Putri dkk., 2026), sedangkan musim kemarau yang panjang membuat wilayah rentan kekeringan (Aulia Putri dkk., 2026). "
            "Karena itu, gambaran dan perkiraan curah hujan bulanan diperlukan untuk perencanaan, mitigasi bencana, dan pengelolaan sumber daya air (Aulia Putri dkk., 2026).",
            "Iklim Indonesia didominasi pola hujan monsunal (Kusdarwati, 2023; Tulak dkk., 2022), dengan musim hujan sekitar November sampai April dan kemarau sekitar Mei sampai Oktober (Permata dkk., 2024). "
            f"Data Kota Mataram 2020-2025 menunjukkan pola yang sama: rata-rata November sampai April {c1(_wet)} mm, sedangkan Mei sampai Oktober {c1(_dry)} mm. Pola naik-turun ini berulang setiap tahun.",
            "Kota Mataram adalah pusat kegiatan sosial dan ekonomi Provinsi Nusa Tenggara Barat, sehingga informasi curah hujan dibutuhkan untuk perencanaan wilayah (Hadinata dkk., 2026). "
            "Data curah hujan bulanan Kota Mataram tersedia secara terbuka pada publikasi tahunan <i>Kota Mataram dalam Angka</i> yang diterbitkan BPS dengan data asal BMKG. "
            "Data curah hujan bulanan dari BPS juga dipakai sebagai sumber data penelitian peramalan curah hujan di daerah lain (Kusdarwati, 2023; Purnama, 2021).",
            "Data curah hujan bulanan adalah deret waktu, yaitu pengamatan yang berurutan menurut waktu. Analisis spektral pada curah hujan bulanan di Subang dan di satu kota di Jawa Barat menunjukkan pola yang berulang dengan periode sekitar 12 bulan, "
            "meskipun bentuk pola musimannya dapat berubah antarperiode (Susilokarti dkk., 2016; Darmawan dkk., 2017). Pola berulang seperti ini lebih tepat digambarkan dengan fungsi periodik daripada garis lurus terhadap waktu.",
            "Regresi harmonik memodelkan pola periodik dengan fungsi sinus dan kosinus dari waktu, dan sudah dipakai pada data curah hujan Indonesia (Kusdarwati, 2023; Zega & Mardiningsih, 2025). "
            "Model ini menggambarkan puncak musim hujan dan lembah musim kemarau sebagai satu gelombang (Kusdarwati, 2023; Syendra Wanti dkk., 2026). "
            "Analisis spektral pada curah hujan Kota Bandung dan Kota Jayapura juga menemukan periode dominan sekitar 12 bulan (Habinuddin dkk., 2019; Tulak dkk., 2022), dan periodogram curah hujan bulanan tiga kota di Jawa Timur menunjukkan periode musiman satu tahun (Kusdarwati, 2023).",
            "Model ARIMA musiman (SARIMA) banyak dipakai dalam peramalan curah hujan, antara lain oleh Purnama (2021) dan Aulia Putri dkk. (2026). "
            "Kusdarwati (2023) memodelkan komponen musiman lebih dulu dengan fungsi harmonik, baru kemudian memeriksa autokorelasi residualnya. "
            "Dibandingkan model SARIMA, regresi harmonik orde pertama (k = 1) hanya memerlukan tiga parameter, dapat ditafsirkan melalui amplitudo dan fase, serta menghasilkan kurva ramalan yang tetap mengikuti siklus tahunan (Kusdarwati, 2023; Zega & Mardiningsih, 2025).",
            "Penelitian curah hujan di Kota Mataram sebelumnya memakai LSTM dengan data harian BMKG (Hadinata dkk., 2026) dan regresi nonparametrik deret Fourier pada tiga stasiun untuk prediksi tahun 2017 (Astuti dkk., 2018). "
            "Penelitian ini melanjutkan Astuti dkk. (2018) dengan data Kota Mataram yang lebih baru, yaitu 72 data bulanan resmi BPS (2020-2025), dan mengikuti alur Kusdarwati (2023): daerah dengan satu periode ulang tahunan dapat dimodelkan dengan regresi harmonik orde pertama. "
            "Koefisien ditaksir dengan <i>Ordinary Least Squares</i> (OLS) dari seluruh data, kecocokan model dinilai dengan R^{2} dan RMSE seperti pada Kotarumalos dkk. (2025), lalu model dipakai meramal curah hujan bulanan tahun 2026. Laporan ini memuat Bab I sampai Bab III.",
        ]: self.para(t)
        self.h2("1.2", "Rumusan Masalah")
        self.para("Bagaimana hasil peramalan curah hujan bulanan Kota Mataram tahun 2026 dengan model regresi harmonik?")
        self.h2("1.3", "Batasan Masalah")
        self.lst(["Lokasi hanya Kota Mataram, Provinsi Nusa Tenggara Barat.",
                  "Periode Januari 2020 sampai Desember 2025, 72 pengamatan bulanan.",
                  "Data sekunder dari publikasi BPS Kota Mataram (<i>Kota Mataram dalam Angka</i> edisi 2021-2026), tidak diunduh langsung dari portal BMKG.",
                  "Metode hanya regresi harmonik univariat; variabel meteorologi lain seperti suhu, tekanan udara, dan indeks ENSO tidak dimasukkan.",
                  "Seluruh 72 data dipakai menyusun model. Ramalan dibuat untuk Januari sampai Desember 2026 dan belum dapat dibandingkan dengan data aktual karena data 2026 belum terbit."], numbered=False)
        self.h2("1.4", "Tujuan Penelitian")
        self.para("Mengetahui hasil peramalan curah hujan bulanan Kota Mataram tahun 2026 dengan model regresi harmonik.")
        self.h2("1.5", "Manfaat Penelitian")
        self.para("Memberi contoh penerapan regresi harmonik pada data curah hujan bulanan resmi, dari data mentah sampai ramalan tahun 2026, lengkap dengan sumber dan keterbatasan data, "
                  "serta gambaran pola musiman curah hujan Kota Mataram (waktu puncak dan lembah, serta besar ayunannya) yang dapat dipakai untuk perencanaan pertanian dan kesiapsiagaan bencana.")

        # ===== BAB II =====
        self.h1(None, multiline=("BAB II", "KAJIAN PUSTAKA"))
        self.h2("2.1", "Curah Hujan")
        self.para("Hujan adalah peristiwa jatuhnya butiran air dalam bentuk cair atau padat ke permukaan bumi. Curah hujan diukur dalam milimeter (mm); curah hujan 1 mm berarti air hujan setinggi 1 mm tertampung pada permukaan datar seluas 1 m² tanpa meresap, mengalir, atau menguap (Habinuddin dkk., 2019); volume itu setara dengan 1 liter per meter persegi. "
                  "Di Indonesia, musim hujan umumnya terjadi sekitar November sampai April dan kemarau sekitar Mei sampai Oktober (Permata dkk., 2024); pembagian ini dipakai untuk membandingkan rata-rata musiman.")
        self.h2("2.2", "Deret Waktu")
        self.para("Deret waktu (data runtun waktu) adalah serangkaian pengamatan terhadap suatu peubah yang diukur menurut urutan waktu, misalnya harian atau bulanan (Habinuddin dkk., 2019). Pengamatan yang dibuat berurutan sepanjang waktu itu dianalisis untuk mengenali pola dan meramalkan nilai berikutnya (Zega & Mardiningsih, 2025). Data curah hujan bulanan termasuk deret waktu (Habinuddin dkk., 2019; Zega & Mardiningsih, 2025).")
        self.h2("2.3", "Statistika Deskriptif")
        self.para("Statistika deskriptif merangkum data dengan ukuran pemusatan dan ukuran penyebaran (Sudaryono, 2021). Penelitian curah hujan di Kota Ambon dan Kota Bengkulu juga memulai analisis dengan rata-rata, simpangan baku, nilai minimum, dan nilai maksimum (Kotarumalos dkk., 2025; Syendra Wanti dkk., 2026). Mean adalah jumlah nilai dibagi banyaknya data, median nilai tengah data terurut, dan modus nilai yang paling sering muncul. "
                  "Simpangan baku sampel mengukur sebaran data terhadap mean, dengan pembagi n − 1 karena data merupakan sampel (Sudaryono, 2021):")
        self.eq("x̄ = Σx_{i} / n        s = √[ Σ(x_{i} − x̄)^{2} / (n − 1) ]")
        self.h2("2.4", "Regresi Harmonik")
        self.para("Regresi harmonik memakai fungsi sinus dan kosinus (deret Fourier) untuk memodelkan pola periodik (Kusdarwati, 2023; Zega & Mardiningsih, 2025). Untuk data bulanan dengan periode T = 12 bulan, frekuensi sudutnya ω = 2π/12, dan model orde pertama (k = 1) adalah:")
        self.eq("Y_{t} = b_{0} + b_{1} sin(2πt/12) + b_{2} cos(2πt/12) + ε_{t}")
        self.para("dengan Y_{t} curah hujan bulan ke-t, b_{0} intersep, b_{1} dan b_{2} koefisien sinus dan kosinus, serta ε_{t} galat acak dengan rata-rata nol. Orde pertama dipakai karena curah hujan di daerah yang hanya memiliki satu periode ulang, misalnya satu tahun, dapat dimodelkan dengan harmonik orde satu (Kusdarwati, 2023). "
                  "Koefisien ditaksir dengan <i>Ordinary Least Squares</i> (OLS), yaitu meminimalkan jumlah kuadrat galat (Astuti dkk., 2018; Kotarumalos dkk., 2025). Analisis harmonik memberikan informasi frekuensi dan amplitudo siklus (Zega & Mardiningsih, 2025). Bentuk gelombangnya ditafsirkan melalui amplitudo A (setengah jarak puncak ke lembah) dan fase φ (letak puncak dalam setahun); rumusnya diturunkan dari identitas trigonometri:")
        self.eq("A = √(b_{1}^{2} + b_{2}^{2})        φ = atan2(b_{1}, b_{2})        puncak pada t = φ/ω")
        self.para("Pengaruh gelombang tahunan diuji dengan uji F. Hipotesis nolnya H_{0}: b_{1} = b_{2} = 0 (tidak ada pola musiman) dan hipotesis alternatifnya H_{1}: paling sedikit satu dari $b_1$, $b_2$ tidak nol (ada pola musiman), pada taraf α = 0,05. Bentuk hipotesis yang sama dipakai untuk menguji ada atau tidaknya pola musiman pada curah hujan oleh Darmawan dkk. (2017) dan Purnama (2021), dan uji F dibaca dari keluaran regresi pada Excel oleh Azmi dkk. (2020). Darmawan dkk. (2017) memakai statistik F berderajat bebas (2, n − 3) untuk pasangan koefisien kosinus dan sinus.")
        self.h2("2.5", "Ukuran Kecocokan Model")
        self.para("Kecocokan model dinilai pada data yang dipakai menaksir koefisien, dengan koefisien determinasi (R^{2}) dan <i>Root Mean Square Error</i> (RMSE). "
                  "Model dengan R^{2} lebih besar dan RMSE lebih kecil dianggap lebih baik menggambarkan pola curah hujan (Kotarumalos dkk., 2025). "
                  "R^{2} juga dipakai memilih model deret Fourier curah hujan Kota Mataram oleh Astuti dkk. (2018), dan RMSE dipakai sebagai kriteria pemilihan model oleh Permata dkk. (2024).")
        self.eq("R^{2} = 1 − SSE/SST = 1 − Σ(Y_{t} − Ŷ_{t})^{2} / Σ(Y_{t} − Ȳ)^{2}        RMSE = √[ Σ(Y_{t} − Ŷ_{t})^{2} / n ]")
        self.para("dengan Y_{t} curah hujan aktual, Ŷ_{t} nilai duga model, Ȳ rata-rata curah hujan, dan n banyaknya data.")
        self.para("Kusdarwati (2023) juga menilai model dengan plot data curah hujan terhadap nilai duga model; pada data Kota Surabaya, model sudah menjangkau curah hujan rendah tetapi belum menjangkau curah hujan yang tinggi. "
                  "Plot yang sama dipakai dalam penelitian ini. Kedua ukuran di atas menilai kecocokan pada data 2020–2025. Akurasi ramalan 2026 belum dapat diukur karena data aktual 2026 belum tersedia.")
        self.h2("2.6", "Penelitian Terdahulu")
        self.para("Tabel 2.1 merangkum 15 penelitian terdahulu di Indonesia yang terbit tahun 2016–2026. Sebelas di antaranya membahas deret Fourier, regresi harmonik, atau analisis spektral curah hujan; tiga lainnya berlokasi di Kota Mataram dan NTB dengan metode non-harmonik; satu menjadi acuan pembagian musim dan kriteria RMSE. Dengan Astuti dkk. (2018) yang masuk kelompok Fourier, empat penelitian berlokasi di Kota Mataram atau NTB. Isi tabel diringkas dari abstrak masing-masing artikel; beberapa angka rincian data diambil dari isi artikel.")
        self.tab_caption("2.1", "Penelitian terdahulu")
        t = self.table(["No", "Peneliti (tahun)", "Data", "Metode", "Hasil"],
                       [[i + 1, a, b, c, e_] for i, (a, b, c, e_) in enumerate(TERDAHULU_H)],
                       [1.0, 3.1, 3.4, 3.2, 4.3], ["c", "l", "l", "l", "l"], size=9.5)
        for row in t.rows[1:]:
            for c in row.cells:
                for pp in c.paragraphs: pp.paragraph_format.keep_with_next = False
        self.para("Periode dominan sekitar 12 bulan dilaporkan di Subang, Jayapura, Bandung, Serdang Bedagai, dan tiga kota di Jawa Timur (Susilokarti dkk., 2016; Tulak dkk., 2022; Habinuddin dkk., 2019; Zega & Mardiningsih, 2025; Kusdarwati, 2023), dan komponen harmonik atau Fourier sudah dipakai pada curah hujan Indonesia, termasuk Kota Mataram dan Kota Ambon (Astuti dkk., 2018; Kusdarwati, 2023; Kotarumalos dkk., 2025). Sebagian besar studi peramalan memakai SARIMA atau model pembelajaran mesin. Dari tabel ini, dua penelitian menjadi dasar: Kusdarwati (2023) untuk alur pemodelan harmonik dan penilaian kesesuaian model, dan Astuti dkk. (2018) sebagai penelitian curah hujan Kota Mataram yang dilanjutkan dengan data lebih baru. Penelitian ini berbeda dalam tiga hal: data bulanan resmi BPS Kota Mataram selama enam tahun, regresi harmonik k = 1 dengan tiga parameter yang ditafsirkan melalui amplitudo dan fase, serta ramalan 12 bulan tahun 2026 dari model yang disusun dengan seluruh data.")
        self.h2("2.7", "Kerangka Pemikiran")
        self.para("Penelitian ini memakai satu variabel, yaitu curah hujan bulanan (univariat), yang dijelaskan oleh fungsi sinus dan kosinus dari waktu. Alurnya ditunjukkan pada Gambar 2.1: data 72 bulan dirangkum, variabel sinus dan kosinus dibentuk, koefisiennya ditaksir dengan OLS dari seluruh data dan diuji dengan uji F, kecocokan model dinilai dengan R^{2} dan RMSE, lalu model meramalkan 12 bulan tahun 2026.")
        self.figure("2.1", "Kerangka pemikiran penelitian (univariat)", None, w=14, path=KER,
                    sumber="Sumber: diadaptasi dari alur Kusdarwati (2023) dan Astuti dkk. (2018)")

        # ===== BAB III =====
        self.h1(None, multiline=("BAB III", "METODE PENELITIAN"))
        self.h2("3.1", "Jenis Penelitian")
        self.para("Penelitian kuantitatif dengan data sekunder deret waktu; analisisnya deskriptif (merangkum data) dan prediktif (memodelkan pola musiman dan meramalkan dengan regresi harmonik).")
        self.h2("3.2", "Lokasi dan Waktu Penelitian")
        self.para("Kota Mataram, Provinsi Nusa Tenggara Barat, data Januari 2020 sampai Desember 2025. Pengumpulan dan pengolahan data dilakukan pada Oktober sampai November 2026.")
        self.h2("3.3", "Metode Pengumpulan Data")
        self.para("Studi dokumen: kolom jumlah curah hujan (mm) pada Tabel 1.2.1 dibaca dari publikasi <i>Kota Mataram dalam Angka</i> edisi 2021 sampai 2026 (Badan Pusat Statistik Kota Mataram, 2021, 2022, 2023, 2024, 2025, 2026). "
                  "Satu edisi memuat satu tahun, sehingga edisi N berisi data tahun N−1 (Tabel 3.1; tangkapan halaman pada Lampiran A). "
                  "Data tidak diunduh dari portal data online BMKG karena unduhan dibatasi dua tahun per permintaan dan memerlukan akun.")
        self.tab_caption("3.1", "Sumber data tiap tahun")
        self.table(["Tahun data", "Publikasi", "Halaman PDF", "Stasiun pada judul tabel"],
                   [[th, f"Kota Mataram dalam Angka {ed}", hal, "tidak disebut" if ed == 2024 else "BMKG Lombok Barat"] for th, ed, hal in LAMPIRAN_A],
                   [2.2, 6.4, 2.6, 4.0], ["c", "l", "c", "l"])
        self.h2("3.4", "Populasi dan Sampel Penelitian")
        self.para("Populasi adalah seluruh curah hujan bulanan Kota Mataram sepanjang waktu. Sampel adalah curah hujan bulanan Januari 2020 sampai Desember 2025 (72 pengamatan), diambil seluruhnya karena semua bulan tersedia dan urutan waktu harus utuh.")
        self.h2("3.5", "Jenis dan Sumber Data")
        self.para("Data sekunder, kuantitatif, berskala rasio, dari publikasi resmi BPS Kota Mataram (data asal BMKG). "
                  "Rata-rata 12 bulan hasil hitungan tiap tahun dicocokkan dengan baris \"Kota Mataram\" pada tabel BPS (selisih 0,01 mm pada 2024 karena pembulatan: 150,725 pada hitungan, 150,73 pada tabel), "
                  "dan 72 nilai dicocokkan satu per satu dengan halaman PDF. Pemeriksaan ini mengurangi kemungkinan salah baca, tetapi tidak membuktikan bahwa angka BPS benar. Catatan atas data:", keep=True)
        self.lst(["Judul Tabel 1.2.1 edisi 2021, 2022, 2023, 2025, dan 2026 menyebut stasiun BMKG Lombok Barat; edisi 2024 tidak menyebut stasiun. Lokasi stasiun pengamatan tidak dapat dipastikan berada di dalam Kota Mataram.",
                  "Nilai 0,00 mm pada Juli 2021 dan Agustus 2023 tercetak bersama 6 hari hujan dan 1 hari hujan. Teks bahasa Inggris edisi 2024 menulis \"almost 0.00 mm\" untuk Agustus 2023, sehingga diduga hujan di bawah batas ukur tercatat 0; salah cetak belum bisa dikesampingkan. Angka tidak diubah.",
                  "Edisi 2026 mencatat rata-rata 2024 sebesar 166,82 mm (edisi 2025: 150,73 mm); data bulanan 2024 tetap dari edisi 2025 karena edisi 2026 tidak memuat rincian bulanannya.",
                  "Presisi angka berbeda antaredisi, dan angka tidak diverifikasi silang ke portal BMKG.",
                  "Nilai 672,5 mm pada Desember 2024 adalah nilai terbesar dan berada di atas batas pencilan 590,0 mm (kuartil ketiga ditambah 1,5 kali jangkauan antarkuartil). Nilai ini tetap dipakai. Model harmonik orde pertama tidak memodelkan pencilan, dan Kusdarwati (2023) mencatat bahwa pencilan yang sangat besar dapat membuat parameter sinus dan kosinus tidak nyata."], numbered=False)
        self.h2("3.6", "Teknik dan Alat Pengolahan Data")
        self.para("Berkas PDF diubah ke teks dengan <i>pdftotext</i>, lalu 12 nilai tiap edisi disalin ke satu berkas CSV (72 baris) dan dicek dengan rata-rata tahunan. "
                  "Statistik deskriptif dihitung di Microsoft Excel (Lampiran B); regresi harmonik dan uji F dihitung dengan Python 3 (pandas, SciPy, statsmodels, matplotlib).")
        self.h2("3.7", "Identifikasi dan Klasifikasi Variabel")
        self.para("Variabel terikat adalah curah hujan bulanan (Y_{t}), kuantitatif kontinu berskala rasio. Variabel bebasnya dibentuk dari waktu t, yaitu sin(2πt/12) dan cos(2πt/12).")
        self.para("Pola musiman curah hujan Indonesia digerakkan oleh monsun, yang membagi tahun menjadi musim hujan November sampai April dan kemarau Mei sampai Oktober (Kusdarwati, 2023; Tulak dkk., 2022; Permata dkk., 2024). Variabilitas antartahun curah hujan monsun Indonesia dipengaruhi pula oleh fenomena global seperti <i>El Niño-Southern Oscillation</i> (ENSO) (Kusdarwati, 2023; Aulia Putri dkk., 2026). Faktor itu tidak dimasukkan ke model.")
        self.h2("3.8", "Definisi Operasional Variabel")
        self.para("Curah hujan bulanan adalah jumlah curah hujan satu bulan kalender yang dicatat BMKG dan dimuat pada kolom \"Jumlah Curah Hujan\" Tabel 1.2.1 publikasi <i>Kota Mataram dalam Angka</i>, dalam milimeter (mm).")
        self.h2("3.9", "Teknik Analisis Data dan Uji Hipotesis")
        self.lst(["Mengelompokkan 72 data ke matriks tahun × bulan.",
                  "Menghitung mean, median, modus, dan simpangan baku sampel (n − 1), per tahun dan seluruh data.",
                  "Membentuk X_{1t} = sin(2πt/12) dan X_{2t} = cos(2πt/12) dengan t = 0 pada Januari 2020 sampai t = 71 pada Desember 2025, menaksir b_{0}, b_{1}, b_{2} dengan OLS dari seluruh 72 bulan data, lalu menguji pengaruh gelombang tahunan dengan uji F: H_{0}: b_{1} = b_{2} = 0 (tidak ada pola musiman) melawan H_{1}: paling sedikit satu dari b_{1}, b_{2} tidak nol (ada pola musiman), dengan α = 0,05 dan derajat bebas (2, 69).",
                  "Menilai kecocokan model dengan R^{2}, RMSE, dan plot data terhadap nilai duga, menghitung amplitudo dan fase, lalu meramal 12 bulan tahun 2026 (t = 72 sampai 83)."])
        self.para("Bentuk hipotesis pada langkah 3 mengikuti Darmawan dkk. (2017) dan Purnama (2021), dan uji F dari keluaran regresi mengikuti Azmi dkk. (2020). "
                  "Urutan langkah 3 dan 4 mengikuti Kusdarwati (2023), dan R^{2} serta RMSE sebagai ukuran kecocokan mengikuti Kotarumalos dkk. (2025).")

        # ===== DAFTAR PUSTAKA =====
        self.h1("DAFTAR PUSTAKA", "toc", brk=True)
        self.para("Catatan: tautan (DOI dan alamat halaman) pada daftar pustaka dapat diklik.", indent=False, size=11, after=8)
        for t in PUSTAKA_H:
            p = d.add_paragraph(); pf = p.paragraph_format
            pf.alignment, pf.left_indent, pf.first_line_indent, pf.line_spacing, pf.space_after = WD_ALIGN_PARAGRAPH.LEFT, Cm(1.25), Cm(-1.25), 1.0, Pt(5)
            self.runs_url(p, t, 11)

        # ===== LAMPIRAN =====
        self.h1("LAMPIRAN", "toc", brk=True)
        self.h2l("Lampiran A  Tangkapan Tabel 1.2.1 BPS Kota Mataram")
        self.para("Tangkapan halaman kolom jumlah curah hujan pada Tabel 1.2.1 tiap edisi. Baris Januari sampai Desember adalah data tahun yang dipakai; baris \"Kota Mataram\" adalah rata-rata 12 bulan.", indent=False)
        for i, (th, ed, hal) in enumerate(LAMPIRAN_A, 1):
            self.figure(f"A.{i}", f"Tabel 1.2.1 Kota Mataram dalam Angka {ed} (data {th}, halaman PDF {hal})", None, w=14,
                        path=LAMP / f"crop_bps{ed}.png", gaya="Keterangan Lampiran")
        self.h2l("Lampiran B  Tangkapan Lembar Kerja Excel")
        xl = sorted(LAMP.glob("harmonik_excel_*.png"))
        if xl:
            self.para("Tangkapan lembar kerja <i>Data_Curah_Hujan_Mataram_Bab3.xlsx</i> (dicetak dari Excel). Sel biru adalah angka dari publikasi BPS; sel lain berupa rumus Excel (AVERAGE, MEDIAN, MODE, STDEV, MIN, MAX, COUNT).", indent=False)
            from PIL import Image
            wmax = max(Image.open(x).width for x in xl)
            for i, img in enumerate(xl, 1):
                iw, ih = Image.open(img).size; w = min(14.0, 21.0 * iw / ih)  # lebar teks 14 cm (margin 4/3), tinggi maks 21 cm
                self.figure(f"B.{i}", XL_JUDUL[i - 1] if i <= len(XL_JUDUL) else f"Lembar kerja, bagian {i}", None, w=w, path=img, gaya="Keterangan Lampiran")
        else:
            self.para("[Tangkapan lembar kerja Excel menyusul.]", indent=False)
        return d



def jalan():
    gambar_kerangka_harmonik()
    b0 = Harmonik(); b0.build(); entries = b0.found
    pm = {}
    for k in range(5):
        b = Harmonik(entries, pm); b.build(); b.d.save(OUT_H)
        pm2, body = pagemap(render(OUT_H), entries)
        print(f"lintasan {k + 1}: entri {len(pm2)}, sama: {pm2 == pm}")
        if pm2 == pm: break
        pm = pm2
    print("tersimpan:", OUT_H.with_suffix(".pdf"), "| halaman PDF:", len(render(OUT_H)), "| Bab I di PDF hal", body + 1)


if __name__ == "__main__":
    jalan()
