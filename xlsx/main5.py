from openpyxl import load_workbook

# change cell contents
file_xlsx = "precos.xlsx"
wb = load_workbook(file_xlsx)

sheet_wb = wb["New cars 1"]
sheet_wb["A1"] = "Tabela de Precos 2023"

wb.save(file_xlsx)
