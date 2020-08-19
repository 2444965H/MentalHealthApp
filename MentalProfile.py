"""
Here, the information about the severity level of the DAS will come together and here,
the Inference Engine should be triggered, if the DAS-level reaches a trigger-point (>=5, respectively)
"""
import SeverityAlgorithm

class Profile:
    def calculateProfile(self,depressionValueIR,anxietyValueIR,stressValueIR):
        #IndividualContextualSituation = ContextualQuestionAlgorithm.ContextualCheck()
        individualDepressionLevel = SeverityAlgorithm.Depression(depressionValueIR)
        individualAnxietyLevel = SeverityAlgorithm.Anxiety(anxietyValueIR)
        individualStressLevel = SeverityAlgorithm.Stress(stressValueIR)

        IndividualDASArray = []
        IndividualDASArray = individualDepressionLevel, individualAnxietyLevel, individualStressLevel
        print("IndividualDASArray")
        print(IndividualDASArray)
        return IndividualDASArray

    def calculateStressLevel(self,stressValueIR):
        individualStressLevel = SeverityAlgorithm.Stress(stressValueIR)
        return individualStressLevel

#testInstance = Profile()
#print(Profile.IndividualDASArray)
# Profile().financial_advice()
