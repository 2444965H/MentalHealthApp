from tinydb import TinyDB, Query

# Create path
db = TinyDB('db.json')
DBQuery = Query()


def insertInDB(InputArray):
    dbArray = []
    dbArray = InputArray  # database array is filled with the input given from Parser.py
    # db.upsert: If there are already values, then update db - otherwise insert the new value in empty db.
    db.upsert({'ID': dbArray[0], 'individualDepressionLevel': dbArray[1],
               'individualAnxietyLevel': dbArray[2], 'individualStressLevel': dbArray[3],
               'financialdistress': dbArray[4], 'employment': dbArray[5], 'isCaretaker': dbArray[6],
               'getsEnoughSupport': dbArray[7], 'caringForAdults': dbArray[8],
               'caringForU18Children': dbArray[9], 'caringForDisabledChildren': dbArray[10],
               'enoughTimeForOneself': dbArray[11], 'leisureTimePlanned': dbArray[12],
               'leisureTimePlannedExecuted': dbArray[13], 'anySocialActivities': dbArray[14],
               'missedOutDueExternalFactors': dbArray[15], 'alternativeMeeting': dbArray[16],
               'stayedOut': dbArray[17], 'negativeSocialExchanges': dbArray[18],
               'resolved': dbArray[19], 'futureStrategy': dbArray[20],
               'sensibleResolvePossible': dbArray[21], 'maxIndValueOfDAS': dbArray[22]}, DBQuery.ID == dbArray[0])

    # print(len(db))
    # dbOldArray = db.get(DBQuery.ID == dbArray[0])
    print("New Entry has been entered, old entry has been overwritten")
    print(db.get(DBQuery.ID == dbArray[0]))
    # return dbOldArray


# Called in Parser.py
def checkExistence(username):
    dbExistence = db.get(DBQuery.ID == username)
    return dbExistence


def readFromDB(username):
    dbOldEntry = []
    dbOldQuery = db.get(DBQuery.ID == username)
    dbOldEntry.append(dbOldQuery['ID'])
    dbOldEntry.append(dbOldQuery['individualDepressionLevel'])
    dbOldEntry.append(dbOldQuery['individualAnxietyLevel'])
    dbOldEntry.append(dbOldQuery['individualStressLevel'])
    dbOldEntry.append(dbOldQuery['financialdistress'])
    dbOldEntry.append(dbOldQuery['employment'])
    dbOldEntry.append(dbOldQuery['isCaretaker'])
    dbOldEntry.append(dbOldQuery['getsEnoughSupport'])
    dbOldEntry.append(dbOldQuery['caringForAdults'])
    dbOldEntry.append(dbOldQuery['caringForU18Children'])
    dbOldEntry.append(dbOldQuery['caringForDisabledChildren'])
    dbOldEntry.append(dbOldQuery['enoughTimeForOneself'])
    dbOldEntry.append(dbOldQuery['leisureTimePlanned'])
    dbOldEntry.append(dbOldQuery['leisureTimePlannedExecuted'])
    dbOldEntry.append(dbOldQuery['anySocialActivities'])
    dbOldEntry.append(dbOldQuery['missedOutDueExternalFactors'])
    dbOldEntry.append(dbOldQuery['alternativeMeeting'])
    dbOldEntry.append(dbOldQuery['stayedOut'])
    dbOldEntry.append(dbOldQuery['negativeSocialExchanges'])
    dbOldEntry.append(dbOldQuery['resolved'])
    dbOldEntry.append(dbOldQuery['futureStrategy'])
    dbOldEntry.append(dbOldQuery['sensibleResolvePossible'])
    dbOldEntry.append(dbOldQuery['maxIndValueOfDAS'])

    return dbOldEntry

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
