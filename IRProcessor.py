#This file's Value classes takes the arrays from the Parser.py file and DUPLICATES them
# -> Original values from the Parser.py are not changed
#Next, the values from the new, duplicated array are replaced with numeric values (int)
#to make them more processable for the next algorithm which measures severity by summation

from Parser import DepressionIR, AnxietyIR, StressIR

class NumericalDepressionArray:
    #Overwrite DepressionArray from DepressionIR from string to int values
    #print("Depression Array:") #ONLY for UNBUGGING: when array is printed pint(DepressionArray[i]), then uncomment this for title
    DepressionArray = DepressionIR.DepressionArray #Duplication
    #Overwriting the Array of Depression Value with the Array of Depression IR
    for i in range(len(DepressionArray)):
        if DepressionArray[i] == "Not at all":
            DepressionArray[i] = 0
        if DepressionArray[i] == "Several days":
            DepressionArray[i] = 1
        if DepressionArray[i] == "More than half the days":
            DepressionArray[i] = 2
        if DepressionArray[i] == "Nearly every day":
            DepressionArray[i] = 3
 #       print(DepressionArray[i])

class NumericalAnxietyArray:
    #Overwrite AnxietyArray from string to int values
    #print("Anxiety Array:") #ONLY for UNBUGGING: when array is printed pint(AnxietyArray[i]), then uncomment this for title
    AnxietyArray = AnxietyIR.AnxietyArray #Duplication
    #Overwriting the Array of Anxiety Value with the Array of Anxiety IR
    for i in range(len(AnxietyArray)):
        if AnxietyArray[i] == "Not at all":
            AnxietyArray[i] = 0
        if AnxietyArray[i] == "Several days":
            AnxietyArray[i] = 1
        if AnxietyArray[i] == "More than half the days":
            AnxietyArray[i] = 2
        if AnxietyArray[i] == "Nearly every day":
            AnxietyArray[i] = 3
#        print(AnxietyArray[i])

class NumericalStressArray:
    #Overwrite StressArray from string to int values
    #print("Stress Array:") #ONLY for UNBUGGING: when array is printed pint(StressArray[i]), then uncomment this for title
    StressArray = StressIR.StressArray #Duplication
    #Overwriting the Array of Stress Value with the Array of Stress IR
    for i in range(len(StressArray)):
        if StressArray[i] == "Not affected":
            StressArray[i] = 0
        if StressArray[i] == "Little affected":
            StressArray[i] = 1
        if StressArray[i] == "Severely affected":
            StressArray[i] = 2
#        print(StressArray[i])
