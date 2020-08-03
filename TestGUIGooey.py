import argparse
from experta import Rule, Fact, MATCH, DefFacts
from gooey import Gooey
from gooey import GooeyParser
from wx.lib.agw.buttonpanel import BPArt

import SeverityAlgorithm

@Gooey
def guiMakerFinance():
    parser = GooeyParser(description="Check Financials")

    #group1 = parser.add_mutually_exclusive_group()
    #group2 = parser.add_mutually_exclusive_group()
    group1 = parser.add_argument(
        "financialdistress",
        metavar='Are you in financial distress?',
        choices=["yes, I'm in financial distress",
                 "no, I'm not in financial distress"]
        #default="yes, I'm in financial distress" #If you want to have one of  the values as a default value, re-comment this
    )

    group2 = parser.add_argument(
        "employment",
        metavar='Which type of employment do you have?',
        choices=['Full-Time',
                 'Part-Time',
                 'On sabbatical - not working by choice',
                 'Otherwise occupied',
                 'Job-seeking'
                 ]
    )

    #financialdistress = group1.add_argument("-financiallyDistressed", metavar="--yes, I'm in financial distress", action="store_true")
    #financialdistress = group1.add_argument("-notfinanciallyDistressed", metavar="--no, I'm not in financial distress", action="store_true")

    #employment = group2.add_argument("-Full-Time", metavar="--I'm working Full-Time",  action="store_true")
    #employment = group2.add_argument("-Part-Time", metavar="--I'm working Part-Time", action="store_true")

    #parser=
    AnswerArray = []
    AnswerArray.append(parser.parse_args().financialdistress)
    AnswerArray.append(parser.parse_args().employment)
    #args = parser.parse_args()
    #print("Response:", args) #Redo uncomment this to check what input it takes in GUI
    return AnswerArray

#    parser.add_argument('filename', help="name of the file to process", widget='FileChooser')
#    parser.add_argument("-n", "--nolinenum", action='store_true', help="do not generate line numbers")
#    parser.add_argument("-c", "--comments", action='store_true', help="generate commants")


#@Gooey
#def guiMakerFinance2():
    # parser = GooeyParser(description="Check Financials")
    # group = parser.add_mutually_exclusive_group()
    # group.add_argument("-Full-Time", "--I'm working Full-Time", action="store_true")
    # group.add_argument("-Part-Time", "--I'm working Part-Time", action="store_true")
    # args = parser.parse_args()