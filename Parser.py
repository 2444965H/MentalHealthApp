from numpy.random.tests import data
from openpyxl import load_workbook
import numpy as np
#import openpyxl
#workbook = openpyxl.open_workbook('file.xlsx')
#worksheet = workbook.sheet_by_index(0)
#print(worksheet.cell(0, 0).value)
wb = load_workbook(filename ='Input.xlsx')
ws = wb['Day 1']
#Tab namens "test" - Klein/Großschreibung achten!

class DepressionIR:
    DepressionArray = []
    for x in range(4,13):
        DepressionArray.append(ws.cell(row=x, column=2).value)
        #print(ws.cell(row=x, column=2).value)
    #print(len(DepressionArray))

class AnxietyIR:
    AnxietyArray = []
    for x in range(18,25):
        AnxietyArray.append(ws.cell(row=x, column=2).value)
        #print(ws.cell(row=x, column=2).value)
    #print(len(AnxietyArray))

class StressIR:
    StressArray = []
    for x in range(29,39):
        StressArray.append(ws.cell(row=x, column=2).value)
        #print(ws.cell(row=x, column=2).value)
    #print(len(StressArray))

