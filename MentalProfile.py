"""
Here, the information about the severity level of the depression, anxiety, and stress will come together and here,
the Inference Engine should be triggered, if the DAS-level reaches a trigger-point (>=5, respectively)
"""
import SeverityAlgorithm
#import KnowledgeEngine
#from TestKnowledgeEngine import ContextualQuestions
from IRProcessor import NumericalDepressionArray


class Profile:
    #IndividualContextualSituation = ContextualQuestionAlgorithm.ContextualCheck()
    individualDepressionLevel = SeverityAlgorithm.Depression()
    individualAnxietyLevel = SeverityAlgorithm.Anxiety()
    individualStressLevel = SeverityAlgorithm.Stress()

    IndividualDASArray = []
    IndividualDASArray = individualDepressionLevel, individualAnxietyLevel, individualStressLevel

    def triggerRecommendations(self):
        if (SeverityAlgorithm.sumOfDepression >=5) or (SeverityAlgorithm.sumOfAnxiety >=5) or (SeverityAlgorithm.sumOfStress >=5):
            print('hi')


testInstance = Profile()
print(Profile.IndividualDASArray)
# Profile().financial_advice()
