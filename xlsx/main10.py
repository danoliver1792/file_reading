from openpyxl import load_workbook
from openpyxl.styles import Font
from openpyxl.styles.colors import BLUE

wb = load_workbook("numeros.xlsx")
sheet_wb = wb["sheet1"]

font_title = Font(bold=True, size=12, color=BLUE)
font_tot = Font(bold=True, color=BLUE)

sheet_wb["B1"].font = font_title
sheet_wb["B8"].font = font_tot
sheet_wb["C8"].font = font_tot
sheet_wb["D8"].font = font_tot
sheet_wb["E8"].font = font_tot

wb.save("numeros.xlsx")
