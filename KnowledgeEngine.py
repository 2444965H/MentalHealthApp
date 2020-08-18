"""
- Inference machine: Here, Knowledge Base (Rules) and Facts are matched together
- From experta Documentation, Chapter 3, page 11: The class (KnowledgeEngine) is instantiated, populated with facts,
and then executed
- PLEASE NOTE: As long as there are more than 1 triggers firing, experta does not care which rule is being executed first
- Abbreviations: DAS ≙ Depression, Anxiety, Stress
"""

from experta import * #They DO NOT MAINTAIN AN INTERNAL ORDER OF ITEMS #From experta Documentation, Chapter 3, page 8
import MentalProfile
import RecommendationsCaregiver
import RecommendationsFinancial
import RecommendationsLeisure
import RecommendationsSocial


class FinancialFact(Fact):
    """Info about the financial situation: Sub-attributes are "financialDistress" and "employment"."""
    pass

class FamilyFact(Fact):
    """Info about the family situation: Sub-attributes are "financialDistress" and "employment"."""
    pass

class LeisureFact(Fact):
    """Info about the leisure situation: Sub-attributes are "" and ""."""
    pass

class SocialFact(Fact):
    """Info about the social situation: Sub-attributes are "" and ""."""
    pass

class DASLevel(Fact):
    """Info about the depression/anxiety/stress: Sub-attributes are "depression","anxiety", and "stress". """
    pass

#Variable declaration for highest, in other word "max", overall value of all DAS parameters of the indvidiual
maxIndValueOfDAS =  max(MentalProfile.Profile.IndividualDASArray)
maxIndValueOfDASFiveToNine = (maxIndValueOfDAS >=5 and maxIndValueOfDAS <10) #If the highest DAS value is from 5-9
maxIndValueOfDASTenToFourteen = (maxIndValueOfDAS >=10 and maxIndValueOfDAS<15) #If the highest DAS value is from 10-14
maxIndValueOfDASFifteen = (maxIndValueOfDAS >=15) #If the highest DAS value is 15 or higher

#Variable declaration for stress level
individualStressLevel = MentalProfile.Profile.individualStressLevel

