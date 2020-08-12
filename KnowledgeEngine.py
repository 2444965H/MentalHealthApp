"""
- Inference machine: Here, Knowledge Base (Rules) and Facts are matched together
- From experta Documentation, Chapter 3, page 11: The class (KnowledgeEngine) is instantiated, populated with facts,
and then executed
- PLEASE NOTE: Within the Knowledge Engine, as long as there are more than 1 triggers firing, experta
does not care which rule is being executed first
- To shorten: DAS ≙ Depression, Anxiety, Stress
"""
import KnowledgeEngineGUI
from experta import *

#They DO NOT MAINTAIN AN INTERNAL ORDER OF ITEMS #From experta Documentation, Chapter 3, page 8
import MentalProfile
import Recommendations

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
    def financial_advice_1(self):
    #Couple Contextual Questions with PHQ-level information
        # Coupled with Depression/Anxiety/Stress lvl= from 5 to 10
        if maxIndValueOfDASFiveToNine:
            print(Recommendations.financial_advice_1)
        # Coupled with Depression/Anxiety/Stress lvl= from 10 to 15
        if maxIndValueOfDASTenToFourteen:
            print(Recommendations.financial_advice_cluster_1_2)
        # Coupled with Depression/Anxiety/Stress lvl= 15 or higher
        if maxIndValueOfDASFifteen:
            print(Recommendations.financial_advice_3)

    @Rule(FinancialFact(financialDistress='yes, I am in financial distress'),
          FinancialFact(employment='Part-Time'))
    def financial_advice_2(self):
        if maxIndValueOfDASFiveToNine:
            print(Recommendations.financial_advice_1)
        if maxIndValueOfDASTenToFourteen:
            print(Recommendations.financial_advice_cluster_1_2_4_5)
        if maxIndValueOfDASFifteen:
            print(Recommendations.financial_advice_cluster_3_4_5)

    @Rule(FinancialFact(financialDistress='yes, I am in financial distress'),
          FinancialFact(employment='On sabbatical - not working by choice'))
    def financial_advice_3a(self):
        if maxIndValueOfDASFiveToNine:
            print(Recommendations.financial_advice_1)
        if maxIndValueOfDASTenToFourteen:
            print(Recommendations.financial_advice_cluster_2_3_4_5)
        if maxIndValueOfDASFifteen:
            print(Recommendations.financial_advice_4 + Recommendations.financial_advice_5)

    @Rule(FinancialFact(financialDistress='yes, I am in financial distress'),
          FinancialFact(employment='Otherwise occupied')) #Could be a student or else
    def financial_advice_3b(self):
        if maxIndValueOfDASFiveToNine:
            print(Recommendations.financial_advice_1)
        if maxIndValueOfDASTenToFourteen:
            print(Recommendations.financial_advice_cluster_2_3_5)
        if maxIndValueOfDASFifteen:
            print(Recommendations.financial_advice_cluster_4_5)

    @Rule(FinancialFact(financialDistress='yes, I am in financial distress'),
          FinancialFact(employment='Job-seeking'))
    def financial_advice_4(self):
        if maxIndValueOfDASFiveToNine:
            print(Recommendations.financial_advice_cluster_1_6)
        if maxIndValueOfDASTenToFourteen:
            print(Recommendations.financial_advice_cluster_1_3_5_6)
        if maxIndValueOfDASFifteen:
            print(Recommendations.financial_advice_cluster_3_5_6)

