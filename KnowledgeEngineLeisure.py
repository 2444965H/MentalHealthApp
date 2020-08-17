"""
- Inference machine: Here, Knowledge Base (Rules) and Facts are matched together
- From experta Documentation, Chapter 3, page 11: The class (KnowledgeEngine) is instantiated, populated with facts,
and then executed
- PLEASE NOTE: Within the Knowledge Engine, as long as there are more than 1 triggers firing, experta
does not care which rule is being executed first
#They DO NOT MAINTAIN AN INTERNAL ORDER OF ITEMS #From experta Documentation, Chapter 3, page 8
- To shorten: DAS ≙ Depression, Anxiety, Stress
"""
import KnowledgeEngineGUI
from experta import *
import MentalProfile
import RecommendationsLeisure

class LeisureFact(Fact):
    """Info about the leisure situation: Sub-attributes are "" and ""."""
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
#Leisure Questions
    @Rule(LeisureFact(enoughTimeForOneself='no, I did not have enough leisure time for myself'),
          LeisureFact(leisureTimePlanned='no, I did/am not planning to take off time for leisure'))
    # enoughTimeForOneself=no & leisureTimePlanned=no
    def leisure_situation_1(self):
        print(RecommendationsLeisure.leisure_advice_1) #To prevent any DAS level BEFORE they occur, trigger whenever Rule=true

    @Rule(LeisureFact(enoughTimeForOneself='no, I did not have enough leisure time for myself'),
          LeisureFact(leisureTimePlanned='yes, I planned/am planning to take off time for leisure'),
          LeisureFact(leisureTimePlannedExecuted='yes, I had leisure time like planned'))
    # enoughTimeForOneself=no & leisureTimePlanned=yes & leisureTimePlannedExecuted=yes
    def leisure_situation_2(self):
        if maxIndValueOfDASFiveToNine:
            print(RecommendationsLeisure.leisure_advice_2)
        if maxIndValueOfDASTenToFourteen:
            print(RecommendationsLeisure.leisure_advice_cluster_2_3)
        if maxIndValueOfDASFifteen:
            print(RecommendationsLeisure.leisure_advice_4)

    @Rule(LeisureFact(enoughTimeForOneself='no, I did not have enough leisure time for myself'),
          LeisureFact(leisureTimePlanned='yes, I planned/am planning to take off time for leisure'),
          LeisureFact(leisureTimePlannedExecuted='no, I was not able to take leisure time like planned '))
    # enoughTimeForOneself=no & leisureTimePlanned=yes & leisureTimePlannedExecuted=no
    def leisure_situation_3(self):
        if maxIndValueOfDASFiveToNine:
            print(RecommendationsLeisure.leisure_advice_3)
        if maxIndValueOfDASTenToFourteen:
            print(RecommendationsLeisure.leisure_advice_cluster_3_4)
        if maxIndValueOfDASFifteen:
            print(RecommendationsLeisure.leisure_advice_cluster_2_3_4)
