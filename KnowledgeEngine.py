"""
Inference machine: Here, Knowledge Base (Rules) and Facts are matched together
From experta Documentation, Chapter 3, page 11: The class (KnowledgeEngine) is instantiated, populated with facts,
and then executed
"""
import Gooey_GUI
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

class ContextualQuestions(KnowledgeEngine):
#Financial Questions
    @Rule(FinancialFact(financialDistress='yes, I am in financial distress'),
          FinancialFact(employment='Full-Time'))
    def financial_advice_1(self):
        if max(MentalProfile.Profile.IndividualDASArray) >=5 and max(MentalProfile.Profile.IndividualDASArray) <10: #Coupled with DAS lvl= from 5 to 10
            print(Recommendations.financial_advice_1)
        if max(MentalProfile.Profile.IndividualDASArray) >=10 and max(MentalProfile.Profile.IndividualDASArray)<15: # from 10 to 15
            print(Recommendations.financial_advice_1 + Recommendations.financial_advice_2)
        if max(MentalProfile.Profile.IndividualDASArray) >=15:
            print(Recommendations.financial_advice_3)

    # @Rule(FinancialFact(financialDistress='yes, I am in financial distress'),
    #       FinancialFact(employment='Full-Time'))
    # def financial_advice_10(self):
    #     print("Financial Advice 1)

    @Rule(FinancialFact(financialDistress='yes, I am in financial distress'),
          FinancialFact(employment='Part-Time'))
    def financial_advice_2(self):
        print("Financial Advice 2: Increase to full-time")

    @Rule(FinancialFact(financialDistress='yes, I am in financial distress'),
          FinancialFact(employment='On sabbatical - not working by choice'))
    def financial_advice_3a(self):
        print("Financial Advice 3a")

    @Rule(FinancialFact(financialDistress='yes, I am in financial distress'),
          FinancialFact(employment='Otherwise occupied'))
    def financial_advice_3b(self):
        print("Financial Advice 3b")

    @Rule(FinancialFact(financialDistress='yes, I am in financial distress'),
          FinancialFact(employment='Job-seeking'))
    def financial_advice_4(self):
        print("Financial Advice 4")

#Family Questions
    @Rule(FamilyFact(isCaretaker='Yes, I am a caregiver'),
          FamilyFact(getsEnoughSupport='Yes, I have enough support'))
    # isCaretaker=Yes & getsEnoughSupport=Yes
    def family_advice_0(self):
        print("Family Advice 0")

    @Rule(FamilyFact(isCaretaker='Yes, I am a caregiver'),
          FamilyFact(getsEnoughSupport='Yes, I have enough support'),
          FamilyFact(caringForAdults='yes, I am a caregiver for an adult'))
    # isCaretaker=Yes & getsEnoughSupport=Yes & caringForAdults=Yes
    def family_advice_1a(self):
        print("Family Advice 1a")

    @Rule(FamilyFact(isCaretaker='Yes, I am a caregiver'),
          FamilyFact(getsEnoughSupport='Yes, I have enough support'),
          FamilyFact(caringForDisabledChildren='yes, I am a caregiver for at least one disabled child'))
    # isCaretaker=Yes & getsEnoughSupport=Yes & caringForDisabledChildren=Yes
    def family_advice_1b(self):
        print("Family Advice 1b")

    @Rule(FamilyFact(isCaretaker='Yes, I am a caregiver'),
          FamilyFact(getsEnoughSupport='Yes, I have enough support'),
          FamilyFact(caringForChildren='yes, I am a caregiver for at least one child under 18'))
    # isCaretaker=Yes & getsEnoughSupport=Yes & caringForU18Children=Yes
    def family_advice_2(self):
        print("Family Advice 2")

    @Rule(FamilyFact(isCaretaker='Yes, I am a caregiver'),
          FamilyFact(getsEnoughSupport='No, I have not enough support'))
    # isCaretaker=Yes & getsEnoughSupport=No
    def family_advice_3(self):
        print("Family Advice 3")

