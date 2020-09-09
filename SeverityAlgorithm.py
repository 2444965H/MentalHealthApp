"""
- This file does not have classes, it has functions that can be used to derive new information from the data.
- It takes the values from the arrays created in IRProcessor.py and adds them up for each DAS respectively.
- These DAS values are needed for the MentalProfile.py
"""
from IRProcessor import NumericalDepressionArray, NumericalAnxietyArray, NumericalStressArray
import IRProcessor


# Sum of values out of 9 questions - value range for each question: 0-3
def depression(depression_value):
    # NumericalDepressionArray.calculateDepression(NumericalDepressionArray,arg1)
    depression_array = NumericalDepressionArray.calculateDepression(NumericalDepressionArray, depression_value)
    sum_of_depression = sum(NumericalDepressionArray.calculateDepression(NumericalDepressionArray, depression_value))
    # sum(NumericalDepressionArray.DepressionArray)
    # print("Depression Value: ") #uncomment this if you want to see the array of values saved for the depression value
    # print(sum_of_depression) #uncomment this if you want to see the array of values saved for the depression value
    # print('Degree and Value of Depression is ',sum_of_depression)
    if sum_of_depression <= 4:
        # print('minimal depressive symptoms')
        return sum_of_depression, depression_array
    if 5 <= sum_of_depression < 10:
        # equivalent to: if (sum_of_depression >= 5) and (sum_of_depression <= 9):
        # print('mildly depressive symptoms')
        return sum_of_depression, depression_array
    if 10 <= sum_of_depression < 15:
        # equivalent to: if (sum_of_depression >= 10) and (sum_of_depression <= 14):
        # print('moderate depressive symptoms')
        return sum_of_depression, depression_array
    if 15 <= sum_of_depression < 28:
        # equivalent to: if (sum_of_depression >= 15) and (sum_of_depression <= 27):
        # print('severe depressive symptoms')
        return sum_of_depression, depression_array
    else:
        print('Something went wrong')


# Sum of values out of 7 questions - value range for each question: 0-3
def anxiety(anxiety_value):
    anxiety_array = NumericalAnxietyArray.calculateAnxiety(NumericalAnxietyArray, anxiety_value)
    sum_of_anxiety = sum(NumericalAnxietyArray.calculateAnxiety(NumericalAnxietyArray, anxiety_value))
    #  #print('Degree and Value of Anxiety is ',sum_of_anxiety)
    # print("Anxiety Value: ") #uncomment this if you want to see the array of values saved for the anxiety value
    # print(sum_of_anxiety) #uncomment this if you want to see the array of values saved for the anxiety value
    if sum_of_anxiety <= 4:
        # print('minimal anxiety symptoms')
        return sum_of_anxiety, anxiety_array
    if 5 <= sum_of_anxiety < 10:
        # equivalent to: if (sum_of_anxiety >= 5) and (sum_of_anxiety <= 9):
        # print('mildly anxiety symptoms')
        return sum_of_anxiety, anxiety_array
    if 10 <= sum_of_anxiety < 15:
        # equivalent to: if (sum_of_anxiety >= 10) and (sum_of_anxiety <= 14):
        # print('moderate anxiety symptoms')
        return sum_of_anxiety, anxiety_array
    if 15 <= sum_of_anxiety < 22:
        # equivalent to: if (sum_of_anxiety >= 15) and (sum_of_anxiety <= 21):
        # print('severe anxiety symptoms')
        return sum_of_anxiety, anxiety_array
    else:
        print('Something went wrong')


# Sum of values out of 10 questions - value range for each question: 0-2
def stress(stress_value):
    stress_array = NumericalStressArray.calculateStress(NumericalStressArray, stress_value)
    sum_of_stress = sum(NumericalStressArray.calculateStress(NumericalStressArray, stress_value))
    # print('Degree and Value of Stress is ', sumOfStress)
    # print("Stress Value: ") #uncomment this if you want to see the array of values saved for the stress value
    # print(sum_of_stress) #uncomment this if you want to see the array of values saved for the stress value
    if sum_of_stress <= 4:
        # print('minimally distinct psychosocial stress factors')
        return sum_of_stress, stress_array
    if 5 <= sum_of_stress < 10:
        # equivalent to: if (sumOfStress >= 5) and (sumOfStress <= 9):
        # print('mildly distinct psychosocial stress factors')
        return sum_of_stress, stress_array
    if 10 <= sum_of_stress < 15:
        # equivalent to: if (sumOfStress >= 10) and (sumOfStress <= 14):
        # print('moderate distinct psychosocial stress factors')
        return sum_of_stress, stress_array
    if 15 <= sum_of_stress < 21:
        # equivalent to: if (sumOfStress >= 15) and (sumOfStress <= 20):
        # print('severe distinct psychosocial stress factors')
        return sum_of_stress, stress_array
    else:
        print('Something went wrong')
