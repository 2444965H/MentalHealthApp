from Parser import DepressionIR, AnxietyIR, StressIR


def Depression():
    sumOfDepression = sum(DepressionIR.DepressionArray)
    print('Degree and Value of Depression is ',sumOfDepression)

def Anxiety():
    sumOfAnxiety = sum(AnxietyIR.AnxietyArray)
    print('Degree and Value of Anxiety is ',sumOfAnxiety)

def Stress():
    sumOfStress = sum(Stress().StressArray)
    print('Degree and Value of Stress is ',sumOfStress)

Depression()
Anxiety()
Stress()
