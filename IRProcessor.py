"""
The classes below are called by SeverityAlgorithm.py to process/save the parsed GUI user input from a String array to an
int array that can be summarized in SeverityAlgorithm.py to an int value that mirrors the respective DAS level in the
MentalProfile.py
-> Original values are not changed

For Debugging: QuestionArray can be uncommented in Parser.py to see the PHQ-Questions and respective answers
"""


class NumericalDepressionArray:
    def calculateDepression(self, depressionValueIR):
        # Overwrite DepressionArray from Parser.DepressionIR from string to int values
        DepressionArray = depressionValueIR  # DepressionIR.DepressionArray
        for i in range(len(DepressionArray)):
            if DepressionArray[i] == "Not at all":
                DepressionArray[i] = 0
            if DepressionArray[i] == "Several days":
                DepressionArray[i] = 1
            if DepressionArray[i] == "More than half the days":
                DepressionArray[i] = 2
            if DepressionArray[i] == "Nearly every day":
                DepressionArray[i] = 3
        #print("Depression Array Values: ")
        #print(DepressionArray)
        return DepressionArray


class NumericalAnxietyArray:
    def calculateAnxiety(self, anxietyValueIR):
        # Overwrite AnxietyArray from Parser.AnxietyIR from string to int values
        AnxietyArray = anxietyValueIR  # AnxietyIR.AnxietyArray
        for i in range(len(AnxietyArray)):
            if AnxietyArray[i] == "Not at all":
                AnxietyArray[i] = 0
            if AnxietyArray[i] == "Several days":
                AnxietyArray[i] = 1
            if AnxietyArray[i] == "More than half the days":
                AnxietyArray[i] = 2
            if AnxietyArray[i] == "Nearly every day":
                AnxietyArray[i] = 3
        #print("Anxiety Array Values: ")
        #print(AnxietyArray)
        return AnxietyArray


class NumericalStressArray:
    def calculateStress(self, stressValueIR):
        # Overwrite StressArray from Parser.StressIR string to int values
        StressArray = stressValueIR
        for i in range(len(StressArray)):
            if StressArray[i] == "Not affected":
                StressArray[i] = 0
            if StressArray[i] == "Little affected":
                StressArray[i] = 1
            if StressArray[i] == "Severely affected":
                StressArray[i] = 2
        #print("Stress Array Values: ")
        #print(StressArray)
        return StressArray
