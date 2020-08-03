import argparse
from argparse import ArgumentParser
from experta import *
from gooey import Gooey, GooeyParser
import TestGUIGooey
import SeverityAlgorithm
from TestGUIGooey import guiMakerFinance

class ContextualQuestions(KnowledgeEngine):
    @DefFacts()
    def _initial_action(self):
        if (SeverityAlgorithm.Depression() >= 5) or (SeverityAlgorithm.Anxiety() >= 5) or (
                SeverityAlgorithm.Stress() >= 5):
            yield Fact(action="DefineFinancialSituation")
            teststring = TestGUIGooey.guiMakerFinance()
            print(teststring)

    @Rule(Fact(action='DefineFinancialSituation'),
          NOT(Fact(financialdistress=W())))
    def ask_financialdistress(self, financialdistress=None):
        #financialdistress=TestGUIGooey.guiMakerFinance()
        financialdistress= self.declare(Fact(financialdistress=input))
        #pass financialdistress

    @Rule(Fact(action='DefineFinancialSituation'),
          NOT(Fact(employment=W())))
    def ask_employment(self, employment=None):
        #employment=TestGUIGooey.guiMakerFinance()
        self.declare(Fact(employment=input))
        # self.declare(Fact(employment=input("What kind of employment do you have? Type in: Full-Time or Part-Time")))

    # @Rule(Fact(action='DefineFinancialSituation'),
    #       Fact(financialdistress=TestGUIGooey.MATCH.financialdistress),
    #       Fact(employment=TestGUIGooey.MATCH.employment))
    # def greet(self, financialdistress, employment):
    #     print("You are in financial distress: %s. Your employment status: %s" % (financialdistress, employment))

    # @Rule(Fact(action='DefineFinancialSituation'),
    #       Fact(financialdistress='yes'),
    #       Fact(employment='Full-Time'))
    # def financial_advice_1(self):
    #     print("Financial Advice 1: Develop a Personal Financial Strategy")


engine = ContextualQuestions()
engine.reset()  # Prepare the engine for the execution.
engine.run()  # Run it!