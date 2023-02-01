from openpyxl import load_workbook

# printing product descriptions
wb = load_workbook("precos.xlsx")
sheet_wb = wb["precos"]

for row in range(3, 13):
    desc = sheet_wb[f"B{row}"]
    print(desc.value)

for row in range(3, 13):
    qtd = 0
    x = sheet_wb[f"C{row}"].value
    qtd += x

    print(f"total amount: {qtd}")
