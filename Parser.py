"""
- Inference machine: Here, Knowledge Base (Rules) and Facts are matched together
- From experta Documentation, Chapter 3, page 8 & 11: This class is instantiated, populated with facts,
  and then executed. When facts match a rule, the rule is triggered.
  If there are  ≥1 triggers firing, experta executes those rules randomly (no internal order of items)
"""
import ParserGUI
import MentalProfile
import KnowledgeEngine
import KnowledgeEngineTwo
import database

AnswerArrayCP = ParserGUI.PHQ_QuestionsGUI() # THe complete(CP) user answers are transferred from GUI to answer array

# If you want to print out the information of the Contextual Questions including its answers, uncomment the next 3 lines
# print("Selected answers:")
# for x in range(0, 26):  # NumberOfAnswersReturnedByGUI #declareAnswerArry[x+1]
#         print("- " + (IRProcessor.QuestionArray[x] + "  " + AnswerArrayCP[x]))

class DepressionIR:
    DepressionArray = []
    for x in range(0,9):
        DepressionArray.append(AnswerArrayCP[x])
    #print("Value of Depression Array: ") #Uncomment this & next line to check, if output is correct
    #print(DepressionArray)

class AnxietyIR:
    AnxietyArray = []
    for x in range(9,16):
        AnxietyArray.append(AnswerArrayCP[x])
    #print("Value of Anxiety Array: ") #Uncomment this & next line to check, if output is correct
    #print(AnxietyArray)

class StressIR:
    StressArray = []
    for x in range (16,26):
        StressArray.append(AnswerArrayCP[x])
    #print("Value of Stress Array: ") #Uncomment this & next line to check, if output is correct
    #print(StressArray)

    # AnswerArray = []
print("Selected answers:")
for x in range(26, 43):
    print("- " + AnswerArrayCP[x])
#declareAnswerArry[x+1]

#Calculate Mental-Profile - Depression, Anxiety and Stress (DAS) as well as the xxxx are instantiated here
individualDepressionLevel = MentalProfile.Profile.calculateDepressionLevel(MentalProfile.Profile,DepressionIR.DepressionArray)
individualAnxietyLevel = MentalProfile.Profile.calculateAnxietyLevel(MentalProfile.Profile,AnxietyIR.AnxietyArray)
individualStressLevel = MentalProfile.Profile.calculateStressLevel(MentalProfile.Profile,StressIR.StressArray)
maxIndValueOfDAS = max(MentalProfile.Profile.calculateProfile(MentalProfile.Profile,DepressionIR.DepressionArray,AnxietyIR.AnxietyArray,StressIR.StressArray))
# print("MaxValue:") #Uncomment this & next line to check, if output is correct
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

InputArray = []
InputArray.append("Username")
InputArray.append(individualDepressionLevel)
InputArray.append(individualAnxietyLevel)
InputArray.append(individualStressLevel)
for x in range(26,44):
    InputArray.append(AnswerArrayCP[x])

dbOldFactsArray = database.insertInDB(InputArray)

#Start Knowledge-Engine
engineTwo = KnowledgeEngineTwo.ComparingOldInputWithNew()
engineTwo.reset()  # Prepare the engine for the execution.

# Declaring Financial Facts
engineTwo.declare(KnowledgeEngineTwo.NewFinancialFact(financialDistress=AnswerArrayCP[26]))  # GUIINPUT instead of hardcode
engineTwo.declare(KnowledgeEngineTwo.NewFinancialFact(employment=AnswerArrayCP[27]))  # GUIINPUT instead of hardcode

# Declaring Family Facts
engineTwo.declare(KnowledgeEngineTwo.NewFamilyFact(isCaretaker=AnswerArrayCP[28]))  # GUIINPUT instead of hardcode
engineTwo.declare(KnowledgeEngineTwo.NewFamilyFact(getsEnoughSupport=AnswerArrayCP[29]))
engineTwo.declare(KnowledgeEngineTwo.NewFamilyFact(caringForAdults=AnswerArrayCP[30]))
engineTwo.declare(KnowledgeEngineTwo.NewFamilyFact(caringForU18Children=AnswerArrayCP[31]))
engineTwo.declare(KnowledgeEngineTwo.NewFamilyFact(caringForDisabledChildren=AnswerArrayCP[32]))

# Declaring Leisure Facts
engineTwo.declare(KnowledgeEngineTwo.NewLeisureFact(enoughTimeForOneself=AnswerArrayCP[33]))
engineTwo.declare(KnowledgeEngineTwo.NewLeisureFact(leisureTimePlanned=AnswerArrayCP[34]))
engineTwo.declare(KnowledgeEngineTwo.NewLeisureFact(leisureTimePlannedExecuted=AnswerArrayCP[35]))

# Declaring Social Facts
engineTwo.declare(KnowledgeEngineTwo.NewSocialFact(anySocialActivities=AnswerArrayCP[36]))
engineTwo.declare(KnowledgeEngineTwo.NewSocialFact(missedOutDueExternalFactors=AnswerArrayCP[37]))
engineTwo.declare(KnowledgeEngineTwo.NewSocialFact(alternativeMeeting=AnswerArrayCP[38]))
engineTwo.declare(KnowledgeEngineTwo.NewSocialFact(stayedOut=AnswerArrayCP[39]))
engineTwo.declare(KnowledgeEngineTwo.NewSocialFact(negativeSocialExchanges=AnswerArrayCP[40]))
engineTwo.declare(KnowledgeEngineTwo.NewSocialFact(resolved=AnswerArrayCP[41]))
engineTwo.declare(KnowledgeEngineTwo.NewSocialFact(futureStrategy=AnswerArrayCP[42]))
engineTwo.declare(KnowledgeEngineTwo.NewSocialFact(sensibleResolvePossible=AnswerArrayCP[43]))

#EngineTwo Declare Old Facts mit dbOldFacts Array

engineTwo.run() # Executes & runs it