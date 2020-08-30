from gooey import Gooey
from gooey import GooeyParser


@Gooey(program_name='Complete Questionaire',
       tabbed_groups=True,
       navigation='Tabbed',
       fullscreen=True)
def PHQ_QuestionsGUI():
    parserGUI = GooeyParser(description="Please go through all 7 tabs and answer the questions")
    AnswerArrayGUI = []

#PHQ9 Questions for Depression - Part of PHQ-D
    allPHQ9Questions = parserGUI.add_argument_group('PHQ-9 for Depression') #Groups the Questions in a tab

    interestOrPleasureinDoingThings = allPHQ9Questions.add_argument(
        "littleInterestInDoingThings", #equal to AnswerArrayPHQ[0]
        metavar='Little interest or pleasure in doing things?',
        choices=["Not at all",
                 "Several days",
                 "More than half the days",
                 "Nearly every day"]
    )

    feelingDown = allPHQ9Questions.add_argument(
        "feelingDown", #equal to AnswerArrayPHQ[1]
        metavar='Feeling down, depressed, or hopeless?',
        choices=["Not at all",
                 "Several days",
                 "More than half the days",
                 "Nearly every day"]
    )

    troubleSleeping = allPHQ9Questions.add_argument(
        "troubleSleeping", #equal to AnswerArrayPHQ[2]
        metavar='Trouble falling or staying asleep, or sleeping too much',
        choices=["Not at all",
                 "Several days",
                 "More than half the days",
                 "Nearly every day"]
    )

    feelingTired = allPHQ9Questions.add_argument(
        "feelingTired", #equal to AnswerArrayPHQ[3]
        metavar='Feeling tired or having little energy',
        choices=["Not at all",
                 "Several days",
                 "More than half the days",
                 "Nearly every day"]
    )

    poorAppetite = allPHQ9Questions.add_argument(
        "poorAppetite", #equal to AnswerArrayPHQ[4]
        metavar='Poor apppetite or overeating',
        choices=["Not at all",
                 "Several days",
                 "More than half the days",
                 "Nearly every day"]
    )

    feelingBadAboutYourself = allPHQ9Questions.add_argument(
        "feelingBadAboutYourself", #equal to AnswerArrayPHQ[5]
        metavar='Feeling bad about yourself - or that you are a failure or have let yourself or your family down',
        choices=["Not at all",
                 "Several days",
                 "More than half the days",
                 "Nearly every day"]
    )

    badConcentration = allPHQ9Questions.add_argument(
        "badConcentration", #equal to AnswerArrayPHQ[6]
        metavar='Trouble concentrating on things, such as reading the newspaper or watching television',
        choices=["Not at all",
                 "Several days",
                 "More than half the days",
                 "Nearly every day"]
    )

    speakingSlowORFast = allPHQ9Questions.add_argument(
        "speakingSlowORFast", #equal to AnswerArrayPHQ[7]
        metavar='Moving/Speaking so slowly OR being restless that others have noticed?',
        #'Moving or speaking so slowly that other people could have noticed? Or the opposite - being so fidgety or restless that you have been moving around a lot more than usual',
        choices=["Not at all",
                 "Several days",
                 "More than half the days",
                 "Nearly every day"]
    )

    hurtingOneself = allPHQ9Questions.add_argument(
        "hurtingOneself", #equal to AnswerArrayPHQ[8]
        metavar='Thoughts that you would be better off dead or of hurting yourself in some way',
        choices=["Not at all",
                 "Several days",
                 "More than half the days",
                 "Nearly every day"]
    )

