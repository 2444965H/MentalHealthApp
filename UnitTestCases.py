import unittest

import database
from IRProcessor import NumericalDepressionArray, NumericalAnxietyArray, NumericalStressArray
import MentalProfile
from SeverityAlgorithm import depression, anxiety, stress

# Unit testing to test all "basic" code in IRProcessor.py, SeverityAlgorithm.py, MentalProfile.py, and database.py
class Tests(unittest.TestCase):
    # Testing IRProcessor.py
    def test_depression_array_value_string_into_int(self):
        # for depression array: Does it convert the string values correctly to int?
        depression_array_one = []
        depression_array_one.append("Not at all")
        self.assertEqual([0], NumericalDepressionArray.calculateDepression(
            NumericalDepressionArray, depression_array_one))
        depression_array_two = []
        depression_array_two.append("Several days")
        self.assertEqual([1], NumericalDepressionArray.calculateDepression(
            NumericalDepressionArray, depression_array_two))
        depression_array_three = []
        depression_array_three.append("More than half the days")
        self.assertEqual([2], NumericalDepressionArray.calculateDepression(
            NumericalDepressionArray, depression_array_three))
        depression_array_four = []
        depression_array_four.append("Nearly every day")
        self.assertEqual([3], NumericalDepressionArray.calculateDepression(
            NumericalDepressionArray, depression_array_four))

    def test_anxiety_array_value_string_into_int(self):
        # for anxiety array
        anxiety_array_one = ["Not at all"]
        self.assertEqual([0], NumericalAnxietyArray.calculateAnxiety(NumericalAnxietyArray, anxiety_array_one))
        anxiety_array_two = ["Several days"]
        self.assertEqual([1], NumericalAnxietyArray.calculateAnxiety(NumericalAnxietyArray, anxiety_array_two))
        anxiety_array_three = ["More than half the days"]
        self.assertEqual([2], NumericalAnxietyArray.calculateAnxiety(NumericalAnxietyArray, anxiety_array_three))
        anxiety_array_four = ["Nearly every day"]
        self.assertEqual([3], NumericalAnxietyArray.calculateAnxiety(NumericalAnxietyArray, anxiety_array_four))

    def test_stress_array_value_string_into_int(self):
        # for stress array
        stress_array_one = ["Not affected"]
        self.assertEqual([0], NumericalStressArray.calculateStress(NumericalStressArray, stress_array_one))
        stress_array_two = ["Little affected"]
        self.assertEqual([1], NumericalStressArray.calculateStress(NumericalStressArray, stress_array_two))
        stress_array_three = ["Severely affected"]
        self.assertEqual([2], NumericalStressArray.calculateStress(NumericalStressArray, stress_array_three))

    def test_depression_array_conversion_string_into_int(self):
        depression_array_one = ["Not at all", "Nearly every day", "More than half the days", "Several days"]
        self.assertEqual([0, 3, 2, 1],
                         NumericalDepressionArray.calculateDepression(NumericalDepressionArray, depression_array_one))

    def test_anxiety_array_conversion_string_into_int(self):
        anxiety_array_one = ["Not at all", "Nearly every day", "More than half the days", "Several days"]
        self.assertEqual([0, 3, 2, 1], NumericalAnxietyArray.calculateAnxiety(NumericalAnxietyArray, anxiety_array_one))

    def test_stress_array_conversion_string_into_int(self):
        stress_array_one = ["Not affected", "Little affected", "Severely affected"]
        self.assertEqual([0, 1, 2], NumericalStressArray.calculateStress(NumericalStressArray, stress_array_one))

# SeverityAlgorithm.py : Is the sum of the array correct and is the array correct?
    def test_depression_summation(self):
        sum_of_depression = depression([1, 1, 0, 2])
        # is the sum correct?
        self.assertEqual(4, sum_of_depression[0])
        # is the array correct?
        self.assertEqual([1, 1, 0, 2], sum_of_depression[1])

    def test_anxiety_summation(self):
        sum_of_anxiety = anxiety([0, 2, 1, 1, 0, 2])
        self.assertEqual(6, sum_of_anxiety[0])
        self.assertEqual([0, 2, 1, 1, 0, 2], sum_of_anxiety[1])

    def test_stress_summation(self):
        sum_of_stress = stress([1, 2, 1, 1, 2])
        self.assertEqual(7, sum_of_stress[0])
        self.assertEqual([1, 2, 1, 1, 2], sum_of_stress[1])

# MentalProfile.py: test whether the values passed are then correctly processed as a DAS value
    def test_calculateDepressionLevel(self):
        depression_value = MentalProfile.Profile.calculateDepressionLevel(MentalProfile.Profile, [1, 2, 1, 1, 2])
        self.assertEqual(7, depression_value)

    def test_calculateAnxietyLevel(self):
        anxiety_value = MentalProfile.Profile.calculateAnxietyLevel(MentalProfile.Profile, [2, 2, 1, 1, 2])
        self.assertEqual(8, anxiety_value)

    def test_calculateStressLevel(self):
        stress_value = MentalProfile.Profile.calculateStressLevel(MentalProfile.Profile, [1, 2, 0, 1, 2])
        self.assertEqual(6, stress_value)

    def test_calculateProfile(self):
        das_array = MentalProfile.Profile.calculateProfile(MentalProfile.Profile, [1, 2, 1, 1, 2], [2, 2, 1, 1, 2], [1, 2, 0, 1, 2])
        self.assertEqual(7, das_array[0])
        self.assertEqual(8, das_array[1])
        self.assertEqual(6, das_array[2])

# database.py: checking whether the user under a certain username exists
    # test with user who does not exist
    def test_db_check_existence(self):
        username = database.check_existence("Anna")
        self.assertEqual(None, username)

    # # test with user who does exist
    # def test_db_check_existence(self):
    #     username = database.check_existence("Username")
    #     self.assertEqual("Username", username)

if __name__ == '__main__':
    unittest.main()
