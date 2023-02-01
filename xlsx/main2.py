from openpyxl import load_workbook

# printing a cell range
wb = load_workbook("precos.xlsx")
sheet_wb = wb["precos"]

cells = sheet_wb["A3:D12"]

for c1, c2, c3, c4 in cells:
    print("{0:2} {1:90} {2:4} {3:10}".format(c1.value, c2.value, c3.value, c4.value))
    