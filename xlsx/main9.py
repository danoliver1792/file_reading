from openpyxl import load_workbook

wb = load_workbook("numeros.xlsx")
sheet_wb = wb["sheet1"]

sheet_wb["B8"] = "=SOMA(B2:B7)"
sheet_wb["C8"] = "=SOMA(C2:C7)"
sheet_wb["D8"] = "=SOMA(D2:D7)"
sheet_wb["E8"] = "=SOMA(E2:E7)"

sheet_wb["F2"] = "=MÉDIA(B2:E2)"
sheet_wb["F3"] = "=MÉDIA(B3:E3)"
sheet_wb["F4"] = "=MÉDIA(B4:E4)"
sheet_wb["F5"] = "=MÉDIA(B5:E5)"
sheet_wb["F6"] = "=MÉDIA(B6:E6)"
sheet_wb["F7"] = "=MÉDIA(B7:E7)"

sheet_wb["G2"] = '=SE(F2>50,"LIKE","DESLIKE")'
sheet_wb["G3"] = '=SE(F3>50,"LIKE","DESLIKE")'
sheet_wb["G4"] = '=SE(F4>50,"LIKE","DESLIKE")'
sheet_wb["G5"] = '=SE(F5>50,"LIKE","DESLIKE")'
sheet_wb["G6"] = '=SE(F6>50,"LIKE","DESLIKE")'
sheet_wb["G7"] = '=SE(F7>50,"LIKE","DESLIKE")'

wb.save("numeros.xlsx")
