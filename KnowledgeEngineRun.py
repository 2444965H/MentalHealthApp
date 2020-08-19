"""
- Inference machine: Here, Knowledge Base (Rules) and Facts are matched together
- From experta Documentation, Chapter 3, page 11: The class (KnowledgeEngine) is instantiated, populated with facts,
and then executed
- PLEASE NOTE: Within the Knowledge Engine, as long as there are more than 1 triggers firing, experta
does not care which rule is being executed first
#They DO NOT MAINTAIN AN INTERNAL ORDER OF ITEMS #From experta Documentation, Chapter 3, page 8
- To shorten: DAS ≙ Depression, Anxiety, Stress
"""

import KnowledgeEngineGUI
import KnowledgeEngine
import ParserGUI


#AnswerArray = []
AnswerArrayContext = KnowledgeEngineGUI.AnswerArrayContextGUI
print(AnswerArrayContext)
# AnswerArrayPHQ = ParserGUI.PHQ_QuestionsGUI()
# print("Selected answers:")
# for x in range(0, 26):  # NumberOfAnswersReturnedByGUI #declareAnswerArry[x+1]
#         print("- " + AnswerArrayPHQ[x])
#
# class DepressionIR:
#     DepressionArray = []
#     for x in range(0,9):
#         DepressionArray.append(AnswerArrayPHQ[x])
#     #print("Value of Depression Array: ")
#     #print(DepressionArray)
#     #print(len(DepressionArray)) #will print how many values in the array are
#
# class AnxietyIR:
#     AnxietyArray = []
#     for x in range(9,16):
#         AnxietyArray.append(AnswerArrayPHQ[x])
#     #print("Value of Anxiety Array: ")
#     #print(AnxietyArray)
#
# class StressIR:
#     StressArray = []
#     for x in range (16,26):
#         StressArray.append(AnswerArrayPHQ[x])
#     #print("Value of Stress Array: ")
#     #print(StressArray)

#
# print("Selected answers:")
# for x in range(26, 43):  # NumberOfAnswersReturnedByGUI #declareAnswerArry[x+1]
#     print("- " + AnswerArrayContext[x])
#
# engine = KnowledgeEngine.ContextualQuestions()
# engine.reset()  # Prepare the engine for the execution.
#
# #Declaring Financial Facts
# engine.declare(KnowledgeEngine.FinancialFact(financialDistress=AnswerArrayContext[0])) #GUIINPUT instead of hardcode
# engine.declare(KnowledgeEngine.FinancialFact(employment=AnswerArrayContext[1])) #GUIINPUT instead of hardcode
#
# #Declaring Family Facts
# engine.declare(KnowledgeEngine.FamilyFact(isCaretaker=AnswerArrayContext[2])) #GUIINPUT instead of hardcode
# engine.declare(KnowledgeEngine.FamilyFact(getsEnoughSupport=AnswerArrayContext[3]))
# engine.declare(KnowledgeEngine.FamilyFact(caringForAdults=AnswerArrayContext[4]))
# engine.declare(KnowledgeEngine.FamilyFact(caringForU18Children=AnswerArrayContext[5]))
# engine.declare(KnowledgeEngine.FamilyFact(caringForDisabledChildren=AnswerArrayContext[6]))
#
# #Declaring Leisure Facts
# engine.declare(KnowledgeEngine.LeisureFact(enoughTimeForOneself=AnswerArrayContext[7]))
# engine.declare(KnowledgeEngine.LeisureFact(leisureTimePlanned=AnswerArrayContext[8]))
# engine.declare(KnowledgeEngine.LeisureFact(leisureTimePlannedExecuted=AnswerArrayContext[9]))
#
# #Declaring Social Facts
# engine.declare(KnowledgeEngine.SocialFact(anySocialActivities=AnswerArrayContext[10]))
# engine.declare(KnowledgeEngine.SocialFact(missedOutDueExternalFactors=AnswerArrayContext[11]))
# engine.declare(KnowledgeEngine.SocialFact(alternativeMeeting=AnswerArrayContext[12]))
# engine.declare(KnowledgeEngine.SocialFact(stayedOut=AnswerArrayContext[13]))
# engine.declare(KnowledgeEngine.SocialFact(negativeSocialExchanges=AnswerArrayContext[14]))
# engine.declare(KnowledgeEngine.SocialFact(resolved=AnswerArrayContext[15]))
# engine.declare(KnowledgeEngine.SocialFact(futureStrategy=AnswerArrayContext[16]))
# engine.declare(KnowledgeEngine.SocialFact(sensibleResolvePossible=AnswerArrayContext[17]))
#
#
#
# #Option 2
#
# # engine.declare(KnowledgeEngine.FinancialFact(financialDistress=AnswerArrayContext[26]))  # GUIINPUT instead of hardcode
# # engine.declare(KnowledgeEngine.FinancialFact(employment=AnswerArrayContext[27]))  # GUIINPUT instead of hardcode
# #
# # # Declaring Family Facts
# # engine.declare(KnowledgeEngine.FamilyFact(isCaretaker=AnswerArrayContext[28]))  # GUIINPUT instead of hardcode
# # engine.declare(KnowledgeEngine.FamilyFact(getsEnoughSupport=AnswerArrayContext[29]))
# # engine.declare(KnowledgeEngine.FamilyFact(caringForAdults=AnswerArrayContext[30]))
# # engine.declare(KnowledgeEngine.FamilyFact(caringForU18Children=AnswerArrayContext[31]))
# # engine.declare(KnowledgeEngine.FamilyFact(caringForDisabledChildren=AnswerArrayContext[32]))
# #
# # # Declaring Leisure Facts
# # engine.declare(KnowledgeEngine.LeisureFact(enoughTimeForOneself=AnswerArrayContext[33]))
# # engine.declare(KnowledgeEngine.LeisureFact(leisureTimePlanned=AnswerArrayContext[34]))
# # engine.declare(KnowledgeEngine.LeisureFact(leisureTimePlannedExecuted=AnswerArrayContext[35]))
# #
# # # Declaring Social Facts
# # engine.declare(KnowledgeEngine.SocialFact(anySocialActivities=AnswerArrayContext[36]))
# # engine.declare(KnowledgeEngine.SocialFact(missedOutDueExternalFactors=AnswerArrayContext[37]))
# # engine.declare(KnowledgeEngine.SocialFact(alternativeMeeting=AnswerArrayContext[38]))
# # engine.declare(KnowledgeEngine.SocialFact(stayedOut=AnswerArrayContext[39]))
# # engine.declare(KnowledgeEngine.SocialFact(negativeSocialExchanges=AnswerArrayContext[40]))
# # engine.declare(KnowledgeEngine.SocialFact(resolved=AnswerArrayContext[41]))
# # engine.declare(KnowledgeEngine.SocialFact(futureStrategy=AnswerArrayContext[42]))
# # engine.declare(KnowledgeEngine.SocialFact(sensibleResolvePossible=AnswerArrayContext[43]))
# engine.run()  # Executes & runs it