#GAD-7 (Modul of PHQ-D)
    allGAD7Questions = parserGUI.add_argument_group('GAD-7 for Anxiety')

    feelingNervous = allGAD7Questions.add_argument(
        "feelingNervous", #equal to AnswerArrayPHQ[0]
        metavar='Feeling nervous, anxious or on edge?',
        choices=["Not at all",
                 "Several days",
                 "More than half the days",
                 "Nearly every day"]
    )

    worrying = allGAD7Questions.add_argument(
        "worrying", #equal to AnswerArrayPHQ[1]
        metavar='Not being able to stop or control worrying?',
        choices=["Not at all",
                 "Several days",
                 "More than half the days",
                 "Nearly every day"]
    )

    worryingTooMuch = allGAD7Questions.add_argument(
        "worryingTooMuch",
        metavar='Worrying too much about different things?',
        choices=["Not at all",
                 "Several days",
                 "More than half the days",
                 "Nearly every day"]
    )

    troubleRelaxing = allGAD7Questions.add_argument(
        "troubleRelaxing",
        metavar='Trouble relaxing?',
        choices=["Not at all",
                 "Several days",
                 "More than half the days",
                 "Nearly every day"]
    )

    restless = allGAD7Questions.add_argument(
        "restless",
        metavar='Being so restless that it is hard to sit still?',
        choices=["Not at all",
                 "Several days",
                 "More than half the days",
                 "Nearly every day"]
    )

    annoyedOrIrritable = allGAD7Questions.add_argument(
        "annoyedOrIrritable",
        metavar='Becoming easily annoyed or irritable?',
        choices=["Not at all",
                 "Several days",
                 "More than half the days",
                 "Nearly every day"]
    )

    afraidAwfulHappening = allGAD7Questions.add_argument(
        "afraidAwfulHappening",
        metavar='Feeling afraid as if something awful might happen?',
        choices=["Not at all",
                 "Several days",
                 "More than half the days",
                 "Nearly every day"]
    )

