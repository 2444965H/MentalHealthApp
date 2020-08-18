from gooey import Gooey
from gooey import GooeyParser

@Gooey(program_name='Contextual Questions',
       tabbed_groups=True,
       navigation='Tabbed',
       fullscreen=True)

def contextualQuestionsGUI():
    parser = GooeyParser(description="Please go through the 4 tabs and answer the questions")
    AnswerArray = []

#Financial Questions
    allFinancialQuestions = parser.add_argument_group('Financial') #Groups the questions in a tab and gives them a name

    financialQuestionFinancialDistress = allFinancialQuestions.add_argument(
        "financialdistress", #equal to AnswerArray[0]
        metavar='Are you in financial distress?',
        choices=["Yes, I am in financial distress",
                 "No, I am not in financial distress"]
        # default="yes, I'm in financial distress" #If you want to have one of the values as a default value, re-comment this
    )

    financialQuestionEmployment = allFinancialQuestions.add_argument(
        "employment", #equal to AnswerArray[1]
        metavar='What is your employment situation?',
        choices=['Full-Time',
                 'Part-Time',
                 'On sabbatical - not working by choice',
                 'Otherwise occupied',
                 'Job-seeking']
    )

#Family Questions
    allFamilyQuestions = parser.add_argument_group('Family') #Groups the questions in a tab and gives them a name

    familyQuestionCaretaker = allFamilyQuestions.add_argument(
        "isCaretaker", #equal to AnswerArray[2]
        metavar='Are you taking care of any family members (e.g. children, elderly)?',
        choices=['Yes, I am a caregiver',
                 'No, I am not a caregiver'],
    )

    familyQuestionEnoughSupport = allFamilyQuestions.add_argument(
        "getsEnoughSupport", #equal to AnswerArray[3]
        metavar='Do you have/get enough support as a caregiver? E.g. from partner, social workers',
        choices=['Yes, I have enough support',
                 'No, I have not enough support',
                 'Not applicable - not a caregiver']
        )

    familyQuestionCaringForAdults = allFamilyQuestions.add_argument(
        "caringForAdults", #equal to AnswerArray[4]
        metavar='Are you a caregiver for an adult?',
        choices=['Yes, I am a caregiver for an adult',
                 'No, I am not a caregiver for an adult',
                 'Not applicable - not a caregiver']
    )

    familyQuestionCaringForChildrenU18 = allFamilyQuestions.add_argument(
        "caringForU18Children", #equal to AnswerArray[5]
        metavar = 'Are you a caregiver for any children under 18?',
        choices = ['Yes, I am a caregiver for at least one child under 18',
                   'No, I am not a caregiver for child/children under 18',
                   'Not applicable - not a caregiver']
    )

    familyQuestionCaringForDisabledChildren = allFamilyQuestions.add_argument(
        "caringForDisabledChildren", #equal to AnswerArray[6]
        metavar= 'Are you a caregiver for a disabled child?',
        choices = ['Yes, I am a caregiver for at least one disabled child',
                   'No, I am not a caregiver for at least one disabled child',
                   'Not applicable - not a caregiver']
    )

