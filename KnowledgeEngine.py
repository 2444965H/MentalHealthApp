import Gooey_GUI
from experta import *

class FinancialQuestions(Fact):
    """Info about the financial situation: Sub-attributes are "financialDistress" and "employment"."""
    pass

class FamilyQuestions(Fact):
    """Info about the family situation: Sub-attributes are "financialDistress" and "employment"."""
    pass

class LeisureQuestions(Fact):
    """Info about the leisure situation: Sub-attributes are "" and ""."""
    pass

class SocialQuestions(Fact):
    """Info about the social situation: Sub-attributes are "" and ""."""
    pass

class DASLevel(Fact):
    """Info about the depression/anxiety/stress: Sub-attributes are "depression","anxiety", and "stress". """
    pass

class ContextualQuestions(KnowledgeEngine):
#Financial Questions
    @Rule(FinancialQuestions(financialDistress='yes, I am in financial distress'), FinancialQuestions(employment='Full-Time'))
    def financial_advice_1(self):
        print("Financial Advice 1: Have a Financial Strategy")

    @Rule(FinancialQuestions(financialDistress='yes, I am in financial distress'), FinancialQuestions(employment='Full-Time'))
    def financial_advice_10(self):
        print("Financial Advice 1: Have a Financial Strategy")

    @Rule(FinancialQuestions(financialDistress='yes, I am in financial distress'), FinancialQuestions(employment='Part-Time'))
    def financial_advice_2(self):
        print("Financial Advice 2: Increase to full-time")

    @Rule(FinancialQuestions(financialDistress='yes, I am in financial distress'), FinancialQuestions(employment='On sabbatical - not working by choice'))
    def financial_advice_3a(self):
        print("Financial Advice 3a")

    @Rule(FinancialQuestions(financialDistress='yes, I am in financial distress'), FinancialQuestions(employment='Otherwise occupied'))
    def financial_advice_3b(self):
        print("Financial Advice 3b")

    @Rule(FinancialQuestions(financialDistress='yes, I am in financial distress'), FinancialQuestions(employment='Job-seeking'))
    def financial_advice_4(self):
        print("Financial Advice 4")

#Family Questions
    @Rule(FamilyQuestions(isCaretaker='Yes, I am a caregiver'), FamilyQuestions(getsEnoughSupport='Yes, I have enough support'))
    # isCaretaker=Yes & getsEnoughSupport=Yes
    def family_advice_0(self):
        print("Family Advice 0")

    @Rule(FamilyQuestions(isCaretaker='Yes, I am a caregiver'), FamilyQuestions(getsEnoughSupport='Yes, I have enough support'), FamilyQuestions(caringForAdults='yes, I am a caregiver for an adult'))
    # isCaretaker=Yes & getsEnoughSupport=Yes & caringForAdults=Yes
    def family_advice_1a(self):
        print("Family Advice 1a")

    @Rule(FamilyQuestions(isCaretaker='Yes, I am a caregiver'), FamilyQuestions(getsEnoughSupport='Yes, I have enough support'), FamilyQuestions(caringForDisabledChildren='yes, I am a caregiver for at least one disabled child'))
    # isCaretaker=Yes & getsEnoughSupport=Yes & caringForDisabledChildren=Yes
    def family_advice_1b(self):
        print("Family Advice 1b")

    @Rule(FamilyQuestions(isCaretaker='Yes, I am a caregiver'), FamilyQuestions(getsEnoughSupport='Yes, I have enough support'), FamilyQuestions(caringForChildren='yes, I am a caregiver for at least one child under 18'))
    # isCaretaker=Yes & getsEnoughSupport=Yes & caringForU18Children=Yes
    def family_advice_2(self):
        print("Family Advice 2")

    @Rule(FamilyQuestions(isCaretaker='Yes, I am a caregiver'), FamilyQuestions(getsEnoughSupport='No, I have not enough support'))
    # isCaretaker=Yes & getsEnoughSupport=No
    def family_advice_3(self):
        print("Family Advice 3")

#Leisure Questions
    @Rule(LeisureQuestions(enoughTimeForOneself='no, I did not have enough leisure time for myself'), LeisureQuestions(leisureTimePlanned='no, I did/am not planning to take off time for leisure'))
    # enoughTimeForOneself=no & leisureTimePlanned=no
    def leisure_advice_1(self):
        print("Leisure Advice 1")

    @Rule(LeisureQuestions(enoughTimeForOneself='no, I did not have enough leisure time for myself'), LeisureQuestions(leisureTimePlanned='yes, I planned/am planning to take off time for leisure'), LeisureQuestions(leisureTimePlannedExecuted='yes, I had leisure time like planned'))
    # enoughTimeForOneself=no & leisureTimePlanned=yes & leisureTimePlannedExecuted=yes
    def leisure_advice_2(self):
        print("Leisure Advice 2")

    @Rule(LeisureQuestions(enoughTimeForOneself='no, I did not have enough leisure time for myself'), LeisureQuestions(leisureTimePlanned='yes, I planned/am planning to take off time for leisure'), LeisureQuestions(leisureTimePlannedExecuted='no, I was not able to take leisure time like planned '))
    # enoughTimeForOneself=no & leisureTimePlanned=yes & leisureTimePlannedExecuted=no
    def leisure_advice_3(self):
        print("Leisure Advice 3")

