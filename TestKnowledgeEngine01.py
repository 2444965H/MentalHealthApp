#Old Version - not working
import argparse
from argparse import ArgumentParser
from experta import *
from gooey import Gooey, GooeyParser
import Gooey_GUI
import SeverityAlgorithm
from Gooey_GUI import contextualQuestionsGUI

class FinancialQuestions(Fact):
    """Info about the FinancialDistressLevel."""
    pass

class Light(Fact):
    """Info about the traffic light."""
    pass


@Rule(
    Fact(action='DefineFinancialSituation'))
def shitty_advice_1(self):
    print("This is shitty advice")


@Rule(Light(color='red'))
def red_light(self):
    print("Don't walk")

class ContextualQuestions(KnowledgeEngine):
    @DefFacts()
    def _initial_action(self):
        if (SeverityAlgorithm.Depression() >= 5) or (SeverityAlgorithm.Anxiety() >= 5) or (
                SeverityAlgorithm.Stress() >= 5):
            yield Fact(action='DefineFinancialSituation')
            AnswerArray = [] #Maybe substitue Array with ArrayList?
            AnswerArray = Gooey_GUI.contextualQuestionsGUI()
            print("Selected answers:")
            for x in range(0, 3): #NumberOfAnswersReturnedByGUI
                print("- " + AnswerArray[x])
                yield Fact(financialDistress=AnswerArray[0])
            #First Conjunction Rule: If financial distress = yes AND employment = Full-Time, then print Advice 1
#            for x in range(0,1):
#                if AnswerArray[0] == "yes, I am in financial distress" and AnswerArray[1] == "Full-Time":
#                    print("Financial Advice 1: Develop a Personal Financial Strategy")
                @Rule(
                      Fact(action='DefineFinancialSituation'),
                      Fact(AnswerArray[0] == "yes, I am in financial distress"),
                      Fact(AnswerArray[1] =="Full-Time"))
                def financial_advice_1(self):
                    print("Financial Advice 1: Develop a Personal Financial Strategy")

                @Rule(FinancialQuestions(financialDistress='yes, I am in financial distress'))
                def shitty_advice_1(self):
                    print("This is shitty advice")

                # @Rule(Fact(action='DefineFinancialSituation'),
                #       Fact(financialdistress='yes'),
                #       Fact(employment='Full-Time'))
                # def financial_advice_1(self):
                #     print("Financial Advice 1: Develop a Personal Financial Strategy")

#Does the User suffer from financial distress?
    # @Rule(Fact(action='DefineFinancialSituation'),
    #       NOT(Fact(financialdistress=W())))
    # def ask_financialdistress(self):
    #     self.declare(Fact(financialdistress=input))

#What is the employment situation of the User?
    # @Rule(Fact(action='DefineFinancialSituation'),
    #       NOT(Fact(employment=W())))
    # def ask_employment(self):
    #     self.declare(Fact(employment=input))

engine = ContextualQuestions()
engine.reset()  # Prepare the engine for the execution.
engine.declare(FinancialQuestions(financialDistress='yes, I am in financial distress'))
engine.declare(Light(color='red'))
engine.run()  # Run it!
print("TestTest")
# @Rule(Fact(action='DefineFinancialSituation'),
#       Fact(financialdistress=TestGUIGooey.MATCH.financialdistress),
#       Fact(employment=TestGUIGooey.MATCH.employment))
# def greet(self, financialdistress, employment):
#     print("You are in financial distress: %s. Your employment status: %s" % (financialdistress, employment))

