import SeverityAlgorithm
from IRProcessor import NumericalDepressionArray, NumericalAnxietyArray, NumericalStressArray
import RecommendationAlgorithm
import os



#class ContextualCheck:
#    IndividualDepression = sum(NumericalDepressionArray.DepressionArray)
#    IndividualAnxiety = sum(NumericalAnxietyArray.AnxietyArray)
#    IndividualStress = sum(NumericalStressArray.StressArray)

def ContextualCheck():
    ContextArray = []
    if (sum(NumericalDepressionArray.DepressionArray) >=5) or (sum(NumericalAnxietyArray.AnxietyArray) >=5) or (sum(NumericalStressArray.StressArray) >=5):
        print("It seems that you have at least one thing on your mind. Do you want to select what contributes to your current mood? ")
        input = "yn"
        if os.system("choice /c:%s /n /m \"Yes or No (Y/N)\"" % input) - 2:
        # if pressed Y
            print("Yes")
            print("OK, great! Select at least 1 factor that contributes to your mood")
        input2 = "wf"
        if os.system("choice")
        else:
        # if pressed N
            print("No")


