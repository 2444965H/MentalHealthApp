"""
Used by KnowledgeEngine.py
"""

financial_advice_1 \
    = "Financial Advice 1: To easen the financial burden lastingly, you could start with basic budgeting! " \
      "(https://www.youtube.com/watch?v=sVKQn2I4HDM)" #DAS level from 5 to 9

financial_advice_2 \
    = "\n Financial Advice 2: You could also extend your budget: " \
      "By re-negotiating salaries (https://www.youtube.com/watch?v=UTsK8LdDqbU). " \
      "If debt is stressing you out, set course for a long-term Debt Payoff Strategy. " \
      "(https://www.youtube.com/watch?v=jtgnRJKSJlw) " #DAS level from 10 to 14

financial_advice_3 \
    = "\n Financial Advice 3: If you are struggeling heavily with finances, seek out help: " \
      "\n For example, consult with a government-backed financial advice service." \
      "(https://www.moneyadviceservice.org.uk/en/articles/free-financial-advice-your-options)" #DAS level >=15

financial_advice_4 \
    = "\n Financial Advice 4: If feasible, increase to full-time or take up side-hustles."

financial_advice_5 \
    = "\n Financial Advice 5: Look for side hustles or jobs depending on financial need."

#Specifically for Job-seeking
financial_advice_6 \
    = "\n Financial Advice 6: For the job hunt, get help from family & friends (for jobs and company hire events), " \
      "as well as government & NGO's (e.g. application courses)."

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
