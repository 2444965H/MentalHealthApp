import ContextualQuestionAlgorithm
import SeverityAlgorithm
import IRProcessor

class Profile:
    IndividualDepressionLevel = SeverityAlgorithm.Depression()
    IndividualAnxietyLevel = SeverityAlgorithm.Anxiety()
    IndividualStressLevel = SeverityAlgorithm.Stress()

    print(IndividualDepressionLevel, IndividualAnxietyLevel, IndividualStressLevel)
    IndividualContextualSituation = ContextualQuestionAlgorithm.ContextualCheck()


