from experta import *

class ContextualQuestions(KnowledgeEngine):
    @DefFacts()
    def _initial_action(self):
        yield Fact(action="DefineFinancialSituation")

    @Rule(Fact(action='DefineFinancialSituation'),
          NOT(Fact(financialdistress=W())))
    def ask_financialdistress(self):
        self.declare(Fact(financialdistress=input("Are you in financial distress?")))

    @Rule(Fact(action='DefineFinancialSituation'),
          NOT(Fact(employment=W())))
    def ask_employment(self):
        self.declare(Fact(employment=input("What kind of employment do you have? Type in: Full-Time or Part-Time")))

    @Rule(Fact(action='DefineFinancialSituation'),
          Fact(financialdistress=MATCH.financialdistress),
          Fact(employment=MATCH.employment))
    def greet(self, financialdistress, employment):
        print("You are in financial distress: %s. Your employment status: %s" % (financialdistress, employment))

    @Rule(Fact(action='DefineFinancialSituation'),
          Fact(financialdistress='yes'),
          Fact(employment='Full-Time'))
    def financial_advice_1(self):
        print("Financial Advice 1: Develop a Personal Financial Strategy")

engine = ContextualQuestions()
engine.reset() # Prepare the engine for the execution.
engine.run() # Run it!