#Knowledge Engine
class ContextualQuestions(KnowledgeEngine):
#Financial Questions
    @Rule(FinancialFact(financialDistress='Yes, I am in financial distress'),
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

    @Rule(FinancialFact(financialDistress='Yes, I am in financial distress'),
          FinancialFact(employment='Part-Time'))
    def financial_situation_2(self):
        if maxIndValueOfDASFiveToNine:
            print(RecommendationsFinancial.financial_advice_1)
        if maxIndValueOfDASTenToFourteen:
            print(RecommendationsFinancial.financial_advice_cluster_1_2_4_5)
        if maxIndValueOfDASFifteen:
            print(RecommendationsFinancial.financial_advice_cluster_3_4_5)

    @Rule(FinancialFact(financialDistress='Yes, I am in financial distress'),
          FinancialFact(employment='On sabbatical - not working by choice'))
    def financial_situation_3a(self):
        if maxIndValueOfDASFiveToNine:
            print(RecommendationsFinancial.financial_advice_1)
        if maxIndValueOfDASTenToFourteen:
            print(RecommendationsFinancial.financial_advice_cluster_2_3_4_5)
        if maxIndValueOfDASFifteen:
            print(RecommendationsFinancial.financial_advice_4 + RecommendationsFinancial.financial_advice_5)

    @Rule(FinancialFact(financialDistress='Yes, I am in financial distress'),
          FinancialFact(employment='Otherwise occupied')) #Could be a student or else
    def financial_situation_3b(self):
        if maxIndValueOfDASFiveToNine:
            print(RecommendationsFinancial.financial_advice_1)
        if maxIndValueOfDASTenToFourteen:
            print(RecommendationsFinancial.financial_advice_cluster_2_3_5)
        if maxIndValueOfDASFifteen:
            print(RecommendationsFinancial.financial_advice_cluster_4_5)

    @Rule(FinancialFact(financialDistress='Yes, I am in financial distress'),
          FinancialFact(employment='Job-seeking'))
    def financial_situation_4(self):
        if maxIndValueOfDASFiveToNine:
            print(RecommendationsFinancial.financial_advice_cluster_1_6)
        if maxIndValueOfDASTenToFourteen:
            print(RecommendationsFinancial.financial_advice_cluster_1_3_5_6)
        if maxIndValueOfDASFifteen:
            print(RecommendationsFinancial.financial_advice_cluster_3_5_6)

#Family Questions
    @Rule(FamilyFact(isCaretaker='Yes, I am a caregiver'),
          FamilyFact(getsEnoughSupport='Yes, I have enough support'))
    # isCaretaker=Yes & getsEnoughSupport=Yes
    def family_situation_1(self):
        print(RecommendationsCaregiver.caregiver_advice_1)

    # @Rule(FamilyFact(isCaretaker='Yes, I am a caregiver'),
    #       FamilyFact(getsEnoughSupport='No, I have not enough support'))
    # # isCaretaker=Yes & getsEnoughSupport=No
    # # will be triggered independently of who the user has to care for (adults, childrenU18, disabled children)
    # def family_situation_2(self):
    #     if maxIndValueOfDAS >= 5: #always applicable, if there is any persisting burden
    #         print(RecommendationsCaregiver.caregiver_advice_cluster_1_2)

    @Rule(FamilyFact(isCaretaker='Yes, I am a caregiver'),
          FamilyFact(getsEnoughSupport='No, I have not enough support'),
          FamilyFact(caringForAdults='Yes, I am a caregiver for an adult'))
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
          FamilyFact(caringForDisabledChildren='Yes, I am a caregiver for at least one disabled child'))
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
          FamilyFact(caringForChildren='Yes, I am a caregiver for at least one child under 18'))
    # isCaretaker=Yes & getsEnoughSupport=Yes & caringForU18Children=Yes
    def family_situation_5(self):
        if maxIndValueOfDASFiveToNine:
            print(RecommendationsCaregiver.caregiver_advice_5)
        if maxIndValueOfDASTenToFourteen:
            print(RecommendationsCaregiver.caregiver_advice_cluster_2_5)
        if maxIndValueOfDASFifteen:
            print(RecommendationsCaregiver.caregiver_advice_cluster_1_2_3_4)

#Leisure Questions
    @Rule(LeisureFact(enoughTimeForOneself='No, I did not have enough leisure time for myself'),
          LeisureFact(leisureTimePlanned='No, I did/am not planning to take off time for leisure'))
    # enoughTimeForOneself=no & leisureTimePlanned=no
    def leisure_situation_1(self):
        print(RecommendationsLeisure.leisure_advice_1) #To prevent any DAS level BEFORE they occur, trigger whenever Rule=true

    @Rule(LeisureFact(enoughTimeForOneself='No, I did not have enough leisure time for myself'),
          LeisureFact(leisureTimePlanned='Yes, I planned/am planning to take off time for leisure'),
          LeisureFact(leisureTimePlannedExecuted='Yes, I had leisure time like planned'))
    # enoughTimeForOneself=no & leisureTimePlanned=yes & leisureTimePlannedExecuted=yes
    def leisure_situation_2(self):
        if maxIndValueOfDASFiveToNine:
            print(RecommendationsLeisure.leisure_advice_2)
        if maxIndValueOfDASTenToFourteen:
            print(RecommendationsLeisure.leisure_advice_cluster_2_3)
        if maxIndValueOfDASFifteen:
            print(RecommendationsLeisure.leisure_advice_4)

    @Rule(LeisureFact(enoughTimeForOneself='No, I did not have enough leisure time for myself'),
          LeisureFact(leisureTimePlanned='Yes, I planned/am planning to take off time for leisure'),
          LeisureFact(leisureTimePlannedExecuted='No, I was not able to take leisure time like planned '))
    # enoughTimeForOneself=no & leisureTimePlanned=yes & leisureTimePlannedExecuted=no
    def leisure_situation_3(self):
        if maxIndValueOfDASFiveToNine:
            print(RecommendationsLeisure.leisure_advice_3)
        if maxIndValueOfDASTenToFourteen:
            print(RecommendationsLeisure.leisure_advice_cluster_3_4)
        if maxIndValueOfDASFifteen:
            print(RecommendationsLeisure.leisure_advice_cluster_2_3_4)

