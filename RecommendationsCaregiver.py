"""
Used by KnowledgeEngine.py
"""

#Family Caregiver Advice
caregiver_advice_1 \
    = "\n Caregiver Advice 1: To be a caregiver can be mentally and emotionally exhausting. " \
      "If you are overwhelmed, try psychological counseling. " \
      "If you are new to/unsure about caregiving, try a home care guidance session."

caregiver_advice_2 \
    = "\n Caregiver Advice 2: Get additional support from family/relatives/spouse (be it physical/mental/emotional) " \
      "to help cope with the caregiving burden short- and long-term."

caregiver_advice_3 \
    = "\n Caregiver Advice 3: Get additional support through professionals (e.g. practicioners, social workers)"

caregiver_advice_4 \
    = "\n Caregiver Advice 4: Get additional support through organizations (governmental/NGO) that " \
      "help parents of disabled children."

caregiver_advice_5 \
    = "\n Caregiver Advice 5: Take time for yourself: Have someone else (spouse, babysitter, relatives) " \
      "take care of the child/children for a day so you can relax and recover for a while."

#Bigger clusters of advices could have sub-clusters as part of them - however, any subsequent changes would mean that
# the coder would have to work on the cluster, its sub-clusters, it sub-sub-clusters, and so on - which is not feasible

caregiver_advice_cluster_1_2 \
    = caregiver_advice_1 + caregiver_advice_2

caregiver_advice_cluster_3_4 \
    = caregiver_advice_3 + caregiver_advice_4

caregiver_advice_cluster_2_5 \
    = caregiver_advice_2 + caregiver_advice_5

caregiver_advice_cluster_1_2_3 \
    = caregiver_advice_1 + caregiver_advice_2 + caregiver_advice_3

caregiver_advice_cluster_1_2_3_4 \
    = caregiver_advice_1 + caregiver_advice_2 + caregiver_advice_3 + caregiver_advice_4