import argparse

from experta import Rule, Fact, MATCH, DefFacts
from gooey import Gooey
from gooey import GooeyParser


import SeverityAlgorithm

@Gooey
def guiMakerFinance():
    parser = GooeyParser(description="Check Financials")

    #group1 = parser.add_mutually_exclusive_group()
    #group2 = parser.add_mutually_exclusive_group()
    group1 = parser.add_argument(
        "financialdistress",
        metavar='Are you in financial distress?',
        choices=["yes, I'm in financial distress", "no, I'm not in financial distress"],
        #default="yes, I'm in financial distress" #If you want to have one of  the values as a default value, re-comment this
    )

    group2 = parser.add_argument(
        "employment",
        metavar='Which type of emplyoment do you have?',
        choices=['Full-Time', 'Part-Time', 'On sabbatical - not working by choice', 'Otherwise occupied', 'Job-seeking'])

    #financialdistress = group1.add_argument("-financiallyDistressed", metavar="--yes, I'm in financial distress", action="store_true")
    #financialdistress = group1.add_argument("-notfinanciallyDistressed", metavar="--no, I'm not in financial distress", action="store_true")

    #employment = group2.add_argument("-Full-Time", metavar="--I'm working Full-Time",  action="store_true")
    #employment = group2.add_argument("-Part-Time", metavar="--I'm working Part-Time", action="store_true")

    #parser.
    args = parser.parse_args(args="employment")
    #print("Response:", args) #Redo uncomment this to check what input it takes in GUI
    return args

# def testPrint():
#     parser = GooeyParser


#    parser.add_argument('filename', help="name of the file to process", widget='FileChooser')
#    parser.add_argument("-n", "--nolinenum", action='store_true', help="do not generate line numbers")
#    parser.add_argument("-c", "--comments", action='store_true', help="generate commants")


#guiMakerFinance()

#@Gooey
#def guiMakerFinance2():
    # parser = GooeyParser(description="Check Financials")
    # group = parser.add_mutually_exclusive_group()
    # group.add_argument("-Full-Time", "--I'm working Full-Time", action="store_true")
    # group.add_argument("-Part-Time", "--I'm working Part-Time", action="store_true")
    # args = parser.parse_args()

#guiMakerFinance2()