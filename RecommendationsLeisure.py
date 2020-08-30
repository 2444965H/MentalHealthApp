"""
Used by KnowledgeEngine.py
"""

# Leisure Advice
leisure_advice_1 \
    = "\n Leisure Advice 1: Do not neglect your needs. Schedule some time for yourself " \
      "(e.g. hobbies, exercise, meditation)."

leisure_advice_2 \
    = "\n Leisure Advice 2: If possible, try to fit in some (additional) 'me'-time throughout the day today."

leisure_advice_3 \
    = "\n Leisure Advice 3: Safeguard your leisure plans! If you have responsibilities (e.g. work, family), " \
      "organize substitutes or hand-overs. Thus, reducing the risk of being interrupted during your leisure time."

leisure_advice_4 \
    = "\n Leisure Advice 4: Emergency 'Leisure' Vacation - For your days off this week, try to focus on " \
      "satisfying your needs and re-prioritize anything that could be postponed."

# Bigger clusters of advices could have sub-clusters as part of them - however, any subsequent changes would mean that
# the coder would have to work on the cluster, its sub-clusters, it sub-sub-clusters, and so on - which is not feasible

leisure_advice_cluster_2_3 \
    = leisure_advice_2 + leisure_advice_3

leisure_advice_cluster_3_4 \
    = leisure_advice_3 + leisure_advice_4

leisure_advice_cluster_2_3_4 \
    = leisure_advice_2 + leisure_advice_3 + leisure_advice_4
