"""
Here, the information about the severity level of the depression, anxiety, and stress will come together and here,
the Inference Engine should be triggered, if the DAS-level reaches a trigger-point (>=5, respectively)
"""
import SeverityAlgorithm

class Profile:
    def calculateProfile(self,arg1,arg2,arg3):
        #IndividualContextualSituation = ContextualQuestionAlgorithm.ContextualCheck()
        individualDepressionLevel = SeverityAlgorithm.Depression(arg1)
        individualAnxietyLevel = SeverityAlgorithm.Anxiety(arg2)
        individualStressLevel = SeverityAlgorithm.Stress(arg3)

        IndividualDASArray = []
        IndividualDASArray = individualDepressionLevel, individualAnxietyLevel, individualStressLevel
        print("IndividualDASArray")
        print(IndividualDASArray)
        return IndividualDASArray

    def calculateStressLevel(self,arg3):
        individualStressLevel = SeverityAlgorithm.Stress(arg3)
        return individualStressLevel

#testInstance = Profile()
#print(Profile.IndividualDASArray)
# Profile().financial_advice()
