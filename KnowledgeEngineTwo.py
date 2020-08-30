"""
- KnowledgeEngine dedicated for comparing the current and last user input for changes and advising on that change
"""
from experta import *


class OldFinancialFact(Fact):
    """Info about the financial input given the last time the program was executed (taken from database)."""
    pass


class NewFinancialFact(Fact):
    """Info about the financial input given now."""
    pass


class OldFamilyFact(Fact):
    pass


class NewFamilyFact(Fact):
    pass


class OldLeisureFact(Fact):
    pass


class NewLeisureFact(Fact):
    pass


class OldSocialFact(Fact):
    pass


class NewSocialFact(Fact):
    pass


class DASLevelFact(Fact):
    """Passing values concerning DAS: higherThanBefore, LowerThanBefore, lowerStress, higherStress, higherDepression,
    lowerDepression, higherAnxiety, lowerAnxiety
    """
    pass


class ComparingOldInputWithNew(KnowledgeEngine):
    # Financial Comparison
    # If the user was in financial distress before, but now isn't
    @Rule(OldFinancialFact(financialDistress='Yes, I am in financial distress'),
          NewFinancialFact(financialDistress='No, I am not in financial distress'))
    def financial_change_1(self):
        print("Good to hear your financial situation improved!")

    # Family Comparison
    # If the user was not getting enough support as a caregiver before, but is now getting support
    @Rule(OldFamilyFact(isCaretaker='Yes, I am a caregiver'),
          NewFamilyFact(isCaretaker='Yes, I am a caregiver'),
          OldFamilyFact(getsEnoughSupport='No, I have not enough support'),
          NewFamilyFact(getsEnoughSupport='Yes, I have enough support'))
    def family_change_1(self):
        print("Good to hear that you feel like you're getting more support!")

    # Leisure Comparison
    # If the user did not have enough leisure time before, but now has
    @Rule(OldLeisureFact(enoughTimeForOneself='No, I did not have enough leisure time for myself'),
          NewLeisureFact(enoughTimeForOneself='Yes, I had enough leisure time for myself'))
    def leisure_change_1(self):
        print("Great that you have more leisure time for yourself now compared to the last time!")

    @Rule(OldLeisureFact(leisureTimePlanned='No, I did/am not planning to take off time for leisure'),
          NewLeisureFact(leisureTimePlanned='Yes, I planned/am planning to take off time for leisure'))
    def leisure_change_2(self):
        print("Good thinking ahead! Last time, you did not plan on taking time off. "
              "Plan to take time off regularly so you don't burn out!")

    # if the user has higher depression, anxiety, stress level and also had reduced leisure time
    @Rule(OldLeisureFact(enoughTimeForOneself='Yes, I had enough leisure time for myself'),
          NewLeisureFact(enoughTimeForOneself='No, I did not have enough leisure time for myself'),
          DASLevelFact(higherThanBefore='Yes'))
    def leisure_change_3(self):
        print("You seem to be in higher distress than last time! Since the last time, you reduced your leisure time. "
              "Maybe take some breaks again for your mental health!")

    # Social Comparison
    # If the user had a negative social exchange with no resolve, but now has a resolve
    @Rule(OldSocialFact(negativeSocialExchanges='Yes, I had negative social exchanges'),
          NewSocialFact(negativeSocialExchanges='Yes, I had negative social exchanges'),
          OldSocialFact(resolved='No, I did not resolve the negative social exchange(s)'),
          NewSocialFact(resolved='Yes, I resolved the negative social exchange(s)'))
    def social_change_1(self):
        print("How do feel after having resolved a negative social exchange?")

    @Rule(OldSocialFact(anySocialActivities='No, I did not participate in any social activity'),
          NewSocialFact(anySocialActivities='Yes, I participated in social activities'))
    def social_change_2(self):
        print("Good job putting yourself out there! Remember that humans need social contact, too!")

    @Rule(OldSocialFact(anySocialActivities='Yes, I participated in social activities'),
          NewSocialFact(anySocialActivities='No, I did not participate in any social activity'))
    def social_change_3(self):
        print("Good job putting yourself out there! Remember that humans need social contact, too!")

    @Rule(OldSocialFact(anySocialActivities='No, I did not participate in any social activity'),
          NewSocialFact(anySocialActivities='No, I did not participate in any social activity'))
    def social_change_4(self):
        print("Since last time, you still have not tried participating in any social activity. "
              "If you have social anxiety, find a close supportive friend/family member who you could talk to.")
