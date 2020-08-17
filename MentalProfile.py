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


#testInstance = Profile()
#print(Profile.IndividualDASArray)
# Profile().financial_advice()
