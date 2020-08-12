from gooey import Gooey
from gooey import GooeyParser


@Gooey(program_name='PHQ Questions',
       tabbed_groups=True,
       navigation='Tabbed',
       fullscreen=True)
def contextualQuestionsGUI():
    parser = GooeyParser(description="Please go through the 4 tabs and answer the questions")
    AnswerArray = []

#PHQ9 Questions for Depression - Part of PHQ-D
    allPHQ9Questions = parser.add_argument_group('PHQ-9 for Depression') #Groups the Questions in a tab

    interestOrPleasureinDoingThings = allPHQ9Questions.add_argument(
        "littleInterestInDoingThings", #equal to AnswerArray[0]
        metavar='Little interest or pleasure in doing things?',
        choices=["Not at all",
                 "Several days",
                 "More than half the days",
                 "Nearly every day"]
    )

    feelingDown = allPHQ9Questions.add_argument(
        "feelingDown", #equal to AnswerArray[1]
        metavar='Feeling down, depressed, or hopeless?',
        choices=["Not at all",
                 "Several days",
                 "More than half the days",
                 "Nearly every day"]
    )

    troubleSleeping = allPHQ9Questions.add_argument(
        "troubleSleeping", #equal to AnswerArray[2]
        metavar='Trouble falling or staying asleep, or sleeping too much',
        choices=["Not at all",
                 "Several days",
                 "More than half the days",
                 "Nearly every day"]
    )

    feelingTired = allPHQ9Questions.add_argument(
        "feelingTired", #equal to AnswerArray[3]
        metavar='Feeling tired or having little energy',
        choices=["Not at all",
                 "Several days",
                 "More than half the days",
                 "Nearly every day"]
    )

    poorAppetite = allPHQ9Questions.add_argument(
        "poorAppetite", #equal to AnswerArray[4]
        metavar='Poor apppetite or overeating',
        choices=["Not at all",
                 "Several days",
                 "More than half the days",
                 "Nearly every day"]
    )

    feelingBadAboutYourself = allPHQ9Questions.add_argument(
        "feelingBadAboutYourself", #equal to AnswerArray[5]
        metavar='Feeling bad about yourself - or that you are a failure or have let yourself or your family down',
        choices=["Not at all",
                 "Several days",
                 "More than half the days",
                 "Nearly every day"]
    )

    badConcentration = allPHQ9Questions.add_argument(
        "badConcentration", #equal to AnswerArray[6]
        metavar='Trouble concentrating on things, such as reading the newspaper or watching television',
        choices=["Not at all",
                 "Several days",
                 "More than half the days",
                 "Nearly every day"]
    )

    speakingSlowORFast = allPHQ9Questions.add_argument(
        "speakingSlowORFast", #equal to AnswerArray[7]
        metavar='Moving or speaking so slowly that other people could have noticed? Or the opposite - being so fidgety or restless that you have been moving around a lot more than usual',
        choices=["Not at all",
                 "Several days",
                 "More than half the days",
                 "Nearly every day"]
    )
    allGAD7Questions = parser.add_argument_group('GAD-7 for Anxiety')

    feelingNervous = allGAD7Questions.add_argument(
        "feelingNervous", #equal to AnswerArray[0]
        metavar='Feeling nervous, anxious or on edge?',
        choices=["Not at all",
                 "Several days",
                 "More than half the days",
                 "Nearly every day"]
    )

    hurtingOneself = allPHQ9Questions.add_argument(
        "hurtingOneself", #equal to AnswerArray[8]
        metavar='Thoughts that you would be better off dead or of hurting yourself in some way',
        choices=["Not at all",
                 "Several days",
                 "More than half the days",
                 "Nearly every day"]
    )

