from gooey import Gooey
from gooey import GooeyParser


@Gooey(program_name='Complete Questionnaire',
       tabbed_groups=True,
       navigation='Tabbed',
       fullscreen=True)
def questions_for_gui_phq():
    parser_gui = GooeyParser(description="Please go through all 7 tabs and answer the questions. \n"
                                         "Over the last 2-4 weeks, how often have you been bothered by any of the "
                                         "following problems?")
    answer_array_gui = []

    # PHQ9 Questions for Depression - Part of PHQ-D
    all_phq9_questions = parser_gui.add_argument_group('PHQ-9 for Depression')  # Groups the Questions in a tab

    interest_or_pleasure_in_doing_things = all_phq9_questions.add_argument(
        "littleInterestInDoingThings",  # equal to AnswerArrayPHQ[0]
        metavar='Little interest or pleasure in doing things?',
        choices=["Not at all",
                 "Several days",
                 "More than half the days",
                 "Nearly every day"]
    )

    feeling_down = all_phq9_questions.add_argument(
        "feelingDown",  # equal to AnswerArrayPHQ[1]
        metavar='Feeling down, depressed, or hopeless?',
        choices=["Not at all",
                 "Several days",
                 "More than half the days",
                 "Nearly every day"]
    )

    trouble_sleeping = all_phq9_questions.add_argument(
        "troubleSleeping",  # equal to AnswerArrayPHQ[2]
        metavar='Trouble falling or staying asleep, or sleeping too much?',
        choices=["Not at all",
                 "Several days",
                 "More than half the days",
                 "Nearly every day"]
    )

    feeling_tired = all_phq9_questions.add_argument(
        "feelingTired",  # equal to AnswerArrayPHQ[3]
        metavar='Feeling tired or having little energy?',
        choices=["Not at all",
                 "Several days",
                 "More than half the days",
                 "Nearly every day"]
    )

    poor_appetite = all_phq9_questions.add_argument(
        "poorAppetite",  # equal to AnswerArrayPHQ[4]
        metavar='Poor appetite or overeating?',
        choices=["Not at all",
                 "Several days",
                 "More than half the days",
                 "Nearly every day"]
    )

    feeling_bad_about_yourself = all_phq9_questions.add_argument(
        "feelingBadAboutYourself",  # equal to AnswerArrayPHQ[5]
        metavar='Feeling bad about yourself - or that you are a failure or have let yourself or your family down?',
        choices=["Not at all",
                 "Several days",
                 "More than half the days",
                 "Nearly every day"]
    )

    bad_concentration = all_phq9_questions.add_argument(
        "badConcentration",  # equal to AnswerArrayPHQ[6]
        metavar='Trouble concentrating on things, such as reading the newspaper or watching television?',
        choices=["Not at all",
                 "Several days",
                 "More than half the days",
                 "Nearly every day"]
    )

    speaking_slow_or_fast = all_phq9_questions.add_argument(
        "speakingSlowORFast",  # equal to AnswerArrayPHQ[7]
        metavar='Moving/Speaking so slowly OR being restless that others have noticed?',
        # 'Moving or speaking so slowly that other people could have noticed?
        # Or the opposite - being so fidgety or restless that you have been moving around a lot more than usual',
        choices=["Not at all",
                 "Several days",
                 "More than half the days",
                 "Nearly every day"]
    )

    hurting_oneself = all_phq9_questions.add_argument(
        "hurtingOneself",  # equal to AnswerArrayPHQ[8]
        metavar='Thoughts that you would be better off dead or of hurting yourself in some way?',
        choices=["Not at all",
                 "Several days",
                 "More than half the days",
                 "Nearly every day"]
    )

    # GAD-7 (Module of PHQ-D)
    allGAD7Questions = parser_gui.add_argument_group('GAD-7 for Anxiety')

    feeling_nervous = allGAD7Questions.add_argument(
        "feelingNervous",  # equal to AnswerArrayPHQ[0]
        metavar='Feeling nervous, anxious or on edge?',
        choices=["Not at all",
                 "Several days",
                 "More than half the days",
                 "Nearly every day"]
    )

    worrying = allGAD7Questions.add_argument(
        "worrying",  # equal to AnswerArrayPHQ[1]
        metavar='Not being able to stop or control worrying?',
        choices=["Not at all",
                 "Several days",
                 "More than half the days",
                 "Nearly every day"]
    )

    worrying_too_much = allGAD7Questions.add_argument(
        "worryingTooMuch",
        metavar='Worrying too much about different things?',
        choices=["Not at all",
                 "Several days",
                 "More than half the days",
                 "Nearly every day"]
    )

    trouble_relaxing = allGAD7Questions.add_argument(
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

    annoyed_or_irritable = allGAD7Questions.add_argument(
        "annoyedOrIrritable",
        metavar='Becoming easily annoyed or irritable?',
        choices=["Not at all",
                 "Several days",
                 "More than half the days",
                 "Nearly every day"]
    )

    afraid_awful_happening = allGAD7Questions.add_argument(
        "afraidAwfulHappening",
        metavar='Feeling afraid as if something awful might happen?',
        choices=["Not at all",
                 "Several days",
                 "More than half the days",
                 "Nearly every day"]
    )

    # PHQ-Stress Module (Module of PHQ-D - from the questions 12a-12j)

    allPHQStressQuestions = parser_gui.add_argument_group('PHQ-Stress Module for Stress')

    worry_about_health = allPHQStressQuestions.add_argument(
        "worryAboutHealth",  # equal to AnswerArrayPHQ[0]
        metavar='Worry about your health',
        choices=["Not affected",
                 "Little affected",
                 "Severely affected"]
    )

    weight_or_appearance = allPHQStressQuestions.add_argument(
        "weightOrAppearance",  # equal to AnswerArrayPHQ[1]
        metavar='Your weight or your appearance',
        choices=["Not affected",
                 "Little affected",
                 "Severely affected"]
    )

    sexual_desire = allPHQStressQuestions.add_argument(
        "sexualDesire",  # equal to AnswerArrayPHQ[2]
        metavar='Little or no sexual desire or pleasure during intercourse',
        choices=["Not affected",
                 "Little affected",
                 "Severely affected"]
    )

    difficulties_with_so = allPHQStressQuestions.add_argument(
        "difficultiesWithSO",  # equal to AnswerArrayPHQ[3]
        metavar='Difficulties with the spouse, significant other, girlfriend / boyfriend',
        choices=["Not affected",
                 "Little affected",
                 "Severely affected"]
    )

    caregiver_burden = allPHQStressQuestions.add_argument(
        "caregiverBurden",  # equal to AnswerArrayPHQ[4]
        metavar='Burden of caring for children, parents, or other family members',
        choices=["Not affected",
                 "Little affected",
                 "Severely affected"]
    )

    stress_at_work_school = allPHQStressQuestions.add_argument(
        "stressAtWorkSchool",  # equal to AnswerArrayPHQ[5]
        metavar='Stress at work or at school',
        choices=["Not affected",
                 "Little affected",
                 "Severely affected"]
    )

    financial_problems = allPHQStressQuestions.add_argument(
        "financialProblems",  # equal to AnswerArrayPHQ[6]
        metavar='Financial problems or concerns',
        choices=["Not affected",
                 "Little affected",
                 "Severely affected"]
    )

    no_talk_partner = allPHQStressQuestions.add_argument(
        "noTalkPartner",  # equal to AnswerArrayPHQ[7]
        metavar='Not having someone to talk to about problems',
        choices=["Not affected",
                 "Little affected",
                 "Severely affected"]
    )

    sth_bad_happened = allPHQStressQuestions.add_argument(
        "sthBadHappened",  # equal to AnswerArrayPHQ[8]
        metavar='Something bad that happened recently',
        choices=["Not affected",
                 "Little affected",
                 "Severely affected"]
    )

    thoughts_or_dreams_about_terrible_events = allPHQStressQuestions.add_argument(
        "thoughtsOrDreamsAboutTerribleEvents",  # equal to AnswerArrayPHQ[9]
        metavar='Thoughts about terrible events from earlier or dreams about it',
        # ' - e.g. the destruction of your own home, a serious accident,
        # a robbery, physical violence or a forced sexual act',
        choices=["Not affected",
                 "Little affected",
                 "Severely affected"]
    )

    # Financial Questions
    all_financial_questions = parser_gui.add_argument_group(
        'Financial')  # Groups the questions in a tab and gives them a name

    financial_question_financial_distress = all_financial_questions.add_argument(
        "financialdistress",  # equal to AnswerArray[0]
        metavar='Are you in financial distress?',
        choices=["Yes, I am in financial distress",
                 "No, I am not in financial distress"]
        # default="yes, I'm in financial distress"
        # If you want to have one of the values as a default value, re-comment the line above
    )

    financial_question_employment = all_financial_questions.add_argument(
        "employment",  # equal to AnswerArray[1]
        metavar='What is your employment situation?',
        choices=['Full-Time',
                 'Part-Time',
                 'On sabbatical - not working by choice',
                 'Otherwise occupied',
                 'Job-seeking']
    )

    # Family Questions
    all_family_questions = parser_gui.add_argument_group('Family')
    # Groups the questions in a tab and gives them a name

    family_question_caretaker = all_family_questions.add_argument(
        "isCaretaker",  # equal to AnswerArray[2]
        metavar='Are you taking care of any family members (e.g. children, elderly)?',
        choices=['Yes, I am a caregiver',
                 'No, I am not a caregiver'],
    )

    family_question_enough_support = all_family_questions.add_argument(
        "getsEnoughSupport",  # equal to AnswerArray[3]
        metavar='Do you have/get enough support as a caregiver? E.g. from partner, social workers?',
        choices=['Yes, I have enough support',
                 'No, I have not enough support',
                 'Not applicable - not a caregiver']
    )

    family_question_caring_for_adults = all_family_questions.add_argument(
        "caringForAdults",  # equal to AnswerArray[4]
        metavar='Are you a caregiver for an adult?',
        choices=['Yes, I am a caregiver for an adult',
                 'No, I am not a caregiver for an adult',
                 'Not applicable - not a caregiver']
    )

    family_question_caring_for_children_u18 = all_family_questions.add_argument(
        "caringForU18Children",  # equal to AnswerArray[5]
        metavar='Are you a caregiver for any children under 18?',
        choices=['Yes, I am a caregiver for at least one child under 18',
                 'No, I am not a caregiver for child/children under 18',
                 'Not applicable - not a caregiver']
    )

    family_question_caring_for_disabled_children = all_family_questions.add_argument(
        "caringForDisabledChildren",  # equal to AnswerArray[6]
        metavar='Are you a caregiver for a disabled child?',
        choices=['Yes, I am a caregiver for at least one disabled child',
                 'No, I am not a caregiver for at least one disabled child',
                 'Not applicable - not a caregiver']
    )

    # Leisure Questions
    all_leisure_questions = parser_gui.add_argument_group('Leisure')

    leisure_question_enough_time_for_oneself = all_leisure_questions.add_argument(
        "enoughTimeForOneself",
        metavar='Did you spend enough leisure time on yourself?',
        choices=['Yes, I had enough leisure time for myself',
                 'No, I did not have enough leisure time for myself']
    )

    leisure_question_off_time_planned = all_leisure_questions.add_argument(
        "leisureTimePlanned",
        metavar='Did you plan to take off some time for leisure?',
        choices=['Yes, I planned/am planning to take off time for leisure',
                 'No, I did/am not planning to take off time for leisure']
    )

    leisure_question_leisure_time_planned_executed = all_leisure_questions.add_argument(
        "leisureTimePlannedExecuted",
        metavar='Were you able to execute your leisure/hobbies like you planned?',
        choices=['Yes, I had leisure time like planned',
                 'No, I was not able to take leisure time like planned']
    )

    # Social Questions
    all_social_questions = parser_gui.add_argument_group('Social')  # Groups the questions in a tab and gives them a name

    social_question_any_social_activities = all_social_questions.add_argument(
        "anySocialActivities",
        metavar='Did you participate in any social activities?',
        choices=["Yes, I participated in social activities",
                 "No, I did not participate in any social activity"]
    )

    social_question_missed_out_due_external_factors = all_social_questions.add_argument(
        "missedOutDueExternalFactors",
        metavar='Did you miss out on social activities due to other responsibilities or ext. factors?',
        choices=["Yes, I did miss social activities due to external factors",
                 "No, I did not miss any social activities due to external factors"]
    )

    social_question_alternative_meeting = all_social_questions.add_argument(
        "alternativeMeeting",
        metavar='Did you seek out alternatives for the meeting?',
        choices=["Yes, we did seek out alternatives to meet",
                 "No, we did not seek out alternatives to meet"]
    )

    social_question_stayed_out = all_social_questions.add_argument(
        "stayedOut",
        metavar='Did you cancel plans you had with other or stayed out of any social meeting',
        choices=["Yes, I cancelled/stayed out of social meetings",
                 "No, I did not cancel/stayed out of social meetings"]
    )

    social_question_negative_exchanges = all_social_questions.add_argument(
        "negativeSocialExchanges",
        metavar='Did you have any negative social exchanges?',
        choices=['Yes, I had negative social exchanges',
                 'No, I did not have any negative social exchanges']
    )

    social_question_resolved = all_social_questions.add_argument(
        "resolved",
        metavar='Did you resolve the negative social exchanges?',
        choices=['Yes, I resolved the negative social exchange(s)',
                 'No, I did not resolve the negative social exchange(s)']
    )

    social_question_future_strategy = all_social_questions.add_argument(
        "futureStrategy",
        metavar='Do you have a strategy on how to deal with those kinds of negative social exchanges in the future?',
        choices=['Yes, I have a negative social exchange strategy',
                 'No, I do not have a strategy for negative social exchanges']
    )

    social_question_sensible_resolve_possible = all_social_questions.add_argument(
        "sensibleResolvePossible",
        metavar='Do you have the possibility to resolve this matter sensibly?',
        choices=['Yes, I can resolve this matter sensibly',
                 'No, I cannot resolve this matter sensibly']
    )

    # PHQ-9
    answer_array_gui.append(parser_gui.parse_args().littleInterestInDoingThings)
    answer_array_gui.append(parser_gui.parse_args().feelingDown)
    answer_array_gui.append(parser_gui.parse_args().troubleSleeping)
    answer_array_gui.append(parser_gui.parse_args().feelingTired)
    answer_array_gui.append(parser_gui.parse_args().poorAppetite)
    answer_array_gui.append(parser_gui.parse_args().feelingBadAboutYourself)
    answer_array_gui.append(parser_gui.parse_args().badConcentration)
    answer_array_gui.append(parser_gui.parse_args().speakingSlowORFast)
    answer_array_gui.append(parser_gui.parse_args().hurtingOneself)

    # GAD-7 (Module of PHQ-D)
    answer_array_gui.append(parser_gui.parse_args().feelingNervous)
    answer_array_gui.append(parser_gui.parse_args().worrying)
    answer_array_gui.append(parser_gui.parse_args().worryingTooMuch)
    answer_array_gui.append(parser_gui.parse_args().troubleRelaxing)
    answer_array_gui.append(parser_gui.parse_args().restless)
    answer_array_gui.append(parser_gui.parse_args().annoyedOrIrritable)
    answer_array_gui.append(parser_gui.parse_args().afraidAwfulHappening)

    # PHQ Stress Module (Module of PHQ-D)
    answer_array_gui.append(parser_gui.parse_args().worryAboutHealth)
    answer_array_gui.append(parser_gui.parse_args().weightOrAppearance)
    answer_array_gui.append(parser_gui.parse_args().sexualDesire)
    answer_array_gui.append(parser_gui.parse_args().difficultiesWithSO)
    answer_array_gui.append(parser_gui.parse_args().caregiverBurden)
    answer_array_gui.append(parser_gui.parse_args().stressAtWorkSchool)
    answer_array_gui.append(parser_gui.parse_args().financialProblems)
    answer_array_gui.append(parser_gui.parse_args().noTalkPartner)
    answer_array_gui.append(parser_gui.parse_args().sthBadHappened)
    answer_array_gui.append(parser_gui.parse_args().thoughtsOrDreamsAboutTerribleEvents)

    # Financial Questions
    answer_array_gui.append(parser_gui.parse_args().financialdistress)
    answer_array_gui.append(parser_gui.parse_args().employment)

    # Family/Caretaker Questions
    answer_array_gui.append(parser_gui.parse_args().isCaretaker)
    answer_array_gui.append(parser_gui.parse_args().getsEnoughSupport)
    answer_array_gui.append(parser_gui.parse_args().caringForAdults)
    answer_array_gui.append(parser_gui.parse_args().caringForU18Children)
    answer_array_gui.append(parser_gui.parse_args().caringForDisabledChildren)

    # Leisure Questions
    answer_array_gui.append(parser_gui.parse_args().enoughTimeForOneself)
    answer_array_gui.append(parser_gui.parse_args().leisureTimePlanned)
    answer_array_gui.append(parser_gui.parse_args().leisureTimePlannedExecuted)

    # Social Questions
    answer_array_gui.append(parser_gui.parse_args().anySocialActivities)
    answer_array_gui.append(parser_gui.parse_args().missedOutDueExternalFactors)
    answer_array_gui.append(parser_gui.parse_args().alternativeMeeting)
    answer_array_gui.append(parser_gui.parse_args().stayedOut)
    answer_array_gui.append(parser_gui.parse_args().negativeSocialExchanges)
    answer_array_gui.append(parser_gui.parse_args().resolved)
    answer_array_gui.append(parser_gui.parse_args().futureStrategy)
    answer_array_gui.append(parser_gui.parse_args().sensibleResolvePossible)

    #     # args = parser.parse_args()    #Redo uncomment this to check what input it takes in GUI
    #     # print("Response:", args)      #Redo uncomment this to check what input it takes in GUI
    return answer_array_gui
