#This file does not have classes, it has functions that can be used to derive new information from the data
#It takes the values from the IRProcessor.py and interprets them
#Thus creating a mental profile

from Parser import DepressionIR, AnxietyIR, StressIR
from IRProcessor import NumericalDepressionArray, NumericalAnxietyArray, NumericalStressArray

#Sum of values out of 9 questions - value range: 0-3
def Depression():
    sumOfDepression = sum(NumericalDepressionArray.DepressionArray)
    #print('Degree and Value of Depression is ',sumOfDepression)
    if sumOfDepression <=4:
        #print('minimal depressive symptomps')
        return sumOfDepression
    if (sumOfDepression >=5) and (sumOfDepression <=9):
        #print('mildly depressive symptomps')
        return sumOfDepression
    if (sumOfDepression >=10) and (sumOfDepression <= 14):
        #print('moderate depressive symptomps')
        return sumOfDepression
    if (sumOfDepression >=15) and (sumOfDepression <=27):
        #print('severe depressive symptomps')
        return sumOfDepression
    else:
        print('Something went wrong')

#Sum of values out of 7 questions - value range: 0-3
def Anxiety():
    sumOfAnxiety = sum(NumericalAnxietyArray.AnxietyArray)
    #print('Degree and Value of Anxiety is ',sumOfAnxiety)
    if sumOfAnxiety <=4:
        #print('minimal anxiety symptomps')
        return sumOfAnxiety
    if (sumOfAnxiety >=5) and (sumOfAnxiety <=9):
        #print('mildly anxiety symptomps')
        return sumOfAnxiety
    if (sumOfAnxiety >=10) and (sumOfAnxiety <= 14):
        #print('moderate anxiety symptomps')
        return sumOfAnxiety
    if (sumOfAnxiety >=15) and (sumOfAnxiety <=21):
        #print('severe anxiety symptomps')
        return sumOfAnxiety
    else:
        print('Something went wrong')

#Sum of values out of 10 questions - value range: 0-2
def Stress():
    sumOfStress = sum(NumericalStressArray.StressArray)
    #print('Degree and Value of Stress is ',sumOfStress)
    if sumOfStress <=4:
        #print('minimally distinct psychosocial stress factors')
        return sumOfStress
    if (sumOfStress >=5) and (sumOfStress <=9):
        #print('mildly distinct psychosocial stress factors')
        return sumOfStress
    if (sumOfStress >=10) and (sumOfStress <= 14):
        #print('moderate distinct psychosocial stress factors')
        return sumOfStress
    if (sumOfStress >=15) and (sumOfStress <=20):
        #print('severe distinct psychosocial stress factors')
        return sumOfStress
    else:
        print('Something went wrong')

