from Parser import DepressionIR, AnxietyIR, StressIR
from IRProcessor import DepressionValue, AnxietyValue, StressValue


def Depression():
    sumOfDepression = sum(DepressionValue.DepressionArray)
    print('Degree and Value of Depression is ',sumOfDepression)

def Anxiety():
    sumOfAnxiety = sum(AnxietyValue.AnxietyArray)
    print('Degree and Value of Anxiety is ',sumOfAnxiety)

def Stress():
    sumOfStress = sum(StressValue.StressArray)
    print('Degree and Value of Stress is ',sumOfStress)

Depression()
Anxiety()
Stress()
