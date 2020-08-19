"""
The classes below are called by SeverityAlgorithm.py to process/save the parsed GUI user input from a String array to an
int array that can be summarized in SeverityAlgorithm.py to an int value that mirrors the respective DAS level in the
MentalProfile.py
-> Original values from the Parser.py are not changed
"""

class NumericalDepressionArray:
    def calculateDepression(self,depressionValueIR):
        #Overwrite DepressionArray from PHQContextParser.DepressionIR from string to int values
        #print("Depression Array:") #ONLY for UNBUGGING: when array is printed pint(DepressionArray[i]), then uncomment this for title
        DepressionArray = depressionValueIR #DepressionIR.DepressionArray #Duplication
        for i in range(len(DepressionArray)):
            if DepressionArray[i] == "Not at all":
                DepressionArray[i] = 0
            if DepressionArray[i] == "Several days":
                DepressionArray[i] = 1
            if DepressionArray[i] == "More than half the days":
                DepressionArray[i] = 2
            if DepressionArray[i] == "Nearly every day":
                DepressionArray[i] = 3
            #print(DepressionArray[i])
        print("Depression Array Values: ")
        print(DepressionArray)
        return DepressionArray

class NumericalAnxietyArray:
    def calculateAnxiety(self,anxietyValueIR):
        #Overwrite AnxietyArray from from PHQContextParser.AnxietyIR from string to int values
        #print("Anxiety Array:") #ONLY for UNBUGGING: when array is printed pint(AnxietyArray[i]), then uncomment this for title
        AnxietyArray = anxietyValueIR #AnxietyIR.AnxietyArray #Duplication
        for i in range(len(AnxietyArray)):
            if AnxietyArray[i] == "Not at all":
                AnxietyArray[i] = 0
            if AnxietyArray[i] == "Several days":
                AnxietyArray[i] = 1
            if AnxietyArray[i] == "More than half the days":
                AnxietyArray[i] = 2
            if AnxietyArray[i] == "Nearly every day":
                AnxietyArray[i] = 3
            #print(AnxietyArray[i])
        print("Anxiety Array Values: ")
        print(AnxietyArray)
        return AnxietyArray

class NumericalStressArray:
    def calculateStress(self,arg3):
        #Overwrite StressArray from  string to int values
        #print("Stress Array:") #ONLY for UNBUGGING: when array is printed pint(StressArray[i]), then uncomment this for title
        StressArray = arg3
        #Overwriting the Array of Stress Value with the Array of Stress IR
        for i in range(len(StressArray)):
            if StressArray[i] == "Not affected":
                StressArray[i] = 0
            if StressArray[i] == "Little affected":
                StressArray[i] = 1
            if StressArray[i] == "Severely affected":
                StressArray[i] = 2
            #print(StressArray[i])
        print("Stress Array Values: ")
        print(StressArray)
        return StressArray

# Question Array is used in PHQContextParser.py, when we want to see the corresponding answers to the questions below
QuestionArray = ["Little interest or pleasure in doing things?",
                 'Feeling down, depressed, or hopeless?',
                 'Trouble falling or staying asleep, or sleeping too much',
                 'Feeling tired or having little energy','Poor apppetite or overeating',
                 'Feeling bad about yourself - or that you are a failure or have let yourself or your family down',
                 'Trouble concentrating on things, such as reading the newspaper or watching television',
                 'Moving/Speaking so slowly OR being restless that others have noticed?',
                 'Thoughts that you would be better off dead or of hurting yourself in some way',
                 'Feeling nervous, anxious or on edge?',
                 'Not being able to stop or control worrying?',
                 'Worrying too much about different things?',
                 'Trouble relaxing?',
                 'Being so restless that it is hard to sit still?',
                 'Becoming easily annoyed or irritable?',
                 'Feeling afraid as if something awful might happen?',
                 'Worry about your health','Your weight or your appearance',
                 'Little or no sexual desire or pleasure during intercourse',
                 'Difficulties with the spouse, significant other, girlfriend / boyfriend',
                 'Burden of caring for children, parents, or other family members',
                 'Stress at work or at school',
                 'Financial problems or concerns',
                 'Not having someone to talk to about problems',
                 'Something bad that happened recently',
                 'Thoughts about terrible events from earlier or dreams about it']