#Family Questions
    @Rule(FamilyFact(isCaretaker='Yes, I am a caregiver'),
          FamilyFact(getsEnoughSupport='Yes, I have enough support'))
    # isCaretaker=Yes & getsEnoughSupport=Yes
    def family_advice_1(self):
        print(Recommendations.caregiver_advice_1)

    @Rule(FamilyFact(isCaretaker='Yes, I am a caregiver'),
          FamilyFact(getsEnoughSupport='No, I have not enough support'))
    # isCaretaker=Yes & getsEnoughSupport=No
    # will be triggered independently of who the user has to care for (adults, childrenU18, disabled children)
    def family_advice_2(self):
        if maxIndValueOfDAS >= 5: #always applicable, if there is any persisting burden
            print(Recommendations.caregiver_advice_cluster_1_2)

    @Rule(FamilyFact(isCaretaker='Yes, I am a caregiver'),
          FamilyFact(getsEnoughSupport='No, I have not enough support'),
          FamilyFact(caringForAdults='yes, I am a caregiver for an adult'))
    # isCaretaker=Yes & getsEnoughSupport=Yes & caringForAdults=Yes
    def family_advice_3(self):
        if maxIndValueOfDASFiveToNine:
            print(Recommendations.caregiver_advice_1 + " https://www.sonashomehealth.com/elderly-care-tips-caregivers/")
        if maxIndValueOfDASTenToFourteen:
            print(Recommendations.caregiver_advice_cluster_1_2 +
                  " https://www.sonashomehealth.com/elderly-care-tips-caregivers/")
        if maxIndValueOfDASFifteen:
            print(Recommendations.caregiver_advice_cluster_1_2_3 +
                  " https://www.sonashomehealth.com/elderly-care-tips-caregivers/")

    @Rule(FamilyFact(isCaretaker='Yes, I am a caregiver'),
          FamilyFact(getsEnoughSupport='No, I have not enough support'),
          FamilyFact(caringForDisabledChildren='yes, I am a caregiver for at least one disabled child'))
    # isCaretaker=Yes & getsEnoughSupport=Yes & caringForDisabledChildren=Yes
    def family_advice_4(self):
        if maxIndValueOfDASFiveToNine:
            print(Recommendations.caregiver_advice_1)
        if maxIndValueOfDASTenToFourteen:
            print(Recommendations.caregiver_advice_cluster_1_2)
        if maxIndValueOfDASFifteen:
            print(Recommendations.caregiver_advice_cluster_1_2_3_4)


    @Rule(FamilyFact(isCaretaker='Yes, I am a caregiver'),
          FamilyFact(getsEnoughSupport='No, I have not enough support'),
          FamilyFact(caringForChildren='yes, I am a caregiver for at least one child under 18'))
    # isCaretaker=Yes & getsEnoughSupport=Yes & caringForU18Children=Yes
    def family_advice_5(self):
        if maxIndValueOfDASFiveToNine:
            print(Recommendations.caregiver_advice_5)
        if maxIndValueOfDASTenToFourteen:
            print(Recommendations.caregiver_advice_cluster_2_5)
        if maxIndValueOfDASFifteen:
            print(Recommendations.caregiver_advice_cluster_1_2_3_4)

#Leisure Questions
    @Rule(LeisureFact(enoughTimeForOneself='no, I did not have enough leisure time for myself'),
          LeisureFact(leisureTimePlanned='no, I did/am not planning to take off time for leisure'))
    # enoughTimeForOneself=no & leisureTimePlanned=no
    def leisure_advice_1(self):
        print(Recommendations.leisure_advice_1) #To prevent any DAS level BEFORE they occur, trigger whenever Rule=true

    @Rule(LeisureFact(enoughTimeForOneself='no, I did not have enough leisure time for myself'),
          LeisureFact(leisureTimePlanned='yes, I planned/am planning to take off time for leisure'),
          LeisureFact(leisureTimePlannedExecuted='yes, I had leisure time like planned'))
    # enoughTimeForOneself=no & leisureTimePlanned=yes & leisureTimePlannedExecuted=yes
    def leisure_advice_2(self):
        if maxIndValueOfDASFiveToNine:
            print(Recommendations.leisure_advice_2)
        if maxIndValueOfDASTenToFourteen:
            print(Recommendations.leisure_advice_cluster_2_3)
        if maxIndValueOfDASFifteen:
            print(Recommendations.leisure_advice_4)

    @Rule(LeisureFact(enoughTimeForOneself='no, I did not have enough leisure time for myself'),
          LeisureFact(leisureTimePlanned='yes, I planned/am planning to take off time for leisure'),
          LeisureFact(leisureTimePlannedExecuted='no, I was not able to take leisure time like planned '))
    # enoughTimeForOneself=no & leisureTimePlanned=yes & leisureTimePlannedExecuted=no
    def leisure_advice_3(self):
        if maxIndValueOfDASFiveToNine:
            print(Recommendations.leisure_advice_3)
        if maxIndValueOfDASTenToFourteen:
            print(Recommendations.leisure_advice_cluster_3_4)
        if maxIndValueOfDASFifteen:
            print(Recommendations.leisure_advice_cluster_2_3_4)

