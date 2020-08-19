#This file loads the input and then parses it into a class for the internal representation (IR)
#The classes are divided into subsections, each with its own IR array.
#Print statements (that are hashed out) can be unhashed in order to check for correct array (output)
#The classes' IR arrays are then processed in the next step in the IRProcessor.py


import ParserGUI

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

AnswerArrayPHQ = ParserGUI.PHQ_QuestionsGUI()
print("Selected answers:")
for x in range(0, 26):  # NumberOfAnswersReturnedByGUI #declareAnswerArry[x+1]
        print("- " + QuestionArray[x] + "  " + AnswerArrayPHQ[x])

# class DepressionIR:
#     DepressionArray = []
#     for x in range(0,9):
#         DepressionArray.append(AnswerArrayPHQ[x])
#     #print("Value of Depression Array: ")
#     #print(DepressionArray)
#     #print(len(DepressionArray)) #will print how many values in the array are
#
# class AnxietyIR:
#     AnxietyArray = []
#     for x in range(9,16):
#         AnxietyArray.append(AnswerArrayPHQ[x])
#     #print("Value of Anxiety Array: ")
#     #print(AnxietyArray)
#
# class StressIR:
#     StressArray = []
#     for x in range (16,26):
#         StressArray.append(AnswerArrayPHQ[x])
#     #print("Value of Stress Array: ")
#     #print(StressArray)