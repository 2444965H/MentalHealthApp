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
import RecommendationsCaregiver


class FamilyFact(Fact):
    """Info about the family situation: Sub-attributes are "financialDistress" and "employment"."""
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
#Family Questions
    @Rule(FamilyFact(isCaretaker='Yes, I am a caregiver'),
          FamilyFact(getsEnoughSupport='Yes, I have enough support'))
    # isCaretaker=Yes & getsEnoughSupport=Yes
    def family_situation_1(self):
        print(RecommendationsCaregiver.caregiver_advice_1)

    @Rule(FamilyFact(isCaretaker='Yes, I am a caregiver'),
          FamilyFact(getsEnoughSupport='No, I have not enough support'))
    # isCaretaker=Yes & getsEnoughSupport=No
    # will be triggered independently of who the user has to care for (adults, childrenU18, disabled children)
    def family_situation_2(self):
        if maxIndValueOfDAS >= 5: #always applicable, if there is any persisting burden
            print(RecommendationsCaregiver.caregiver_advice_cluster_1_2)

    @Rule(FamilyFact(isCaretaker='Yes, I am a caregiver'),
          FamilyFact(getsEnoughSupport='No, I have not enough support'),
          FamilyFact(caringForAdults='yes, I am a caregiver for an adult'))
    # isCaretaker=Yes & getsEnoughSupport=Yes & caringForAdults=Yes
    def family_situation_3(self):
        if maxIndValueOfDASFiveToNine:
            print(RecommendationsCaregiver.caregiver_advice_1 + " https://www.sonashomehealth.com/elderly-care-tips-caregivers/")
        if maxIndValueOfDASTenToFourteen:
            print(RecommendationsCaregiver.caregiver_advice_cluster_1_2 +
                  " https://www.sonashomehealth.com/elderly-care-tips-caregivers/")
        if maxIndValueOfDASFifteen:
            print(RecommendationsCaregiver.caregiver_advice_cluster_1_2_3 +
                  " https://www.sonashomehealth.com/elderly-care-tips-caregivers/")

    @Rule(FamilyFact(isCaretaker='Yes, I am a caregiver'),
          FamilyFact(getsEnoughSupport='No, I have not enough support'),
          FamilyFact(caringForDisabledChildren='yes, I am a caregiver for at least one disabled child'))
    # isCaretaker=Yes & getsEnoughSupport=Yes & caringForDisabledChildren=Yes
    def family_situation_4(self):
        if maxIndValueOfDASFiveToNine:
            print(RecommendationsCaregiver.caregiver_advice_1)
        if maxIndValueOfDASTenToFourteen:
            print(RecommendationsCaregiver.caregiver_advice_cluster_1_2)
        if maxIndValueOfDASFifteen:
            print(RecommendationsCaregiver.caregiver_advice_cluster_1_2_3_4)

    @Rule(FamilyFact(isCaretaker='Yes, I am a caregiver'),
          FamilyFact(getsEnoughSupport='No, I have not enough support'),
          FamilyFact(caringForChildren='yes, I am a caregiver for at least one child under 18'))
    # isCaretaker=Yes & getsEnoughSupport=Yes & caringForU18Children=Yes
    def family_situation_5(self):
        if maxIndValueOfDASFiveToNine:
            print(RecommendationsCaregiver.caregiver_advice_5)
        if maxIndValueOfDASTenToFourteen:
            print(RecommendationsCaregiver.caregiver_advice_cluster_2_5)
        if maxIndValueOfDASFifteen:
            print(RecommendationsCaregiver.caregiver_advice_cluster_1_2_3_4)