#PHQ-Stress Modul (Modul of PHQ-D - from the questions 12a-12j)

    allPHQStressQuestions = parserGUI.add_argument_group('PHQ-Stress Modul for Stress')

    worryAboutHealth = allPHQStressQuestions.add_argument(
        "worryAboutHealth", #equal to AnswerArrayPHQ[0]
        metavar='Worry about your health',
        choices=["Not affected",
                 "Little affected",
                 "Severely affected"]
    )

    weightOrAppearance = allPHQStressQuestions.add_argument(
        "weightOrAppearance", #equal to AnswerArrayPHQ[1]
        metavar='Your weight or your appearance',
        choices=["Not affected",
                 "Little affected",
                 "Severely affected"]
    )

    sexualDesire = allPHQStressQuestions.add_argument(
        "sexualDesire", #equal to AnswerArrayPHQ[2]
        metavar='Little or no sexual desire or pleasure during intercourse',
        choices=["Not affected",
                 "Little affected",
                 "Severely affected"]
    )

    difficultiesWithSO = allPHQStressQuestions.add_argument(
        "difficultiesWithSO", #equal to AnswerArrayPHQ[3]
        metavar='Difficulties with the spouse, significant other, girlfriend / boyfriend',
        choices=["Not affected",
                 "Little affected",
                 "Severely affected"]
    )

    caregiverBurden = allPHQStressQuestions.add_argument(
        "caregiverBurden", #equal to AnswerArrayPHQ[4]
        metavar='Burden of caring for children, parents, or other family members',
        choices=["Not affected",
                 "Little affected",
                 "Severely affected"]
    )

    stressAtWorkSchool= allPHQStressQuestions.add_argument(
        "stressAtWorkSchool", #equal to AnswerArrayPHQ[5]
        metavar='Stress at work or at school',
        choices=["Not affected",
                 "Little affected",
                 "Severely affected"]
    )

    financialProblems= allPHQStressQuestions.add_argument(
        "financialProblems", #equal to AnswerArrayPHQ[6]
        metavar='Financial problems or concerns',
        choices=["Not affected",
                 "Little affected",
                 "Severely affected"]
    )

    noTalkPartner= allPHQStressQuestions.add_argument(
        "noTalkPartner", #equal to AnswerArrayPHQ[7]
        metavar='Not having someone to talk to about problems',
        choices=["Not affected",
                 "Little affected",
                 "Severely affected"]
    )

    sthBadHappened= allPHQStressQuestions.add_argument(
        "sthBadHappened", #equal to AnswerArrayPHQ[8]
        metavar='Something bad that happened recently',
        choices=["Not affected",
                 "Little affected",
                 "Severely affected"]
    )

    thoughtsOrDreamsAboutTerribleEvents= allPHQStressQuestions.add_argument(
        "thoughtsOrDreamsAboutTerribleEvents", #equal to AnswerArrayPHQ[9]
        metavar='Thoughts about terrible events from earlier or dreams about it',
                #' - e.g. the destruction of your own home, a serious accident, a robbery, physical violence or a forced sexual act',
        choices=["Not affected",
                 "Little affected",
                 "Severely affected"]
    )

    # Financial Questions
    allFinancialQuestions = parserGUI.add_argument_group(
        'Financial')  # Groups the questions in a tab and gives them a name

    financialQuestionFinancialDistress = allFinancialQuestions.add_argument(
        "financialdistress",  # equal to AnswerArray[0]
        metavar='Are you in financial distress?',
        choices=["Yes, I am in financial distress",
                 "No, I am not in financial distress"]
        # default="yes, I'm in financial distress" #If you want to have one of the values as a default value, re-comment this
    )

    financialQuestionEmployment = allFinancialQuestions.add_argument(
        "employment",  # equal to AnswerArray[1]
        metavar='What is your employment situation?',
        choices=['Full-Time',
                 'Part-Time',
                 'On sabbatical - not working by choice',
                 'Otherwise occupied',
                 'Job-seeking']
    )

    # Family Questions
    allFamilyQuestions = parserGUI.add_argument_group('Family')  # Groups the questions in a tab and gives them a name

    familyQuestionCaretaker = allFamilyQuestions.add_argument(
        "isCaretaker",  # equal to AnswerArray[2]
        metavar='Are you taking care of any family members (e.g. children, elderly)?',
        choices=['Yes, I am a caregiver',
                 'No, I am not a caregiver'],
    )

    familyQuestionEnoughSupport = allFamilyQuestions.add_argument(
        "getsEnoughSupport",  # equal to AnswerArray[3]
        metavar='Do you have/get enough support as a caregiver? E.g. from partner, social workers?',
        choices=['Yes, I have enough support',
                 'No, I have not enough support',
                 'Not applicable - not a caregiver']
    )

    familyQuestionCaringForAdults = allFamilyQuestions.add_argument(
        "caringForAdults",  # equal to AnswerArray[4]
        metavar='Are you a caregiver for an adult?',
        choices=['Yes, I am a caregiver for an adult',
                 'No, I am not a caregiver for an adult',
                 'Not applicable - not a caregiver']
    )

    familyQuestionCaringForChildrenU18 = allFamilyQuestions.add_argument(
        "caringForU18Children",  # equal to AnswerArray[5]
        metavar='Are you a caregiver for any children under 18?',
        choices=['Yes, I am a caregiver for at least one child under 18',
                 'No, I am not a caregiver for child/children under 18',
                 'Not applicable - not a caregiver']
    )

    familyQuestionCaringForDisabledChildren = allFamilyQuestions.add_argument(
        "caringForDisabledChildren",  # equal to AnswerArray[6]
        metavar='Are you a caregiver for a disabled child?',
        choices=['Yes, I am a caregiver for at least one disabled child',
                 'No, I am not a caregiver for at least one disabled child',
                 'Not applicable - not a caregiver']
    )

    # Leisure Questions
    allLeisureQuestions = parserGUI.add_argument_group('Leisure')

    leisureQuestionEnoughTimeForOneself = allLeisureQuestions.add_argument(
        "enoughTimeForOneself",
        metavar='Did you spent enough leisure time on yourself?',
        choices=['Yes, I had enough leisure time for myself',
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
        metavar='Were you able to execute your leisure/hobbies like you planned?',
        choices=['Yes, I had leisure time like planned',
                 'No, I was not able to take leisure time like planned']
    )

    # Social Questions
    allSocialQuestions = parserGUI.add_argument_group('Social')  # Groups the questions in a tab and gives them a name

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
        metavar='Did you have any negative social exchanges?',
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

    #PHQ-9
    AnswerArrayGUI.append(parserGUI.parse_args().littleInterestInDoingThings)
    AnswerArrayGUI.append(parserGUI.parse_args().feelingDown)
    AnswerArrayGUI.append(parserGUI.parse_args().troubleSleeping)
    AnswerArrayGUI.append(parserGUI.parse_args().feelingTired)
    AnswerArrayGUI.append(parserGUI.parse_args().poorAppetite)
    AnswerArrayGUI.append(parserGUI.parse_args().feelingBadAboutYourself)
    AnswerArrayGUI.append(parserGUI.parse_args().badConcentration)
    AnswerArrayGUI.append(parserGUI.parse_args().speakingSlowORFast)
    AnswerArrayGUI.append(parserGUI.parse_args().hurtingOneself)

    # GAD-7 (Modul of PHQ-D)
    AnswerArrayGUI.append(parserGUI.parse_args().feelingNervous)
    AnswerArrayGUI.append(parserGUI.parse_args().worrying)
    AnswerArrayGUI.append(parserGUI.parse_args().worryingTooMuch)
    AnswerArrayGUI.append(parserGUI.parse_args().troubleRelaxing)
    AnswerArrayGUI.append(parserGUI.parse_args().restless)
    AnswerArrayGUI.append(parserGUI.parse_args().annoyedOrIrritable)
    AnswerArrayGUI.append(parserGUI.parse_args().afraidAwfulHappening)

    # PHQ Stress Modul (Modul of PHQ-D)
    AnswerArrayGUI.append(parserGUI.parse_args().worryAboutHealth)
    AnswerArrayGUI.append(parserGUI.parse_args().weightOrAppearance)
    AnswerArrayGUI.append(parserGUI.parse_args().sexualDesire)
    AnswerArrayGUI.append(parserGUI.parse_args().difficultiesWithSO)
    AnswerArrayGUI.append(parserGUI.parse_args().caregiverBurden)
    AnswerArrayGUI.append(parserGUI.parse_args().stressAtWorkSchool)
    AnswerArrayGUI.append(parserGUI.parse_args().financialProblems)
    AnswerArrayGUI.append(parserGUI.parse_args().noTalkPartner)
    AnswerArrayGUI.append(parserGUI.parse_args().sthBadHappened)
    AnswerArrayGUI.append(parserGUI.parse_args().thoughtsOrDreamsAboutTerribleEvents)

    #Financial Questions
    AnswerArrayGUI.append(parserGUI.parse_args().financialdistress)
    AnswerArrayGUI.append(parserGUI.parse_args().employment)

    # Family/Caretaker Questions
    AnswerArrayGUI.append(parserGUI.parse_args().isCaretaker)
    AnswerArrayGUI.append(parserGUI.parse_args().getsEnoughSupport)
    AnswerArrayGUI.append(parserGUI.parse_args().caringForAdults)
    AnswerArrayGUI.append(parserGUI.parse_args().caringForU18Children)
    AnswerArrayGUI.append(parserGUI.parse_args().caringForDisabledChildren)

    # Leisure Questions
    AnswerArrayGUI.append(parserGUI.parse_args().enoughTimeForOneself)
    AnswerArrayGUI.append(parserGUI.parse_args().leisureTimePlanned)
    AnswerArrayGUI.append(parserGUI.parse_args().leisureTimePlannedExecuted)

    # Social Questions
    AnswerArrayGUI.append(parserGUI.parse_args().anySocialActivities)
    AnswerArrayGUI.append(parserGUI.parse_args().missedOutDueExternalFactors)
    AnswerArrayGUI.append(parserGUI.parse_args().alternativeMeeting)
    AnswerArrayGUI.append(parserGUI.parse_args().stayedOut)
    AnswerArrayGUI.append(parserGUI.parse_args().negativeSocialExchanges)
    AnswerArrayGUI.append(parserGUI.parse_args().resolved)
    AnswerArrayGUI.append(parserGUI.parse_args().futureStrategy)
    AnswerArrayGUI.append(parserGUI.parse_args().sensibleResolvePossible)

    #     # args = parser.parse_args()    #Redo uncomment this to check what input it takes in GUI
    #     # print("Response:", args)      #Redo uncomment this to check what input it takes in GUI
    return AnswerArrayGUI