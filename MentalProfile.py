"""
Here, the information about the severity level of the DAS will come together and here,
the Inference Engine should be triggered, if the DAS-level reaches a trigger-point (>=5, respectively)
"""
import SeverityAlgorithm


class Profile:
    def calculateProfile(self, depressionValueIR, anxietyValueIR, stressValueIR):
        # IndividualContextualSituation = ContextualQuestionAlgorithm.ContextualCheck()
        individualDepressionLevel = SeverityAlgorithm.depression(depressionValueIR)
        individualAnxietyLevel = SeverityAlgorithm.anxiety(anxietyValueIR)
        individualStressLevel = SeverityAlgorithm.stress(stressValueIR)

        IndividualDASArray = []
        IndividualDASArray = individualDepressionLevel[0], individualAnxietyLevel[0], individualStressLevel[0]
        print("\n Individual's depression, anxiety, and stress value in that particular order: ")
        print(IndividualDASArray)
        return IndividualDASArray

    def calculateDepressionLevel(self, depressionValueIR):
        individualDepressionLevel = SeverityAlgorithm.depression(depressionValueIR)
        print("\n Depression Array")
        print(individualDepressionLevel[1])
        print("Depression Value")
        print(individualDepressionLevel[0])
        return individualDepressionLevel[0]

    def calculateAnxietyLevel(self, anxietyValueIR):
        individualAnxietyLevel = SeverityAlgorithm.anxiety(anxietyValueIR)
        print("Anxiety Array")
        print(individualAnxietyLevel[1])
        print("Anxiety Value")
        print(individualAnxietyLevel[0])
        return individualAnxietyLevel[0]

    def calculateStressLevel(self, stressValueIR):
        individualStressLevel = SeverityAlgorithm.stress(stressValueIR)
        print("Stress Array")
        print(individualStressLevel[1])
        print("Stress Value")
        print(individualStressLevel[0])
        return individualStressLevel[0]

def return_pqh_question():
    phq_question_array = ["Little interest or pleasure in doing things?",
                     'Feeling down, depressed, or hopeless?',
                     'Trouble falling or staying asleep, or sleeping too much',
                     'Feeling tired or having little energy', 'Poor appetite or overeating',
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
                     'Worry about your health', 'Your weight or your appearance',
                     'Little or no sexual desire or pleasure during intercourse',
                     'Difficulties with the spouse, significant other, girlfriend / boyfriend',
                     'Burden of caring for children, parents, or other family members',
                     'Stress at work or at school',
                     'Financial problems or concerns',
                     'Not having someone to talk to about problems',
                     'Something bad that happened recently',
                     'Thoughts about terrible events from earlier or dreams about it']
    return phq_question_array
