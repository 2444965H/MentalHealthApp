import SeverityAlgorithm
import IRProcessor
#from TestKnowledgeEngine import ContextualQuestions


class Profile:
    #IndividualContextualSituation = ContextualQuestionAlgorithm.ContextualCheck()
    def ConfiguringProfile(self):
        IndividualDepressionLevel = SeverityAlgorithm.Depression()
        IndividualAnxietyLevel = SeverityAlgorithm.Anxiety()
        IndividualStressLevel = SeverityAlgorithm.Stress()
        print(IndividualDepressionLevel, IndividualAnxietyLevel, IndividualStressLevel)

    def TriggerRecommendations(self):
        if (SeverityAlgorithm.sumOfDepression >=5) or (SeverityAlgorithm.sumOfAnxiety >=5) or (SeverityAlgorithm.sumOfStress >=5):
            print('hi')