#Leisure Questions
    allLeisureQuestions = parser.add_argument_group('Leisure')

    leisureQuestionEnoughTimeForOneself = allLeisureQuestions.add_argument(
        "enoughTimeForOneself",
        metavar= 'Did you spent enough leisure time on yourself?',
        choices= ['Yes, I had enough leisure time for myself',
                  'No, I did not have enough leisure time for myself']
    )

    leisureQuestionOffTimePlanned = allLeisureQuestions.add_argument(
        "leisureTimePlanned",
        metavar='Did you plan to take off some time for leisure?',
        choices=['Yes, I planned/am planning to take off time for leisure',
                 'No, I did/am not planning to take off time for leisure']
    )

    leisureQuestionLeisureTimePlannedExecuted = allLeisureQuestions.add_argument(
        "leisureTimePlannedExecuted",
        metavar= 'Were you able to execute your leisure/hobbies like you planned?',
        choices= ['Yes, I had leisure time like planned',
                  'No, I was not able to take leisure time like planned']
    )

 #Social Questions
    allSocialQuestions = parser.add_argument_group('Social') #Groups the questions in a tab and gives them a name

    socialQuestionAnySocialActivities = allSocialQuestions.add_argument(
        "anySocialActivities",
        metavar='Did you participate in any social activities?',
        choices=["Yes, I participated in social activities",
                 "No, I did not participate in any social activity"]
    )

    socialQuestionMissedOutDueExternalFactors = allSocialQuestions.add_argument(
        "missedOutDueExternalFactors",
        metavar='Did you miss out on social activities due to other responsibilities or ext. factors?',
        choices=["Yes, I did miss social activities due to external factors",
                 "No, I did not miss any social activities due to external factors"]
    )

    socialQuestionAlternativeMeeting = allSocialQuestions.add_argument(
        "alternativeMeeting",
        metavar='Did you seek out alternatives for the meeting?',
        choices=["Yes, we did seek out alternatives to meet",
                 "No, we did not seek out alternatives to meet"]
    )

    socialQuestionStayedOut = allSocialQuestions.add_argument(
        "stayedOut",
        metavar='Did you cancel plans you had with other or stayed out of any social meeting',
        choices=["Yes, I cancelled/stayed out of social meetings",
                 "No, I did not cancel/stayed out of social meetings"]
    )

    socialQuestionNegativeExchanges = allSocialQuestions.add_argument(
        "negativeSocialExchanges",
        metavar='Did you have any negative  social exchanges?',
        choices=['Yes, I had negative social exchanges',
                 'No, I did not have any negative social exchanges']
    )

    socialQuestionResolved = allSocialQuestions.add_argument(
        "resolved",
        metavar='Did you resolve the negative social exchanges?',
        choices=['Yes, I resolved the negative social exchange(s)',
                 'No, I did not resolve the negative social exchange(s)']
    )

    socialQuestionFutureStrategy = allSocialQuestions.add_argument(
        "futureStrategy",
        metavar='Do you have a strategy on how to deal with those kind of negative social exchanges in the future?',
        choices=['Yes, I have a negative social exchange strategy',
                 'No, I do not have a strategy for negative social exchanges']
    )

    socialQuestionSensibleResolvePossible = allSocialQuestions.add_argument(
        "sensibleResolvePossible",
        metavar='Do you have the possibility to resolve this matter sensibly?',
        choices=['Yes, I can resolve this matter sensibly',
                 'No, I cannot resolve this matter sensibly']
    )


#List of parsed GUI answers
    #Disable the AnswerArray.append below AND the Question above AND adjust AnswerArray length in KnowledgeEngineRun.py,
    #if you want it disabled in the GUI
    #Financial Questions
    AnswerArray.append(parser.parse_args().financialdistress)
    AnswerArray.append(parser.parse_args().employment)

    #Family/Caretaker Questions
    AnswerArray.append(parser.parse_args().isCaretaker)
    AnswerArray.append(parser.parse_args().getsEnoughSupport)
    AnswerArray.append(parser.parse_args().caringForAdults)
    AnswerArray.append(parser.parse_args().caringForU18Children)
    AnswerArray.append(parser.parse_args().caringForDisabledChildren)

    #Leisure Questions
    AnswerArray.append(parser.parse_args().enoughTimeForOneself)
    AnswerArray.append(parser.parse_args().leisureTimePlanned)
    AnswerArray.append(parser.parse_args().leisureTimePlannedExecuted)

    #Social Questions
    AnswerArray.append(parser.parse_args().anySocialActivities)
    AnswerArray.append(parser.parse_args().missedOutDueExternalFactors)
    AnswerArray.append(parser.parse_args().alternativeMeeting)
    AnswerArray.append(parser.parse_args().stayedOut)
    AnswerArray.append(parser.parse_args().negativeSocialExchanges)
    AnswerArray.append(parser.parse_args().resolved)
    AnswerArray.append(parser.parse_args().futureStrategy)
    AnswerArray.append(parser.parse_args().sensibleResolvePossible)

    # args = parser.parse_args()    #Redo uncomment this to check what input it takes in GUI
    # print("Response:", args)      #Redo uncomment this to check what input it takes in GUI

    return AnswerArray

