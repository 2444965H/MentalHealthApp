import argparse
from experta import Rule, Fact, MATCH, DefFacts
from gooey import Gooey
from gooey import GooeyParser
from wx.lib.agw.buttonpanel import BPArt
import SeverityAlgorithm


@Gooey(program_name='Contextual Questions',
       tabbed_groups=True,
       navigation='Tabbed',
       fullscreen=True)
def contextualQuestionsGUI():
    parser = GooeyParser(description="Please go through the 4 tabs and answer the questions")
    AnswerArray = []

#Financial Questions
    allFinancialQuestions = parser.add_argument_group('Financial') #Groups the Questions in a tab
    financialQuestionFinancialDistress = allFinancialQuestions.add_argument(
        "financialdistress", #equal to AnswerArray[0]
        metavar='Are you in financial distress?',
        choices=["yes, I am in financial distress",
                 "no, I am not in financial distress"]
        # default="yes, I'm in financial distress" #If you want to have one of  the values as a default value, re-comment this
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
    allFamilyQuestions = parser.add_argument_group('Family')
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
                 'No, I have not enough support']
        )

    familyQuestionCaringForAdults = allFamilyQuestions.add_argument(
        "caringForAdults", #equal to AnswerArray[4]
        metavar='Are you a caregiver for an adult?',
        choices=['yes, I am a caregiver for an adult',
                 'No, I am not a caregiver for an adult']
    )

    familyQuestionCaringForChildrenU18 = allFamilyQuestions.add_argument(
        "caringForU18Children", #equal to AnswerArray[5]
        metavar = 'Are you a caregiver for any children under 18?',
        choices = ['yes, I am a caregiver for at least one child under 18',
                   'No, I am not a caregiver for child/children under 18']
    )

    familyQuestionCaringForDisabledChildren = allFamilyQuestions.add_argument(
        "caringForDisabledChildren", #equal to AnswerArray[6]
        metavar= 'Are you a caregiver for a disabled child?',
        choices = ['yes, I am a caregiver for at least one disabled child',
                   'no, I am not a caregiver for at least one disabled child']
    )

#Leisure Questions
    allLeisureQuestions = parser.add_argument_group('Leisure')
    leisureQuestionEnoughTimeForOneself = allLeisureQuestions.add_argument(
        "enoughTimeForOneself",
        metavar= 'Did you spent enough leisure time on yourself?',
        choices= ['yes, I had enough leisure time for myself',
                  'no, I did not have enough leisure time for myself']
    )

    leisureQuestionOffTimePlanned = allLeisureQuestions.add_argument(
        "leisureTimePlanned",
        metavar='Did you plan to take off some time for leisure?',
        choices=['yes, I planned/am planning to take off time for leisure',
                 'no, I did/am not planning to take off time for leisure']
    )

    leisureQuestionLeisureTimePlannedExecuted = allLeisureQuestions.add_argument(
        "leisureTimePlannedExecuted",
        metavar= 'Were you able to execute your leisure/hobbies like you planned?',
        choices= ['yes, I had leisure time like planned',
                  'no, I was not able to take leisure time like planned']
    )

