from openpyxl import load_workbook, workbook
#import openpyxl
#workbook = openpyxl.open_workbook('file.xlsx')
#worksheet = workbook.sheet_by_index(0)
#print(worksheet.cell(0, 0).value)
wb = load_workbook(filename ='Input.xlsx')
ws = wb['Day 1']
#Tab namens "test" - Klein/Großschreibung achten!

DepressionArray = []
for x in range(4,13):
    DepressionArray.append(ws.cell(row=x, column=2).value)
    print(ws.cell(row=x, column=2).value)
#print(len(DepressionArray))

AnxietyArray = []
for x in range(18,25):
    AnxietyArray.append(ws.cell(row=x, column=2).value)
    print(ws.cell(row=x, column=2).value)
#print(len(AnxietyArray))

StressArray = []
for x in range(29,39):
    StressArray.append(ws.cell(row=x, column=2).value)
    print(ws.cell(row=x, column=2).value)
#print(len(StressArray))

#Overwrite DepressionArray from string to int values
print("Depression Array:")
for i in range(len(DepressionArray)):
    if DepressionArray[i] == "Not at all":
        DepressionArray[i] = 0
    if DepressionArray[i] == "Several days":
        DepressionArray[i] = 1
    if DepressionArray[i] == "More than half the days":
        DepressionArray[i] = 2
    if DepressionArray[i] == "Nearly every day":
        DepressionArray[i] = 3
    print(DepressionArray[i])

#Overwrite AnxietyArray from string to int values
print("Anxiety Array:")
for i in range(len(AnxietyArray)):
    if AnxietyArray[i] == "Not at all":
        AnxietyArray[i] = 0
    if AnxietyArray[i] == "Several days":
        AnxietyArray[i] = 1
    if AnxietyArray[i] == "More than half the days":
        AnxietyArray[i] = 2
    if AnxietyArray[i] == "Nearly every day":
        AnxietyArray[i] = 3
    print(AnxietyArray[i])

#Overwrite StressArray from string to int values
print("Stress Array:")
for i in range(len(StressArray)):
    if StressArray[i] == "Not affected":
        StressArray[i] = 0
    if StressArray[i] == "Little affected":
        StressArray[i] = 1
    if StressArray[i] == "Severely affected":
        StressArray[i] = 2
    print(StressArray[i])