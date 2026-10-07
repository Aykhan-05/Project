import os
from openpyxl import Workbook, load_workbook

workbook = load_workbook("anbar.xlsx")
sheet = workbook["Anbar_Idxal"]
print(sheet.title)
#print(workbook.sheetnames)
# sheet = workbook["Sheet1"]
# sheet.title = "Anbar_idxal"

sheet.append([
    "Mehsul adi",
    "Mehsul kodu",
    "Miqdar",
    "Vahid qiymet US",
    "Cemi USD",
    "Anbara daxil olma tarixi",
    "Idxal_tarixi",
    "Techizatchi",
    "Invoice/Proforma",
    "Gomruk beyenammesi",
    "Menshe olke",    
])

workbook.save("anbar.xlsx")