#Leisure Questions
    @Rule(LeisureFact(enoughTimeForOneself='no, I did not have enough leisure time for myself'),
          LeisureFact(leisureTimePlanned='no, I did/am not planning to take off time for leisure'))
    # enoughTimeForOneself=no & leisureTimePlanned=no
    def leisure_advice_1(self):
        print("Leisure Advice 1")

    @Rule(LeisureFact(enoughTimeForOneself='no, I did not have enough leisure time for myself'),
          LeisureFact(leisureTimePlanned='yes, I planned/am planning to take off time for leisure'),
          LeisureFact(leisureTimePlannedExecuted='yes, I had leisure time like planned'))
    # enoughTimeForOneself=no & leisureTimePlanned=yes & leisureTimePlannedExecuted=yes
    def leisure_advice_2(self):
        print("Leisure Advice 2")

    @Rule(LeisureFact(enoughTimeForOneself='no, I did not have enough leisure time for myself'),
          LeisureFact(leisureTimePlanned='yes, I planned/am planning to take off time for leisure'),
          LeisureFact(leisureTimePlannedExecuted='no, I was not able to take leisure time like planned '))
    # enoughTimeForOneself=no & leisureTimePlanned=yes & leisureTimePlannedExecuted=no
    def leisure_advice_3(self):
        print("Leisure Advice 3")

#Social Questions
    #Question 1: Did you participate in any social activities?
    @Rule(SocialFact(anySocialActivities=''),
          SocialFact(missedOutDueExternalFactors='yes,  I did miss social activities due to external factors'),
          SocialFact(alternativeMeeting='yes, we did seek out alternatives to meet'))
    # anySocialActivities=no & missedOutDueExternalFactors=yes & alternativeMeeting=yes
    def social_advice_1(self):
        print("Social Advice 1")

    @Rule(SocialFact(anySocialActivities=''),
          SocialFact(missedOutDueExternalFactors='yes,  I did miss social activities due to external factors'),
          SocialFact(alternativeMeeting='no, we did not seek out alternatives to meet'))
    # anySocialActivities=no & missedOutDueExternalFactors=yes & alternativeMeeting=no
    def social_advice_2(self):
        print("Social Advice 2")

    @Rule(SocialFact(anySocialActivities=''),
          SocialFact(missedOutDueExternalFactors='no, I did not miss any social activities due to external factors'),
          SocialFact(stayedOut='yes, I cancelled/stayed out of social meetings'))
    # anySocialActivities=no & missedOutDueExternalFactors=no & stayedOut=yes
    def social_advice_3(self):
        print("Social Advice 3")

    @Rule(SocialFact(anySocialActivities=''),
          SocialFact(missedOutDueExternalFactors='no, I did not miss any social activities due to external factors'),
          SocialFact(stayedOut='no, I did not cancel/stayed out of social meetings'))
    # anySocialActivities=no & missedOutDueExternalFactors=no & stayedOut=no
    def social_advice_4(self):
        print("Social Advice 4")

    #Question 2: Did you have any negative  social exchanges?
    @Rule(SocialFact(negativeSocialExchanges='yes, I had negative social exchanges'),
          SocialFact(resolved='yes, I resolved the negative social exchange(s)'),
          SocialFact(futureStrategy='no, I do not have a strategy for negative social exchanges'))
    # negativeSocialExchanges=yes & resolved=yes & futureStrategy=no
    def social_advice_5(self):
        print("Social Advice 5")

    @Rule(SocialFact(negativeSocialExchanges='yes, I had negative social exchanges'),
          SocialFact(resolved='no, I did not resolve the negative social exchange(s)'),
          SocialFact(sensibleResolvePossible='yes, I can resolve this matter sensibly'))
    # negativeSocialExchanges=yes & resolved=no & sensibleResolvePossible=yes
    def social_advice_6(self):
        print("Social Advice 6")

    @Rule(SocialFact(negativeSocialExchanges='yes, I had negative social exchanges'),
          SocialFact(resolved='no, I did not resolve the negative social exchange(s)'),
          SocialFact(sensibleResolvePossible='no, I cannot resolve this matter sensibly'))
    # negativeSocialExchanges=yes & resolved=no & sensibleResolvePossible=no
    def social_advice_7(self):
        print("Social Advice 7")

#Printy Printy Stuff
AnswerArray = []  # Maybe substitue Array with ArrayList?
AnswerArray = Gooey_GUI.contextualQuestionsGUI()
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