#Social Questions
    # allSocialQuestions = parser.add_argument_group('Social')
    # socialQuestionAnySocialActivities = parser.add_argument(
    #     "anySocialActivities",
    #     metavar='Did you participate in any social activities?',
    #     choices=["yes, I participated in social activities",
    #              "no, I did not participate in any social activity"]
    # )
    #
    # socialQuestionMissedOutDueExternalFactors = parser.add_argument(
    #     "missedOutDueExternalFactors",
    #     metavar = 'Did you miss out on social activities due to other responsibilities or ext. factors?',
    #     choices = ["yes,  I did miss social activities due to external factors",
    #                "no, I did not miss any social activities due to external factors"]
    # )
    #
    # socialQuestionAlternativeMeeting = parser.add_argument(
    #     "alternativeMeeting",
    #     metavar='Did you seek out alternatives for the meeting?',
    #     choices=["yes, we did seek out alternatives to meet",
    #              "no, we did not seek out alternatives to meet"]
    # )

    # socialQuestionStayedOut = parser.add_argument(
    #     "stayedOut",
    #     metavar='Did you cancel plans you had with other or stayed out of any social meeting',
    #     choices=["yes, I cancelled/stayed out of social meetings",
    #              "no, I did not cancel/stayed out of social meetings"]
    # )

    # socialQuestionNegativeExchanges = parser.add_argument(
    #     "negativeSocialExchanges",
    #     metavar='Did you have any negative  social exchanges?',
    #     choices=['yes, I had negative social exchanges',
    #              'no, I did not have any negative social exchanges']
    # )

    # socialQuestionResolved = parser.add_argument(
    #     "resolved",
    #     metavar='Did you resolve the negative social exchanges?',
    #     choices=['yes, I resolved the negative social exchange(s)',
    #              'no, I did not resolve the negative social exchange(s)']
    # )

    # socialQuestionFutureStrategy = parser.add_argument(
    #     "futureStrategy",
    #     metavar='Do you have a strategy on how to deal with those kind of negative social exchanges in the future?',
    #     choices=['yes, I have a negative social exchange strategy',
    #              'no, I do not have a strategy for negative social exchanges']
    # )

    # socialQuestionSensibleResolvePossible = parser.add_argument(
    #     "sensibleResolvePossible",
    #     metavar='Do you have the possibility to resolve this matter sensibly?',
    #     choices=['yes, I can resolve this matter sensibly',
    #              'no, I cannot resolve this matter sensibly']
    # )

#List of parsed GUI answers
    #Disable the Array AND the Question, if you want it disabled in the GUI
    AnswerArray.append(parser.parse_args().financialdistress)
    AnswerArray.append(parser.parse_args().employment)

    AnswerArray.append(parser.parse_args().isCaretaker)
    AnswerArray.append(parser.parse_args().getsEnoughSupport)
    AnswerArray.append(parser.parse_args().caringForAdults)
    AnswerArray.append(parser.parse_args().caringForU18Children)
    AnswerArray.append(parser.parse_args().caringForDisabledChildren)

    AnswerArray.append(parser.parse_args().enoughTimeForOneself)
    AnswerArray.append(parser.parse_args().leisureTimePlanned)
    AnswerArray.append(parser.parse_args().leisureTimePlannedExecuted)

    # AnswerArray.append(parser.parse_args().anySocialActivities)
    # AnswerArray.append(parser.parse_args().missedOutDueExternalFactors)
    # AnswerArray.append(parser.parse_args().alternativeMeeting)
    # AnswerArray.append(parser.parse_args().stayedOut)
    # AnswerArray.append(parser.parse_args().negativeSocialExchanges)
    # AnswerArray.append(parser.parse_args().resolved)
    # AnswerArray.append(parser.parse_args().futureStrategy)
    # AnswerArray.append(parser.parse_args().sensibleResolvePossible)

    # args = parser.parse_args()
    # print("Response:", args) #Redo uncomment this to check what input it takes in GUI
    return AnswerArray




#    parser.add_argument('filename', help="name of the file to process", widget='FileChooser')
#    parser.add_argument("-n", "--nolinenum", action='store_true', help="do not generate line numbers")
#    parser.add_argument("-c", "--comments", action='store_true', help="generate commants")

# group1 = parser.add_mutually_exclusive_group()
# group2 = parser.add_mutually_exclusive_group()
# financialdistress = group1.add_argument("-financiallyDistressed", metavar="--yes, I'm in financial distress", action="store_true")
# financialdistress = group1.add_argument("-notfinanciallyDistressed", metavar="--no, I'm not in financial distress", action="store_true")
# employment = group2.add_argument("-Full-Time", metavar="--I'm working Full-Time",  action="store_true")
# employment = group2.add_argument("-Part-Time", metavar="--I'm working Part-Time", action="store_true")
