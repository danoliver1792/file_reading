from openpyxl import load_workbook

wb = load_workbook("precos.xlsx")

sheet_wb = wb["precos"]

sheet_wb.insert_rows(1)
sheet_wb.insert_cols(1)

wb.save("precos.xlsx")
