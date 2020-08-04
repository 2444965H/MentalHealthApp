import argparse
import Gooey_GUI
import SeverityAlgorithm
from argparse import ArgumentParser
from experta import *
from gooey import Gooey, GooeyParser
from Gooey_GUI import contextualQuestionsGUI

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
    @Rule(FinancialQuestions(financialDistress='yes, I am in financial distress'), FinancialQuestions(employment='Full-Time'))
    def financial_advice_1(self):
        print("Financial Advice 1: Have a Financial Strategy")

    @Rule(FinancialQuestions(financialDistress='yes, I am in financial distress'), FinancialQuestions(employment='Part-Time'))
    def financial_advice_2(self):
        print("Financial Advice 2: Increase to full-time")

AnswerArray = []  # Maybe substitue Array with ArrayList?
AnswerArray = Gooey_GUI.contextualQuestionsGUI()
print("Selected answers:")
for x in range(0, 3):  # NumberOfAnswersReturnedByGUI
    print("- " + AnswerArray[x])


engine = ContextualQuestions()
engine.reset()  # Prepare the engine for the execution.
engine.declare(FinancialQuestions(financialDistress='yes, I am in financial distress')) #GUIINPUT instead of hardcode
engine.declare(FinancialQuestions(employment='Full-Time')) #GUIINPUT instead of hardcode
engine.declare(FinancialQuestions(employment='Part-Time')) #GUIINPUT instead of hardcode
engine.run()  # Run it!