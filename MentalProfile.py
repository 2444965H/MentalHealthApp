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
        print("Individual's depression, anxiety, and stress value in that particular order: ")
        print(IndividualDASArray)
        return IndividualDASArray

    def calculateDepressionLevel(self, depressionValueIR):
        individualDepressionLevel = SeverityAlgorithm.depression(depressionValueIR)
        print("Depression Array")
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