#GAD-7 (Modul of PHQ-D)

    worrying = allGAD7Questions.add_argument(
        "worrying", #equal to AnswerArray[1]
        metavar='Not being able to stop or control worrying?',
        choices=["Not at all",
                 "Several days",
                 "More than half the days",
                 "Nearly every day"]
    )

    feelingNervous = allGAD7Questions.add_argument(
        "feelingNervous",
        metavar='Feeling nervous, anxious or on edge?',
        choices=["Not at all",
                 "Several days",
                 "More than half the days",
                 "Nearly every day"]
    )

    feelingNervous = allGAD7Questions.add_argument(
        "feelingNervous",
        metavar='Feeling nervous, anxious or on edge?',
        choices=["Not at all",
                 "Several days",
                 "More than half the days",
                 "Nearly every day"]
    )

    feelingNervous = allGAD7Questions.add_argument(
        "feelingNervous",
        metavar='Feeling nervous, anxious or on edge?',
        choices=["Not at all",
                 "Several days",
                 "More than half the days",
                 "Nearly every day"]
    )

    feelingNervous = allGAD7Questions.add_argument(
        "feelingNervous",
        metavar='Feeling nervous, anxious or on edge?',
        choices=["Not at all",
                 "Several days",
                 "More than half the days",
                 "Nearly every day"]
    )

    feelingNervous = allGAD7Questions.add_argument(
        "feelingNervous",
        metavar='Feeling nervous, anxious or on edge?',
        choices=["Not at all",
                 "Several days",
                 "More than half the days",
                 "Nearly every day"]
    )

#PHQ-Stress Modul (Modul of PHQ-D - from the questions 12a-12j)

    allPHQStressQuestions = parser.add_argument_group('PHQ-Stress Modul for Stress')

    worryAboutHealth = allPHQStressQuestions.add_argument(
        "worryAboutHealth", #equal to AnswerArray[0]
        metavar='Worry about your health',
        choices=["Not affected",
                 "Little affected",
                 "Severely affected"]
    )

    weightOrAppearance = allPHQStressQuestions.add_argument(
        "weightOrAppearance", #equal to AnswerArray[1]
        metavar='Your weight or your appearance',
        choices=["Not affected",
                 "Little affected",
                 "Severely affected"]
    )

    sexualDesire = allPHQStressQuestions.add_argument(
        "sexualDesire", #equal to AnswerArray[2]
        metavar='Little or no sexual desire or pleasure during intercourse',
        choices=["Not affected",
                 "Little affected",
                 "Severely affected"]
    )

    difficultiesWithSO = allPHQStressQuestions.add_argument(
        "difficultiesWithSO", #equal to AnswerArray[3]
        metavar='Difficulties with the spouse, significant other, girlfriend / boyfriend',
        choices=["Not affected",
                 "Little affected",
                 "Severely affected"]
    )

    caregiverBurden = allPHQStressQuestions.add_argument(
        "caregiverBurden", #equal to AnswerArray[4]
        metavar='Burden of caring for children, parents, or other family members',
        choices=["Not affected",
                 "Little affected",
                 "Severely affected"]
    )

    stressAtWorkSchool= allPHQStressQuestions.add_argument(
        "stressAtWorkSchool", #equal to AnswerArray[5]
        metavar='Stress at work or at school',
        choices=["Not affected",
                 "Little affected",
                 "Severely affected"]
    )

    financialProblems= allPHQStressQuestions.add_argument(
        "financialProblems", #equal to AnswerArray[6]
        metavar='Financial problems or concerns',
        choices=["Not affected",
                 "Little affected",
                 "Severely affected"]
    )

    noTalkPartner= allPHQStressQuestions.add_argument(
        "noTalkPartner", #equal to AnswerArray[7]
        metavar='Not having someone to talk to about problems',
        choices=["Not affected",
                 "Little affected",
                 "Severely affected"]
    )

    sthBadHappened= allPHQStressQuestions.add_argument(
        "sthBadHappened", #equal to AnswerArray[8]
        metavar='Something bad that happened recently',
        choices=["Not affected",
                 "Little affected",
                 "Severely affected"]
    )

    thoughtsOrDreamsAboutTerribleEvents= allPHQStressQuestions.add_argument(
        "thoughtsOrDreamsAboutTerribleEvents", #equal to AnswerArray[9]
        metavar='Thoughts about terrible events from earlier or dreams about it - e.g. the destruction of your own home, a serious accident, a robbery, physical violence or a forced sexual act',
        choices=["Not affected",
                 "Little affected",
                 "Severely affected"]
    )