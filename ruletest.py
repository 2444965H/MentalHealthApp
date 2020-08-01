from experta import *
#class Alert(Fact):
#    """The alert level."""
#    pass
#
#class Status(Fact):
#    """The system status."""
#    pass
#
#f1 = Alert('red')
#f2 = Status('critical')
#
#class MyFact(Fact)
#    pass

#@Rule(MyFact()) # This is the LHS(Left-Hand-Side) - the condition under which the rule fires
#def match_with_every_myfact():
#    """This rule will match with every instance of 'MyFact' ."""
#    #This is the RHS(Right-Hand-Side) - the action that should be taken, when the rule fires.
#    pass

#@Rule(Fact('animal', family = 'felinae'))
#def match_with_cats():
#    """
#    Match with every 'Fact' which:
#    f[0] == 'animal'
#    f['familiy'] == 'felinae'
#    """
#    print("Meow!")

#Financial Triggers
class FinancialDistress(Fact):
    """Yes or No"""
    pass

class Employment(Fact):
    """Full-time, Part-time, otherwiseOccupied, Job-seeking, Sabbatical"""
    pass

#Family Burden Triggers
class IsCaretaker(Fact):
    """Yes or No"""
    pass

class GetsEnoughSupport(Fact):
    """Yes or No"""
    pass

class CaringForAdults(Fact): #Caretaking of Adults, ChildrenUnder18, DisabledChildren is splitted to allow for multiple selections
    """Yes or No"""
    pass

class CaringForDisabledChildren(Fact):
    """Yes or No"""
    pass

class CaringForChildrenUnder18(Fact):
    """Yes or No"""
    pass

#Leisure Situation Trigger
class EnoughTimeForOneself(Fact):
    """Yes or No"""
    pass

class TakeOffTimePlanned(Fact):
    """Yes or No"""
    pass

class PlanExecuted(Fact):
    """Yes or No"""
    pass

#Social Situation Trigger
class AnySocialActivities(Fact):
    """Yes or No"""
    pass

class MissedOutExternalFactor(Fact):
    """Yes or No"""
    pass

class AlternateMeeting(Fact):
    """Yes or No"""
    pass

class StayOut(Fact):
    """Yes or No"""
    pass

class Resolved(Fact):
    """Yes or No"""
    pass

class FutureStrategy(Fact):
    """Yes or No"""
    pass

class SensibleResolvePossible(Fact):
    """Yes or No"""
    pass

#@Rule(MyFact()) # This is the LHS(Left-Hand-Side) - the condition under which the rule fires
#def match_with_every_myfact():
#    """This rule will match with every instance of 'MyFact' ."""
#    #This is the RHS(Right-Hand-Side) - the action that should be taken, when the rule fires.
#    pass

#@Rule(Fact('animal', family = 'felinae'))
#def match_with_cats():
#    """
#    Match with every 'Fact' which:
#    f[0] == 'animal'
#    f['familiy'] == 'felinae'
#    """
#    print("Meow!")

@Rule(
    AND
        (FinancialDistress('Yes'),Employment('Full-time')))
def give_advice():
    print("Meow!")

@Rule(Fact(FinancialDistress = 'Yes', Employment = 'Full-Time'))
def financial_advice_1():
    print("Develop a Financial Strategy")

@Rule(Fact(FinancialDistress = 'Yes', Employment = 'Part-Time'))
def financial_advice_2():
    print("Develop a Financial Strategy 2")

class ContextualQuestions():
    @DefFacts()
    def _initial_action(self):
        yield Fact(action="greet")
