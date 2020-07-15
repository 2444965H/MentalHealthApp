from Parser import DepressionIR, AnxietyIR, StressIR
from IRProcessor import DepressionValue, AnxietyValue, StressValue

#Sum of values out of 9 questions - value range: 0-3
def Depression():
    sumOfDepression = sum(DepressionValue.DepressionArray)
    print('Degree and Value of Depression is ',sumOfDepression)
    if sumOfDepression <=4:
        print('minimal depressive symptomps')
    if (sumOfDepression >=5) and (sumOfDepression <=9):
        print('mildly depressive symptomps')
    if (sumOfDepression >=10) and (sumOfDepression <= 14):
        print('moderate depressive symptomps')
    if (sumOfDepression >=15) and (sumOfDepression <=27):
        print('severe depressive symptomps')
    else:
        print('Something went wrong')

#Sum of values out of 7 questions - value range: 0-3
def Anxiety():
    sumOfAnxiety = sum(AnxietyValue.AnxietyArray)
    print('Degree and Value of Anxiety is ',sumOfAnxiety)
    if sumOfAnxiety <=4:
        print('minimal anxiety symptomps')
    if (sumOfAnxiety >=5) and (sumOfAnxiety <=9):
        print('mildly anxiety symptomps')
    if (sumOfAnxiety >=10) and (sumOfAnxiety <= 14):
        print('moderate anxiety symptomps')
    if (sumOfAnxiety >=15) and (sumOfAnxiety <=21):
        print('severe anxiety symptomps')
    else:
        print('Something went wrong')

#Sum of values out of 10 questions - value range: 0-2
def Stress():
    sumOfStress = sum(StressValue.StressArray)
    print('Degree and Value of Stress is ',sumOfStress)
    if sumOfStress <=4:
        print('minimally distinct psychosocial stress factors')
    if (sumOfStress >=5) and (sumOfStress <=9):
        print('mildly distinct psychosocial stress factors')
    if (sumOfStress >=10) and (sumOfStress <= 14):
        print('moderate distinct psychosocial stress factors')
    if (sumOfStress >=15) and (sumOfStress <=20):
        print('severe distinct psychosocial stress factors')
    else:
        print('Something went wrong')

Depression()
Anxiety()
Stress()
