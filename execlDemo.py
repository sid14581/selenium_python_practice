import openpyxl

book = openpyxl.load_workbook("C:\\Users\\siddh\\OneDrive\\Desktop\\demoData.xlsx")
sheet = book.active
cell = sheet.cell(row=1, column=2)
print(cell.value)
sheet.cell(row=2, column=2).value = "Sid"
print(sheet.cell(row=2, column=2).value)

print(sheet.max_row)
print(sheet.max_column)

sheet['C3'].value = "harsh@gmail.com"
print(sheet['C3'].value)
book.save("C:\\Users\\siddh\\OneDrive\\Desktop\\demoData.xlsx")


