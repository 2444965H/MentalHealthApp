from Parser import DepressionIR, AnxietyIR, StressIR

class DepressionValue:

    #Overwrite DepressionArray from DepressionIR from string to int values
    print("Depression Array:")
    #DepressionArray = []
    DepressionArray = DepressionIR.DepressionArray #Overwriting the Array of Depression Value with the Array of Depression IR
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

class AnxietyValue:
    #Overwrite AnxietyArray from string to int values
    print("Anxiety Array:")
    AnxietyArray = AnxietyIR.AnxietyArray #Overwriting the Array of Anxiety Value with the Array of Anxiety IR
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

class StressValue:
    #Overwrite StressArray from string to int values
    print("Stress Array:")
    StressArray = StressIR.StressArray #Overwriting the Array of Stress Value with the Array of Stress IR
    for i in range(len(StressArray)):
        if StressArray[i] == "Not affected":
            StressArray[i] = 0
        if StressArray[i] == "Little affected":
            StressArray[i] = 1
        if StressArray[i] == "Severely affected":
            StressArray[i] = 2
        print(StressArray[i])
