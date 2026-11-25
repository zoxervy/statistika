#!/usr/bin/env python3
"""Workbook Excel sampai Bab III: data curah hujan bulanan Kota Mataram 2020-2025 dan statistik deskriptif.
Dua sheet: Data (matriks, rata-rata, cek terhadap BPS, grafik) dan Ringkasan (mean, median, modus, simpangan baku, dll).
Tanpa regresi, ramalan, RMSE/MAE. Angka input biru, semua statistik berupa rumus aktif.
Jangan dijalankan jika tidak disuruh (vault: Aturan Kerja).
Jalankan: .venv/bin/python vault/Statistika-RegresiHarmonik/build/buat_xlsx.py
"""
from pathlib import Path

import pandas as pd
from openpyxl import Workbook
from openpyxl.chart import LineChart, Reference
from openpyxl.chart.label import DataLabelList
from openpyxl.styles import Alignment, Border, Font, PatternFill, Side
from openpyxl.utils import get_column_letter as L

ROOT = Path(__file__).resolve().parents[3]  # build/ -> vault folder -> vault -> statistika
OUT = ROOT / "hasil" / "Data_Curah_Hujan_Mataram_Bab3.xlsx"
df = pd.read_csv(ROOT / "data_mentah" / "curah_hujan_bulanan_bps_bmkg.csv")
mat = df.pivot(index="tahun", columns="bulan", values="curah_hujan_mm")
TAHUN = [int(t) for t in mat.index]
assert TAHUN == [2020, 2021, 2022, 2023, 2024, 2025] and mat.shape == (6, 12) and mat.notna().all().all()
BULAN = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
# rata-rata tahunan baris "Kota Mataram" pada Tabel 1.2.1 BPS (dibaca dari data_mentah/bps_pdf/dda2021-2026.txt)
BPS = {2020: 155.12, 2021: 182.18, 2022: 222.75, 2023: 136.58, 2024: 150.73, 2025: 201.42}
EDISI = {2020: 2021, 2021: 2022, 2022: 2023, 2023: 2024, 2024: 2025, 2025: 2026}

SLATE, GREY, PALE = "2F3E4E", "D9DEE3", "F2F4F6"
thin = Side(style="thin", color=GREY)
BOX = Border(left=thin, right=thin, top=thin, bottom=thin)
INPUT = Font(color="0000FF")
BOLD = Font(bold=True, color=SLATE)
TITLE = Font(bold=True, size=13, color=SLATE)
NOTE = Font(italic=True, size=9, color="5A6773")


def hdr(ws, row, col, labels):
    for i, t in enumerate(labels):
        c = ws.cell(row, col + i, t)
        c.font = Font(bold=True, color="FFFFFF"); c.fill = PatternFill("solid", fgColor=SLATE)
        c.alignment = Alignment(horizontal="center", vertical="center", wrap_text=True); c.border = BOX


def put(ws, ref, v, fmt=None, font=None, fill=None, align=None):
    c = ws[ref]; c.value = v; c.border = BOX
    if fmt: c.number_format = fmt
    if font: c.font = font
    if fill: c.fill = PatternFill("solid", fgColor=fill)
    if align: c.alignment = Alignment(horizontal=align)
    return c


def style_chart(ch, labels=False):
    s = ch.series[0]
    s.graphicalProperties.line.solidFill = SLATE; s.graphicalProperties.line.width = 22000; s.smooth = False
    if labels:
        ch.dataLabels = DataLabelList(); ch.dataLabels.showVal = True; ch.dataLabels.position = "t"
        for a in ("showSerName", "showCatName", "showLegendKey", "showPercent"): setattr(ch.dataLabels, a, False)
    ch.x_axis.delete = ch.y_axis.delete = False; ch.legend = None


wb = Workbook()

# ============================================================ 1. Data
ws = wb.active; ws.title = "Data"
ws["A1"] = "Curah hujan bulanan Kota Mataram 2020-2025 (mm)"; ws["A1"].font = TITLE
ws["A2"] = "Sumber: BPS Kota Mataram, Kota Mataram dalam Angka 2021-2026, Tabel 1.2.1 (data BMKG). Sel biru = angka dari publikasi."; ws["A2"].font = NOTE
hdr(ws, 4, 1, ["Tahun"] + BULAN + ["Rata-rata hitungan", "Rata-rata BPS", "Selisih"])
for i, t in enumerate(TAHUN):
    r = 5 + i
    put(ws, f"A{r}", t, font=INPUT, align="center")
    for b in range(1, 13):
        put(ws, f"{L(b + 1)}{r}", float(mat.loc[t, b]), "0.0", INPUT)
    put(ws, f"N{r}", f"=AVERAGE(B{r}:M{r})", "0.000", Font(bold=True), PALE, "right")
    put(ws, f"O{r}", BPS[t], "0.00", INPUT, None, "right")
    put(ws, f"P{r}", f"=ROUND(N{r}-O{r},3)+0", "0.000", align="right")
