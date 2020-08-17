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


#AnswerArray = []
AnswerArray = KnowledgeEngineGUI.contextualQuestionsGUI()
print("Selected answers:")
for x in range(0, 18):  # NumberOfAnswersReturnedByGUI #declareAnswerArry[x+1]
    print("- " + AnswerArray[x])

engine = KnowledgeEngine.ContextualQuestions()
engine.reset()  # Prepare the engine for the execution.

#Declaring Financial Facts
engine.declare(KnowledgeEngine.FinancialFact(financialDistress=AnswerArray[0])) #GUIINPUT instead of hardcode
engine.declare(KnowledgeEngine.FinancialFact(employment=AnswerArray[1])) #GUIINPUT instead of hardcode

#Declaring Family Facts
engine.declare(KnowledgeEngine.FamilyFact(isCaretaker=AnswerArray[2])) #GUIINPUT instead of hardcode
engine.declare(KnowledgeEngine.FamilyFact(getsEnoughSupport=AnswerArray[3]))
engine.declare(KnowledgeEngine.FamilyFact(caringForAdults=AnswerArray[4]))
engine.declare(KnowledgeEngine.FamilyFact(caringForU18Children=AnswerArray[5]))
engine.declare(KnowledgeEngine.FamilyFact(caringForDisabledChildren=AnswerArray[6]))

#Declaring Leisure Facts
engine.declare(KnowledgeEngine.LeisureFact(enoughTimeForOneself=AnswerArray[7]))
engine.declare(KnowledgeEngine.LeisureFact(leisureTimePlanned=AnswerArray[8]))
engine.declare(KnowledgeEngine.LeisureFact(leisureTimePlannedExecuted=AnswerArray[9]))

#Declaring Social Facts
engine.declare(KnowledgeEngine.SocialFact(anySocialActivities=AnswerArray[10]))
engine.declare(KnowledgeEngine.SocialFact(missedOutDueExternalFactors=AnswerArray[11]))
engine.declare(KnowledgeEngine.SocialFact(alternativeMeeting=AnswerArray[12]))
engine.declare(KnowledgeEngine.SocialFact(stayedOut=AnswerArray[13]))
engine.declare(KnowledgeEngine.SocialFact(negativeSocialExchanges=AnswerArray[14]))
engine.declare(KnowledgeEngine.SocialFact(resolved=AnswerArray[15]))
engine.declare(KnowledgeEngine.SocialFact(futureStrategy=AnswerArray[16]))
engine.declare(KnowledgeEngine.SocialFact(sensibleResolvePossible=AnswerArray[17]))

engine.run()  # Executes & runs it