#Social Questions
    #Question 1: Did you participate in any social activities?
    @Rule(SocialQuestions(anySocialActivities=''), SocialQuestions(missedOutDueExternalFactors='yes,  I did miss social activities due to external factors'), SocialQuestions(alternativeMeeting='yes, we did seek out alternatives to meet'))
    # anySocialActivities=no & missedOutDueExternalFactors=yes & alternativeMeeting=yes
    def social_advice_1(self):
        print("Social Advice 1")

    @Rule(SocialQuestions(anySocialActivities=''), SocialQuestions(missedOutDueExternalFactors='yes,  I did miss social activities due to external factors'), SocialQuestions(alternativeMeeting='no, we did not seek out alternatives to meet'))
    # anySocialActivities=no & missedOutDueExternalFactors=yes & alternativeMeeting=no
    def social_advice_2(self):
        print("Social Advice 2")

    @Rule(SocialQuestions(anySocialActivities=''), SocialQuestions(missedOutDueExternalFactors='no, I did not miss any social activities due to external factors'), SocialQuestions(stayedOut='yes, I cancelled/stayed out of social meetings'))
    # anySocialActivities=no & missedOutDueExternalFactors=no & stayedOut=yes
    def social_advice_3(self):
        print("Social Advice 3")

    @Rule(SocialQuestions(anySocialActivities=''), SocialQuestions(missedOutDueExternalFactors='no, I did not miss any social activities due to external factors'), SocialQuestions(stayedOut='no, I did not cancel/stayed out of social meetings'))
    # anySocialActivities=no & missedOutDueExternalFactors=no & stayedOut=no
    def social_advice_4(self):
        print("Social Advice 4")

    #Question 2: Did you have any negative  social exchanges?
    @Rule(SocialQuestions(negativeSocialExchanges='yes, I had negative social exchanges'), SocialQuestions(resolved='yes, I resolved the negative social exchange(s)'), SocialQuestions(futureStrategy='no, I do not have a strategy for negative social exchanges'))
    # negativeSocialExchanges=yes & resolved=yes & futureStrategy=no
    def social_advice_5(self):
        print("Leisure Advice 5")

    @Rule(SocialQuestions(negativeSocialExchanges='yes, I had negative social exchanges'), SocialQuestions(resolved='no, I did not resolve the negative social exchange(s)'), SocialQuestions(sensibleResolvePossible='yes, I can resolve this matter sensibly'))
    # negativeSocialExchanges=yes & resolved=no & sensibleResolvePossible=yes
    def social_advice_6(self):
        print("Leisure Advice 6")

    @Rule(SocialQuestions(negativeSocialExchanges='yes, I had negative social exchanges'), SocialQuestions(resolved='no, I did not resolve the negative social exchange(s)'), SocialQuestions(sensibleResolvePossible='no, I cannot resolve this matter sensibly'))
    # negativeSocialExchanges=yes & resolved=no & sensibleResolvePossible=no
    def social_advice_7(self):
        print("Leisure Advice 7")

#Printy Printy Stuff
AnswerArray = []  # Maybe substitue Array with ArrayList?
AnswerArray = Gooey_GUI.contextualQuestionsGUI()
print("Selected answers:")
for x in range(0, 7):  # NumberOfAnswersReturnedByGUI #declareAnswerArry[x+1]
    print("- " + AnswerArray[x])

engine = ContextualQuestions()
engine.reset()  # Prepare the engine for the execution.
#Declaring Financial Facts
engine.declare(FinancialQuestions(financialDistress=AnswerArray[0])) #GUIINPUT instead of hardcode
engine.declare(FinancialQuestions(employment=AnswerArray[1])) #GUIINPUT instead of hardcode
#Declaring Family Facts
engine.declare(FamilyQuestions(isCaretaker=AnswerArray[2])) #GUIINPUT instead of hardcode
engine.declare(FamilyQuestions(getsEnoughSupport=AnswerArray[3]))
engine.declare(FamilyQuestions(caringForAdults=AnswerArray[4]))
engine.declare(FamilyQuestions(caringForU18Children=AnswerArray[5]))
engine.declare(FamilyQuestions(caringForDisabledChildren=AnswerArray[6]))
#Declaring Leisure Facts
# engine.declare(LeisureQuestions(enoughTimeForOneself=AnswerArray[7]))
# engine.declare(LeisureQuestions(leisureTimePlanned=AnswerArray[8]))
# engine.declare(LeisureQuestions(leisureTimePlannedExecuted=AnswerArray[9]))
#Declaring Social Facts
# engine.declare(SocialQuestions(anySocialActivities=AnswerArray[10]))
# engine.declare(SocialQuestions(missedOutDueExternalFactors=AnswerArray[11]))
# engine.declare(SocialQuestions(alternativeMeeting=AnswerArray[12]))
# engine.declare(SocialQuestions(stayedOut=AnswerArray[13]))
# engine.declare(SocialQuestions(negativeSocialExchanges=AnswerArray[14]))
# engine.declare(SocialQuestions(resolved=AnswerArray[15]))
# engine.declare(SocialQuestions(futureStrategy=AnswerArray[16]))
# engine.declare(SocialQuestions(sensibleResolvePossible=AnswerArray[17]))
engine.run()  # Executes & runs it