#Social Questions: Only dependent on Stress Level, not depending on Depression or Anxiety Level
    #Question 1: Did you participate in any social activities?
    @Rule(SocialFact(anySocialActivities='No, I did not participate in any social activity'),
          SocialFact(missedOutDueExternalFactors='Yes, I did miss social activities due to external factors'),
          SocialFact(alternativeMeeting='Yes, we did seek out alternatives to meet'))
    # anySocialActivities=no & missedOutDueExternalFactors=yes & alternativeMeeting=yes
    def social_situation_1(self):
        if individualStressLevel >=5:
            print(RecommendationsSocial.social_advice_1)

    @Rule(SocialFact(anySocialActivities='No, I did not participate in any social activity'),
          SocialFact(missedOutDueExternalFactors='Yes, I did miss social activities due to external factors'),
          SocialFact(alternativeMeeting='No, we did not seek out alternatives to meet'))
    # anySocialActivities=no & missedOutDueExternalFactors=yes & alternativeMeeting=no
    def social_situation_2(self):
        if individualStressLevel >=5:
            print(RecommendationsSocial.social_advice_2)

    @Rule(SocialFact(anySocialActivities='No, I did not participate in any social activity'),
          SocialFact(missedOutDueExternalFactors='No, I did not miss any social activities due to external factors'),
          SocialFact(stayedOut='Yes, I cancelled/stayed out of social meetings'))
    # anySocialActivities=no & missedOutDueExternalFactors=no & stayedOut=yes
    def social_situation_3(self):
        if individualStressLevel >=5 and individualStressLevel <10:
            print(RecommendationsSocial.social_advice_3)
        if individualStressLevel >=10 and individualStressLevel <15:
            print(RecommendationsSocial.social_advice_cluster_3_4)
        if individualStressLevel >=15:
            print(RecommendationsSocial.social_advice_cluster_3_4_5)

    @Rule(SocialFact(anySocialActivities='No, I did not participate in any social activity'),
          SocialFact(missedOutDueExternalFactors='No, I did not miss any social activities due to external factors'),
          SocialFact(stayedOut='No, I did not cancel/stayed out of social meetings'))
    # anySocialActivities=no & missedOutDueExternalFactors=no & stayedOut=no
    def social_situation_4(self):
        if individualStressLevel >=5:
            print(RecommendationsSocial.social_advice_cluster_3_6)

    #Question 2: Did you have any negative  social exchanges?
    @Rule(SocialFact(negativeSocialExchanges='Yes, I had negative social exchanges'),
          SocialFact(resolved='Yes, I resolved the negative social exchange(s)'),
          SocialFact(futureStrategy='No, I do not have a strategy for negative social exchanges'))
    # negativeSocialExchanges=yes & resolved=yes & futureStrategy=no
    def social_situation_5(self):
        if individualStressLevel >=5:
            print(RecommendationsSocial.social_advice_7)

    @Rule(SocialFact(negativeSocialExchanges='Yes, I had negative social exchanges'),
          SocialFact(resolved='No, I did not resolve the negative social exchange(s)'),
          SocialFact(sensibleResolvePossible='Yes, I can resolve this matter sensibly'))
    # negativeSocialExchanges=yes & resolved=no & sensibleResolvePossible=yes
    def social_situation_6(self):
        if individualStressLevel >=5:
            print(RecommendationsSocial.social_advice_8)

    @Rule(SocialFact(negativeSocialExchanges='Yes, I had negative social exchanges'),
          SocialFact(resolved='No, I did not resolve the negative social exchange(s)'),
          SocialFact(sensibleResolvePossible='No, I cannot resolve this matter sensibly'))
    # negativeSocialExchanges=yes & resolved=no & sensibleResolvePossible=no
    def social_situation_7(self):
        if individualStressLevel >=5:
            print(RecommendationsSocial.social_advice_9)