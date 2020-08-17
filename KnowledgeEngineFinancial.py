"""
- Inference machine: Here, Knowledge Base (Rules) and Facts are matched together
- From experta Documentation, Chapter 3, page 11: The class (KnowledgeEngine) is instantiated, populated with facts,
and then executed
- PLEASE NOTE: Within the Knowledge Engine, as long as there are more than 1 triggers firing, experta
does not care which rule is being executed first
#They DO NOT MAINTAIN AN INTERNAL ORDER OF ITEMS #From experta Documentation, Chapter 3, page 8
- To shorten: DAS ≙ Depression, Anxiety, Stress
"""
from experta import *
import MentalProfile
import RecommendationsFinancial


class FinancialFact(Fact):
    """Info about the financial situation: Sub-attributes are "financialDistress" and "employment"."""
    pass

class DASLevel(Fact):
    """Info about the depression/anxiety/stress: Sub-attributes are "depression","anxiety", and "stress". """
    pass

#Highest, in other word "max", overall value of all DAS parameters of the indvidiual
maxIndValueOfDAS =  max(MentalProfile.Profile.IndividualDASArray)
maxIndValueOfDASFiveToNine = (maxIndValueOfDAS >=5 and maxIndValueOfDAS <10) #If the highest DAS value is from 5-9
maxIndValueOfDASTenToFourteen = (maxIndValueOfDAS >=10 and maxIndValueOfDAS<15) #If the highest DAS value is from 10-14
maxIndValueOfDASFifteen = (maxIndValueOfDAS >=15) #If the highest DAS value is 15 or higher
individualStressLevel = MentalProfile.Profile.individualStressLevel

class ContextualQuestions(KnowledgeEngine):
#Financial Questions
    @Rule(FinancialFact(financialDistress='yes, I am in financial distress'),
          FinancialFact(employment='Full-Time'))
    def financial_situation_1(self):
    #Couple Contextual Questions with PHQ-level information
        # Coupled with Depression/Anxiety/Stress lvl= from 5 to 10
        if maxIndValueOfDASFiveToNine:
            print(RecommendationsFinancial.financial_advice_1)
        # Coupled with Depression/Anxiety/Stress lvl= from 10 to 15
        if maxIndValueOfDASTenToFourteen:
            print(RecommendationsFinancial.financial_advice_cluster_1_2)
        # Coupled with Depression/Anxiety/Stress lvl= 15 or higher
        if maxIndValueOfDASFifteen:
            print(RecommendationsFinancial.financial_advice_3)

    @Rule(FinancialFact(financialDistress='yes, I am in financial distress'),
          FinancialFact(employment='Part-Time'))
    def financial_situation_2(self):
        if maxIndValueOfDASFiveToNine:
            print(RecommendationsFinancial.financial_advice_1)
        if maxIndValueOfDASTenToFourteen:
            print(RecommendationsFinancial.financial_advice_cluster_1_2_4_5)
        if maxIndValueOfDASFifteen:
            print(RecommendationsFinancial.financial_advice_cluster_3_4_5)

    @Rule(FinancialFact(financialDistress='yes, I am in financial distress'),
          FinancialFact(employment='On sabbatical - not working by choice'))
    def financial_situation_3a(self):
        if maxIndValueOfDASFiveToNine:
            print(RecommendationsFinancial.financial_advice_1)
        if maxIndValueOfDASTenToFourteen:
            print(RecommendationsFinancial.financial_advice_cluster_2_3_4_5)
        if maxIndValueOfDASFifteen:
            print(RecommendationsFinancial.financial_advice_4 + RecommendationsFinancial.financial_advice_5)

    @Rule(FinancialFact(financialDistress='yes, I am in financial distress'),
          FinancialFact(employment='Otherwise occupied')) #Could be a student or else
    def financial_situation_3b(self):
        if maxIndValueOfDASFiveToNine:
            print(RecommendationsFinancial.financial_advice_1)
        if maxIndValueOfDASTenToFourteen:
            print(RecommendationsFinancial.financial_advice_cluster_2_3_5)
        if maxIndValueOfDASFifteen:
            print(RecommendationsFinancial.financial_advice_cluster_4_5)

    @Rule(FinancialFact(financialDistress='yes, I am in financial distress'),
          FinancialFact(employment='Job-seeking'))
    def financial_situation_4(self):
        if maxIndValueOfDASFiveToNine:
            print(RecommendationsFinancial.financial_advice_cluster_1_6)
        if maxIndValueOfDASTenToFourteen:
            print(RecommendationsFinancial.financial_advice_cluster_1_3_5_6)
        if maxIndValueOfDASFifteen:
            print(RecommendationsFinancial.financial_advice_cluster_3_5_6)