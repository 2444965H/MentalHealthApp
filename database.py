from tinydb import TinyDB, Query

#Create path
import SeverityAlgorithm
from KnowledgeEngine import individualStressLevel

db = TinyDB('db.json')
DBQuery = Query()

def insertInDB(InputArray):
    dbArray = []
    dbArray = InputArray #database array is filled with the input given from Parser.py
    db.insert({'ID': dbArray[0], 'individualDepressionLevel': dbArray[1],
               'individualAnxietyLevel': dbArray[2], 'individualStressLevel':dbArray[3],
               'financialdistress': dbArray[4], 'employment': dbArray[5], 'isCaretaker': dbArray[6],
               'getsEnoughSupport': dbArray[7], 'caringForAdults': dbArray[8],
               'caringForU18Children': dbArray[9], 'caringForDisabledChildren': dbArray[10],
               'enoughTimeForOneself': dbArray[11], 'leisureTimePlanned': dbArray[12],
               'leisureTimePlannedExecuted': dbArray[13], 'anySocialActivities': dbArray[14],
               'missedOutDueExternalFactors': dbArray[15], 'alternativeMeeting': dbArray[16],
               'stayedOut': dbArray[17], 'negativeSocialExchanges': dbArray[18],
               'resolved': dbArray[19], 'futureStrategy': dbArray[20],
               'sensibleResolvePossible': dbArray[21], 'maxIndValueOfDAS': dbArray[22]})

    print(len(db))
    dbOldArray = db.get(DBQuery.ID == dbArray[0])
    print(db.get(DBQuery.ID == dbArray[0]))
    return dbOldArray

# ID
# individualDepressionLevel
# individualAnxietyLevel
# individualStressLevel
# financialdistress
# employment
# isCaretaker
# getsEnoughSupport
# caringForAdults
# caringForU18Children
# caringForDisabledChildren
# enoughTimeForOneself
# leisureTimePlanned
# leisureTimePlannedExecuted
# anySocialActivities
# missedOutDueExternalFactors
# alternativeMeeting
# stayedOut
# negativeSocialExchanges
# resolved
# futureStrategy
# sensibleResolvePossible

