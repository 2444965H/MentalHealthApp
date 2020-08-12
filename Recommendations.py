"""
Used by KnowledgeEngine.py
"""

financial_advice_1 \
    = "Financial Advice 1: To easen the financial burden lastingly, you could start with basic budgeting! " \
      "https://www.youtube.com/watch?v=sVKQn2I4HDM" #DAS level from 5 to 9

financial_advice_2 \
    = "\n Financial Advice 2: You could also extend your budget: " \
      "By re-negotiating salaries (https://www.youtube.com/watch?v=UTsK8LdDqbU). " \
      "If debt is stressing you out, set course for a long-term Debt Payoff Strategy (https://www.youtube.com/watch?v=jtgnRJKSJlw) " #DAS level from 10 to 14

financial_advice_3 \
    = "\n Financial Advice 3: If you are struggeling heavily with finances, seek out help: " \
      "\n For example, consult with a government-backed financial advice service (https://www.moneyadviceservice.org.uk/en/articles/free-financial-advice-your-options) " #DAS level >=15

financial_advice_4 \
    = "\n Financial Advice 4: If feasible, increase to full-time or take up side-hustles"

financial_advice_5 \
    = "\n Financial Advice 5: Look for side hustles or jobs depending on financial need"

#Specifically for Job-seeking
financial_advice_6 \
    = "\n For the job hunt, get help from family & friends (connecting you to jobs and company hire events), " \
      "as well as government & NGO's (e.g. application courses)"

#Bigger clusters of advices could have sub-clusters as part of them - however, any subsequent changes would mean that
# the coder would have to work on the cluster, its sub-clusters, it sub-sub-clusters, and so on - which is not feasible
financial_advice_cluster_1_2_4_5 \
    = financial_advice_1 + financial_advice_2 + financial_advice_4 + financial_advice_5

financial_advice_cluster_1_3_5_6 \
    = financial_advice_1 + financial_advice_3 + financial_advice_5 + financial_advice_6

financial_advice_cluster_2_3_4_5 \
    = financial_advice_2 + financial_advice_3 + financial_advice_4 + financial_advice_5

financial_advice_cluster_3_4_5 \
    = financial_advice_3 + financial_advice_4 + financial_advice_5

financial_advice_cluster_3_5_6 \
    = financial_advice_3 + financial_advice_5 + financial_advice_6

financial_advice_cluster_2_3_5 \
    = financial_advice_2 + financial_advice_3 + financial_advice_5

financial_advice_cluster_4_5 \
    = financial_advice_4 + financial_advice_5

financial_advice_cluster_1_6 \
    = financial_advice_1 + financial_advice_6

financial_advice_cluster_1_2 \
    = financial_advice_1 + financial_advice_2

#Family Caregiver Advice
caregiver_advice_1 \
    = "\n Caregiver advice 1: To be a caregiver can be mentally and emotionally exhausting. " \
      "If you are overwhelmed, try psychological counseling. " \
      "If you are new to/unsure about caregiving, try a home care guidance session"

caregiver_advice_2 \
    = "\n Caregiver advice 2: Get additional support from family/relatives/spouse (be it physical/mental/emotional) " \
      "to help cope with the caregiving burden short- and long-term."

caregiver_advice_3 \
    = "\n Caregiver advice 3: Get additional support through professionals (e.g. practicioners, social workers)"

caregiver_advice_4 \
    = "\n Caregiver advice 4: Get additional support through organizations (governmental/NGO) that " \
      "help parents of disabled children"

caregiver_advice_5 \
    = "\n Take time for yourself: Have someone else (spouse, babysitter, relatives) take care of the child/children for " \
      "a day so you can relax and recover for a while."

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

#Leisure Advice
leisure_advice_1 \
    = "\n Leisure advice 1: Do not neglect your needs. Schedule some time for yourself (e.g. hobbies, exercise, meditation)."

leisure_advice_2 \
    = "\n If possible, try to fit in some (additional) 'me'-time throughout the day today"

leisure_advice_3 \
    = "\n Safeguard your leisure plans: If you have responsibilities (e.g. work, family), organize substitutes or " \
      "hand-overs. Thus, reducing the risk of being interrupted during your leisure time"

leisure_advice_4 \
    = "\n Emergency 'Leisure' Vacation: For your days off this week, try to focus on satisfying your needs and " \
      "re-prioritize anything that could be postponed"

leisure_advice_5 \
    = "\n "

leisure_advice_cluster_2_3 \
    = leisure_advice_2 + leisure_advice_3

leisure_advice_cluster_3_4 \
    = leisure_advice_2 + leisure_advice_3

leisure_advice_cluster_2_3_4 \
    = leisure_advice_2 + leisure_advice_3 + leisure_advice_4

#Social Advice
social_advice_1 \
    = "\n "

social_advice_2 \
    = "\n "

social_advice_3 \
    = "\n "

social_advice_4 \
    = "\n "

social_advice_5 \
    = "\n "

social_advice_6 \
    = "\n "

social_advice_7 \
    = "\n "

social_advice_8 \
    = "\n "

social_advice_9 \
    = "\n "