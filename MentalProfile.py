"""
Here, the information about the severity level of the depression, anxiety, and stress will come together and here,
the Inference Engine should be triggered, if the DAS-level reaches a trigger-point (>=5, respectively)
"""
import Recommendations
import SeverityAlgorithm
#import KnowledgeEngine
#from TestKnowledgeEngine import ContextualQuestions
from IRProcessor import NumericalDepressionArray


class Profile:
    #IndividualContextualSituation = ContextualQuestionAlgorithm.ContextualCheck()
    IndividualDepressionLevel = SeverityAlgorithm.Depression()
    IndividualAnxietyLevel = SeverityAlgorithm.Anxiety()
    IndividualStressLevel = SeverityAlgorithm.Stress()

    IndividualDASArray = []
    IndividualDASArray = IndividualDepressionLevel, IndividualAnxietyLevel, IndividualStressLevel

    def triggerRecommendations(self):
        if (SeverityAlgorithm.sumOfDepression >=5) or (SeverityAlgorithm.sumOfAnxiety >=5) or (SeverityAlgorithm.sumOfStress >=5):
            print('hi')

    def financial_advice(self):
        if max(Profile.IndividualDASArray) >=5 \
                and max(Profile.IndividualDASArray) <10: #Couple it with DAS Mental Profile == from 5 to 10
            print(Recommendations.financial_advice_1)
        if max(Profile.IndividualDASArray) >=10 \
                and max(Profile.IndividualDASArray)<15: # from 10 to 15
            print(Recommendations.financial_advice_1 + Recommendations.financial_advice_2)
        if SeverityAlgorithm.Depression() >14:
            print(Recommendations.financial_advice_3)

# testInstance = Profile()
# print(Profile.IndividualDASArray)
# Profile().financial_advice()
