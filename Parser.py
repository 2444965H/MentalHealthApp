"""
- Inference machine: Here, Knowledge Base (Rules) and Facts are matched together
- From experta Documentation, Chapter 3, page 11: The class (KnowledgeEngine) is instantiated, populated with facts,
and then executed
- PLEASE NOTE: s long as there are more than 1 triggers firing, experta does not care which rule is being executed first
- They DO NOT MAINTAIN AN INTERNAL ORDER OF ITEMS #From experta Documentation, Chapter 3, page 8
- To shorten: DAS ≙ Depression, Anxiety, Stress

-This file loads the input and then parses it into a class for the internal representation (IR)
- The classes are divided into subsections, each with its own IR array.
- Print statements (that are hashed out) can be unhashed in order to check for correct array (output)
- The classes' IR arrays are then processed in the next step in the IRProcessor.py
"""

import ParserGUI
import MentalProfile
import KnowledgeEngine

AnswerArrayCP = ParserGUI.PHQ_QuestionsGUI()

# If you want to print out the information of the Contextual Questions including it answers, uncomment the next 3 lines
# print("Selected answers:")
# for x in range(0, 26):  # NumberOfAnswersReturnedByGUI #declareAnswerArry[x+1]
#         print("- " + (IRProcessor.QuestionArray[x] + "  " + AnswerArrayCP[x]))

class DepressionIR:
    DepressionArray = []
    for x in range(0,9):
        DepressionArray.append(AnswerArrayCP[x])
    #print("Value of Depression Array: ")
    #print(DepressionArray)

class AnxietyIR:
    AnxietyArray = []
    for x in range(9,16):
        AnxietyArray.append(AnswerArrayCP[x])
    #print("Value of Anxiety Array: ")
    #print(AnxietyArray)

class StressIR:
    StressArray = []
    for x in range (16,26):
        StressArray.append(AnswerArrayCP[x])
    #print("Value of Stress Array: ")
    #print(StressArray)

    # AnswerArray = []
print("Selected answers:")
for x in range(26, 43):
    print("- " + AnswerArrayCP[x])
#declareAnswerArry[x+1]

#Calculate Mental-Profile
individualStressLevel = MentalProfile.Profile.calculateStressLevel(MentalProfile.Profile,StressIR.StressArray)
maxIndValueOfDAS = max(MentalProfile.Profile.calculateProfile(MentalProfile.Profile,DepressionIR.DepressionArray,AnxietyIR.AnxietyArray,StressIR.StressArray))
# print("MaxValue:")
# print(maxIndValueOfDAS)

KnowledgeEngine.maxIndValueOfDASFiveToNine = (maxIndValueOfDAS >=5 and maxIndValueOfDAS <10) #If the highest DAS value is from 5-9
KnowledgeEngine.maxIndValueOfDASTenToFourteen = (maxIndValueOfDAS >=10 and maxIndValueOfDAS<15) #If the highest DAS value is from 10-14
KnowledgeEngine.maxIndValueOfDASFifteen = (maxIndValueOfDAS >=15)
KnowledgeEngine.maxIndValueOfDAS = maxIndValueOfDAS
KnowledgeEngine.individualStressLevel = individualStressLevel

#Start Knowledge-Engine
engine = KnowledgeEngine.ContextualQuestions()
engine.reset()  # Prepare the engine for the execution.

# Declaring Financial Facts
engine.declare(KnowledgeEngine.FinancialFact(financialDistress=AnswerArrayCP[26]))  # GUIINPUT instead of hardcode
engine.declare(KnowledgeEngine.FinancialFact(employment=AnswerArrayCP[27]))  # GUIINPUT instead of hardcode

# Declaring Family Facts
engine.declare(KnowledgeEngine.FamilyFact(isCaretaker=AnswerArrayCP[28]))  # GUIINPUT instead of hardcode
engine.declare(KnowledgeEngine.FamilyFact(getsEnoughSupport=AnswerArrayCP[29]))
engine.declare(KnowledgeEngine.FamilyFact(caringForAdults=AnswerArrayCP[30]))
engine.declare(KnowledgeEngine.FamilyFact(caringForU18Children=AnswerArrayCP[31]))
engine.declare(KnowledgeEngine.FamilyFact(caringForDisabledChildren=AnswerArrayCP[32]))

# Declaring Leisure Facts
engine.declare(KnowledgeEngine.LeisureFact(enoughTimeForOneself=AnswerArrayCP[33]))
engine.declare(KnowledgeEngine.LeisureFact(leisureTimePlanned=AnswerArrayCP[34]))
engine.declare(KnowledgeEngine.LeisureFact(leisureTimePlannedExecuted=AnswerArrayCP[35]))

# Declaring Social Facts
engine.declare(KnowledgeEngine.SocialFact(anySocialActivities=AnswerArrayCP[36]))
engine.declare(KnowledgeEngine.SocialFact(missedOutDueExternalFactors=AnswerArrayCP[37]))
engine.declare(KnowledgeEngine.SocialFact(alternativeMeeting=AnswerArrayCP[38]))
engine.declare(KnowledgeEngine.SocialFact(stayedOut=AnswerArrayCP[39]))
engine.declare(KnowledgeEngine.SocialFact(negativeSocialExchanges=AnswerArrayCP[40]))
engine.declare(KnowledgeEngine.SocialFact(resolved=AnswerArrayCP[41]))
engine.declare(KnowledgeEngine.SocialFact(futureStrategy=AnswerArrayCP[42]))
engine.declare(KnowledgeEngine.SocialFact(sensibleResolvePossible=AnswerArrayCP[43]))

engine.run()  # Executes & runs it