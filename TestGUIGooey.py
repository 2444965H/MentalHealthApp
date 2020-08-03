import argparse

from experta import Rule, Fact, MATCH, DefFacts
from gooey import Gooey
from gooey import GooeyParser


import SeverityAlgorithm

@Gooey
def guiMakerFinance():
    parser = GooeyParser(description="Check Financials")

    group = parser.add_mutually_exclusive_group()
    financialdistress = group.add_argument("-yes", "--yes, I'm in financial distress", action="store_true")
    financialdistress = group.add_argument("-no", "--no, I'm not in financial distress", action="store_true")


    group = parser.add_mutually_exclusive_group()
    employment = group.add_argument("-Full-Time", "--I'm working Full-Time", action="store_true")
    employment = group.add_argument("-Part-Time", "--I'm working Part-Time", action="store_true")
    args = parser.parse_args()
    print("Response:", args)


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