put(ws, "A11", "Rata-rata", font=BOLD, fill=PALE)
for b in range(1, 13):
    col = L(b + 1); put(ws, f"{col}11", f"=AVERAGE({col}5:{col}10)", "0.00", Font(bold=True), PALE)
ws["A12"] = "Rata-rata BPS = baris Kota Mataram pada tabel BPS. Selisih kecil (sampai 0,005 mm) berasal dari pembulatan BPS, misalnya 2024: 150,725 menjadi 150,73."; ws["A12"].font = NOTE
ws["A13"] = "Edisi sumber: " + "; ".join(f"{t} = edisi {EDISI[t]}" for t in TAHUN) + "."; ws["A13"].font = NOTE

ch = LineChart(); ch.title = "Rata-rata curah hujan per bulan (mm)"; ch.height, ch.width = 10, 36; ch.y_axis.scaling.max = 450; ch.y_axis.majorGridlines = None
ch.add_data(Reference(ws, min_col=2, max_col=13, min_row=11), from_rows=True, titles_from_data=False)
ch.set_categories(Reference(ws, min_col=2, max_col=13, min_row=4)); style_chart(ch, labels=True)
ch.y_axis.title = "mm"; ch.dataLabels.numFmt = "0.0"
ws.add_chart(ch, "A15")

# deret waktu 72 bulan (kolom bantu di sebelah kanan bawah grafik)
hdr(ws, 34, 1, ["No", "Tahun", "Bulan", "Curah hujan (mm)"])
for i in range(72):
    r = 35 + i; ty, bm = divmod(i, 12)
    put(ws, f"A{r}", i + 1, align="center")
    put(ws, f"B{r}", f"=A{5 + ty}", align="center")
    put(ws, f"C{r}", BULAN[bm])
    put(ws, f"D{r}", f"={L(bm + 2)}{5 + ty}", "0.0", align="right")
ch2 = LineChart(); ch2.title = "Curah hujan bulanan Jan 2020 - Des 2025 (mm)"; ch2.height, ch2.width = 9, 26; ch2.y_axis.majorGridlines = None
ch2.add_data(Reference(ws, min_col=4, min_row=34, max_row=106), titles_from_data=True)
ch2.set_categories(Reference(ws, min_col=1, min_row=35, max_row=106)); style_chart(ch2)
ch2.y_axis.title = "mm"; ch2.x_axis.title = "bulan ke-"; ch2.x_axis.tickLblSkip = 6; ch2.x_axis.tickMarkSkip = 6
ws.add_chart(ch2, "F34")

ws.column_dimensions["A"].width = 14
for c in range(2, 14): ws.column_dimensions[L(c)].width = 11
for c in (14, 15, 16): ws.column_dimensions[L(c)].width = 14
ws.freeze_panes = "B5"

# ============================================================ 2. Ringkasan
wr = wb.create_sheet("Ringkasan")
wr["A1"] = "Statistik deskriptif curah hujan bulanan Kota Mataram 2020-2025"; wr["A1"].font = TITLE
wr["A2"] = "Semua angka dihitung dengan rumus dari sheet Data. Simpangan baku memakai pembagi n-1 (sampel)."; wr["A2"].font = NOTE
hdr(wr, 4, 1, ["Ukuran"] + [str(t) for t in TAHUN] + ["2020-2025"])
UK = [("Mean", "AVERAGE({})", "0.00"), ("Median", "MEDIAN({})", "0.00"), ("Modus", 'IFERROR(MODE({}),"Tidak ada")', "0.00"),
      ("Simpangan baku (n-1)", "STDEV({})", "0.00"), ("Minimum", "MIN({})", "0.00"), ("Maksimum", "MAX({})", "0.00"), ("Jumlah data", "COUNT({})", "0")]