#Social Questions: Only dependent on Stress Level, not depending on Depression or Anxiety Level
    #Question 1: Did you participate in any social activities?
    @Rule(SocialFact(anySocialActivities='no, I did not participate in any social activity'),
          SocialFact(missedOutDueExternalFactors='yes, I did miss social activities due to external factors'),
          SocialFact(alternativeMeeting='yes, we did seek out alternatives to meet'))
    # anySocialActivities=no & missedOutDueExternalFactors=yes & alternativeMeeting=yes
    def social_advice_1(self):
        if individualStressLevel >=5 and individualStressLevel <10:
            print()
        if individualStressLevel >=10 and individualStressLevel <15:
            print()
        if individualStressLevel >=15:
            print()

    @Rule(SocialFact(anySocialActivities='no, I did not participate in any social activity'),
          SocialFact(missedOutDueExternalFactors='yes, I did miss social activities due to external factors'),
          SocialFact(alternativeMeeting='no, we did not seek out alternatives to meet'))
    # anySocialActivities=no & missedOutDueExternalFactors=yes & alternativeMeeting=no
    def social_advice_2(self):
        if individualStressLevel >=5:
            print("Propose alternate ways to meet, e.g. video/phone call")

    @Rule(SocialFact(anySocialActivities='no, I did not participate in any social activity'),
          SocialFact(missedOutDueExternalFactors='no, I did not miss any social activities due to external factors'),
          SocialFact(stayedOut='yes, I cancelled/stayed out of social meetings'))
    # anySocialActivities=no & missedOutDueExternalFactors=no & stayedOut=yes
    def social_advice_3(self):
        if individualStressLevel >= 5:
            print("Though it may seem daunting in the beginning: Socializing is beneficial for your mental health.")

    @Rule(SocialFact(anySocialActivities='no, I did not participate in any social activity'),
          SocialFact(missedOutDueExternalFactors='no, I did not miss any social activities due to external factors'),
          SocialFact(stayedOut='no, I did not cancel/stayed out of social meetings'))
    # anySocialActivities=no & missedOutDueExternalFactors=no & stayedOut=no
    def social_advice_4(self):
        if individualStressLevel >=5:
            print("Socializing is beneficial for your mental health. Look if you can join friends or make new ones.")

    #Question 2: Did you have any negative  social exchanges?
    @Rule(SocialFact(negativeSocialExchanges='yes, I had negative social exchanges'),
          SocialFact(resolved='yes, I resolved the negative social exchange(s)'),
          SocialFact(futureStrategy='no, I do not have a strategy for negative social exchanges'))
    # negativeSocialExchanges=yes & resolved=yes & futureStrategy=no
    def social_advice_5(self):
        if individualStressLevel >=5:
            print()

    @Rule(SocialFact(negativeSocialExchanges='yes, I had negative social exchanges'),
          SocialFact(resolved='no, I did not resolve the negative social exchange(s)'),
          SocialFact(sensibleResolvePossible='yes, I can resolve this matter sensibly'))
    # negativeSocialExchanges=yes & resolved=no & sensibleResolvePossible=yes
    def social_advice_6(self):
        if individualStressLevel >=5:
            print()

    @Rule(SocialFact(negativeSocialExchanges='yes, I had negative social exchanges'),
          SocialFact(resolved='no, I did not resolve the negative social exchange(s)'),
          SocialFact(sensibleResolvePossible='no, I cannot resolve this matter sensibly'))
    # negativeSocialExchanges=yes & resolved=no & sensibleResolvePossible=no
    def social_advice_7(self):
        if individualStressLevel >=5:
            print()

#Printy Printy Stuff
AnswerArray = []  # Maybe substitue Array with ArrayList?
AnswerArray = KnowledgeEngineGUI.contextualQuestionsGUI()
print("Selected answers:")
for x in range(0, 10):  # NumberOfAnswersReturnedByGUI #declareAnswerArry[x+1]
    print("- " + AnswerArray[x])

engine = ContextualQuestions()
engine.reset()  # Prepare the engine for the execution.
#Declaring Financial Facts
engine.declare(FinancialFact(financialDistress=AnswerArray[0])) #GUIINPUT instead of hardcode
engine.declare(FinancialFact(employment=AnswerArray[1])) #GUIINPUT instead of hardcode
#Declaring Family Facts
engine.declare(FamilyFact(isCaretaker=AnswerArray[2])) #GUIINPUT instead of hardcode
engine.declare(FamilyFact(getsEnoughSupport=AnswerArray[3]))
engine.declare(FamilyFact(caringForAdults=AnswerArray[4]))
engine.declare(FamilyFact(caringForU18Children=AnswerArray[5]))
engine.declare(FamilyFact(caringForDisabledChildren=AnswerArray[6]))
#Declaring Leisure Facts
engine.declare(LeisureFact(enoughTimeForOneself=AnswerArray[7]))
engine.declare(LeisureFact(leisureTimePlanned=AnswerArray[8]))
engine.declare(LeisureFact(leisureTimePlannedExecuted=AnswerArray[9]))
#Declaring Social Facts
# engine.declare(SocialFact(anySocialActivities=AnswerArray[10]))
# engine.declare(SocialFact(missedOutDueExternalFactors=AnswerArray[11]))
# engine.declare(SocialFact(alternativeMeeting=AnswerArray[12]))
# engine.declare(SocialFact(stayedOut=AnswerArray[13]))
# engine.declare(SocialFact(negativeSocialExchanges=AnswerArray[14]))
# engine.declare(SocialFact(resolved=AnswerArray[15]))
# engine.declare(SocialFact(futureStrategy=AnswerArray[16]))
# engine.declare(SocialFact(sensibleResolvePossible=AnswerArray[17]))

engine.run()  # Executes & runs it