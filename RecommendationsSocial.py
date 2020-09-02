"""
Used by KnowledgeEngine.py
"""

# Social Advice
social_advice_1 \
    = "\n Social Advice 1: If it is sensibly possible, try to meet in person again to do social activities together."

social_advice_2 \
    = "\n Social Advice 2: Propose alternate ways to meet, e.g. video/phone call."

social_advice_3 \
    = "\n Social Advice 3: Try to socialize again! Though initially exhausting, it benefits your mental health."

social_advice_4 \
    = "\n Social Advice 4: If you are considerably stressed, you could confide your problems to people close to you." \
      "Don't bottle up your problems or emotions."

social_advice_5 \
    = "\n Social Advice 5: If your high stress level persists for a longer time, " \
      "professional help may support you to find more effective strategies."

social_advice_6 \
    = "\n Social Advice 6: Look if you can join friends or make new ones - by joining hobby or interest groups."

social_advice_7 \
    = "\n Social Advice 7: When you are ready, try to analyze the situation and " \
      "develop a strategy to deal with those exchanges."

social_advice_8 \
    = "\n Social Advice 8: Depending on the situation, try to resolve the negative social exchange with that person."

social_advice_9 \
    = "\n Social Advice 9: Practicing meditation and mindfulness can help you let go this situation " \
      "so that it burdens you less."

# Bigger clusters of advices could have sub-clusters as part of them - however, any subsequent changes would mean that
# the coder would have to work on the cluster, its sub-clusters, it sub-sub-clusters, and so on - which is not feasible

social_advice_cluster_3_4 \
    = social_advice_3 + social_advice_4 + "\n"

social_advice_cluster_3_6 \
    = social_advice_3 + social_advice_6 + "\n"

social_advice_cluster_3_4_5 \
    = social_advice_3 + social_advice_4 + social_advice_5 + "\n"