for k, (lab, f, fmt) in enumerate(UK):
    rr = 5 + k
    put(wr, f"A{rr}", lab, font=BOLD)
    for i in range(6):
        put(wr, f"{L(i + 2)}{rr}", "=" + f.format(f"Data!$B${5 + i}:$M${5 + i}"), fmt, align="right")
    put(wr, f"H{rr}", "=" + f.format("Data!$B$5:$M$10"), fmt, Font(bold=True), PALE, "right")
wr["A12"] = 'Modus "Tidak ada" = tidak ada nilai yang muncul lebih dari sekali dalam tahun itu.'; wr["A12"].font = NOTE

hdr(wr, 14, 1, ["Musim", "Bulan", "Rata-rata (mm)"])
put(wr, "A15", "Hujan", font=BOLD); put(wr, "B15", "November-April")
put(wr, "C15", "=AVERAGE(Data!B5:E10,Data!L5:M10)", "0.00", align="right")
put(wr, "A16", "Kemarau", font=BOLD); put(wr, "B16", "Mei-Oktober")
put(wr, "C16", "=AVERAGE(Data!F5:K10)", "0.00", align="right")

hdr(wr, 18, 1, ["Rata-rata per bulan", "Curah hujan (mm)"])
for b in range(12):
    put(wr, f"A{19 + b}", BULAN[b], font=BOLD)
    put(wr, f"B{19 + b}", f"=Data!{L(b + 2)}11", "0.00", align="right")

ch3 = LineChart(); ch3.title = "Simpangan baku per tahun (mm)"; ch3.height, ch3.width = 8, 15; ch3.y_axis.scaling.max = 250; ch3.y_axis.majorGridlines = None
ch3.add_data(Reference(wr, min_col=2, max_col=7, min_row=8), from_rows=True, titles_from_data=False)
ch3.set_categories(Reference(wr, min_col=2, max_col=7, min_row=4)); style_chart(ch3, labels=True)
ch3.dataLabels.numFmt = "0.0"; ch3.y_axis.title = "mm"
wr.add_chart(ch3, "E13")

# kotak ringkasan di paling bawah
r0 = 33
for col in ("A", "B", "C", "D", "E", "F", "G", "H"): wr[f"{col}{r0}"].fill = PatternFill("solid", fgColor=SLATE)
wr[f"A{r0}"] = "Ringkasan 72 data"; wr[f"A{r0}"].font = Font(bold=True, size=12, color="FFFFFF")
items = [("Jumlah data", "=H11", "0", "bulan (Januari 2020-Desember 2025)"),
         ("Mean", "=H5", "0.00", "mm"), ("Median", "=H6", "0.00", "mm"),
         ("Modus", "=H7", "0.00", "mm (0,0 muncul dua kali: Juli 2021 dan Agustus 2023)"),
         ("Simpangan baku", "=H8", "0.00", "mm, rumus sampel (n-1)"),
         ("Rata-rata musim hujan", "=C15", "0.00", "mm (November-April)"),
         ("Rata-rata musim kemarau", "=C16", "0.00", "mm (Mei-Oktober)"),
         ("Bulan terbasah (rata-rata)", "=INDEX(A19:A30,MATCH(MAX(B19:B30),B19:B30,0))", None, "=MAX(B19:B30)"),
         ("Bulan terkering (rata-rata)", "=INDEX(A19:A30,MATCH(MIN(B19:B30),B19:B30,0))", None, "=MIN(B19:B30)")]
for i, (lab, val, fmt, ket) in enumerate(items, start=1):
    r = r0 + i
    put(wr, f"A{r}", lab, font=BOLD, fill=PALE)
    put(wr, f"B{r}", val, fmt, Font(bold=True), PALE, "right")
    c = put(wr, f"C{r}", ket, font=Font(size=10, color="3A4652"), fill=PALE, align="left")
    if isinstance(ket, str) and ket.startswith("="): c.number_format = '0.00 "mm"'
    wr.merge_cells(f"C{r}:H{r}")
wr.column_dimensions["A"].width = 28
for c in range(2, 9): wr.column_dimensions[L(c)].width = 14
wr.column_dimensions["C"].width = 18

for sh in (ws, wr):  # cetak: landscape, muat satu halaman lebar
    sh.page_setup.orientation = "landscape"; sh.page_setup.fitToWidth = 1; sh.page_setup.fitToHeight = 0
    sh.sheet_properties.pageSetUpPr.fitToPage = True
ws.print_area = "A1:P106"; wr.print_area = "A1:L42"

OUT.parent.mkdir(exist_ok=True)
wb.save(OUT)
print("tersimpan:", OUT)
