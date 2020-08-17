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
from experta import *
import MentalProfile
import RecommendationsSocial


class SocialFact(Fact):
    """Info about the social situation: Sub-attributes are "" and ""."""
    pass

class DASLevel(Fact):
    """Info about the depression/anxiety/stress: Sub-attributes are "depression","anxiety", and "stress". """
    pass

#Highest, in other word "max", overall value of all DAS parameters of the indvidiual
maxIndValueOfDAS =  max(MentalProfile.Profile.IndividualDASArray)
maxIndValueOfDASFiveToNine = (maxIndValueOfDAS >=5 and maxIndValueOfDAS <10) #If the highest DAS value is from 5-9
maxIndValueOfDASTenToFourteen = (maxIndValueOfDAS >=10 and maxIndValueOfDAS<15) #If the highest DAS value is from 10-14
maxIndValueOfDASFifteen = (maxIndValueOfDAS >=15) #If the highest DAS value is 15 or higher
individualStressLevel = MentalProfile.Profile.individualStressLevel


class ContextualQuestions(KnowledgeEngine):
#Social Questions: Only dependent on Stress Level, not depending on Depression or Anxiety Level
    #Question 1: Did you participate in any social activities?
    @Rule(SocialFact(anySocialActivities='no, I did not participate in any social activity'),
          SocialFact(missedOutDueExternalFactors='yes, I did miss social activities due to external factors'),
          SocialFact(alternativeMeeting='yes, we did seek out alternatives to meet'))
    # anySocialActivities=no & missedOutDueExternalFactors=yes & alternativeMeeting=yes
    def social_situation_1(self):
        if individualStressLevel >=5:
            print(RecommendationsSocial.social_advice_1)

    @Rule(SocialFact(anySocialActivities='no, I did not participate in any social activity'),
          SocialFact(missedOutDueExternalFactors='yes, I did miss social activities due to external factors'),
          SocialFact(alternativeMeeting='no, we did not seek out alternatives to meet'))
    # anySocialActivities=no & missedOutDueExternalFactors=yes & alternativeMeeting=no
    def social_situation_2(self):
        if individualStressLevel >=5:
            print(RecommendationsSocial.social_advice_2)

    @Rule(SocialFact(anySocialActivities='no, I did not participate in any social activity'),
          SocialFact(missedOutDueExternalFactors='no, I did not miss any social activities due to external factors'),
          SocialFact(stayedOut='yes, I cancelled/stayed out of social meetings'))
    # anySocialActivities=no & missedOutDueExternalFactors=no & stayedOut=yes
    def social_situation_3(self):
        if individualStressLevel >=5 and individualStressLevel <10:
            print(RecommendationsSocial.social_advice_3)
        if individualStressLevel >=10 and individualStressLevel <15:
            print(RecommendationsSocial.social_advice_cluster_3_4)
        if individualStressLevel >=15:
            print(RecommendationsSocial.social_advice_cluster_3_4_5)

    @Rule(SocialFact(anySocialActivities='no, I did not participate in any social activity'),
          SocialFact(missedOutDueExternalFactors='no, I did not miss any social activities due to external factors'),
          SocialFact(stayedOut='no, I did not cancel/stayed out of social meetings'))
    # anySocialActivities=no & missedOutDueExternalFactors=no & stayedOut=no
    def social_situation_4(self):
        if individualStressLevel >=5:
            print(RecommendationsSocial.social_advice_cluster_3_6)

    #Question 2: Did you have any negative  social exchanges?
    @Rule(SocialFact(negativeSocialExchanges='yes, I had negative social exchanges'),
          SocialFact(resolved='yes, I resolved the negative social exchange(s)'),
          SocialFact(futureStrategy='no, I do not have a strategy for negative social exchanges'))
    # negativeSocialExchanges=yes & resolved=yes & futureStrategy=no
    def social_situation_5(self):
        if individualStressLevel >=5:
            print(RecommendationsSocial.social_advice_7)

    @Rule(SocialFact(negativeSocialExchanges='yes, I had negative social exchanges'),
          SocialFact(resolved='no, I did not resolve the negative social exchange(s)'),
          SocialFact(sensibleResolvePossible='yes, I can resolve this matter sensibly'))
    # negativeSocialExchanges=yes & resolved=no & sensibleResolvePossible=yes
    def social_situation_6(self):
        if individualStressLevel >=5:
            print(RecommendationsSocial.social_advice_8)

    @Rule(SocialFact(negativeSocialExchanges='yes, I had negative social exchanges'),
          SocialFact(resolved='no, I did not resolve the negative social exchange(s)'),
          SocialFact(sensibleResolvePossible='no, I cannot resolve this matter sensibly'))
    # negativeSocialExchanges=yes & resolved=no & sensibleResolvePossible=no
    def social_situation_7(self):
        if individualStressLevel >=5:
            print(RecommendationsSocial.social_advice_9)
