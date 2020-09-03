from tinydb import TinyDB, Query

# Create path
db = TinyDB('db.json')
DBQuery = Query()


def insert_in_db(input_array):
    db_array = []
    db_array = input_array  # database array is filled with the input given from Parser.py
    # db.upsert: If there are already values, then update db - otherwise insert the new value in empty db.
    db.upsert({'ID': db_array[0], 'individualDepressionLevel': db_array[1],
               'individualAnxietyLevel': db_array[2], 'individualStressLevel': db_array[3],
               'financialdistress': db_array[4], 'employment': db_array[5], 'isCaretaker': db_array[6],
               'getsEnoughSupport': db_array[7], 'caringForAdults': db_array[8],
               'caringForU18Children': db_array[9], 'caringForDisabledChildren': db_array[10],
               'enoughTimeForOneself': db_array[11], 'leisureTimePlanned': db_array[12],
               'leisureTimePlannedExecuted': db_array[13], 'anySocialActivities': db_array[14],
               'missedOutDueExternalFactors': db_array[15], 'alternativeMeeting': db_array[16],
               'stayedOut': db_array[17], 'negativeSocialExchanges': db_array[18],
               'resolved': db_array[19], 'futureStrategy': db_array[20],
               'sensibleResolvePossible': db_array[21], 'maxIndValueOfDAS': db_array[22]}, DBQuery.ID == db_array[0])

    # print(len(db))
    # dbOldArray = db.get(DBQuery.ID == db_array[0])
    print("New Entry has been entered, old entry has been overwritten")
    print(db.get(DBQuery.ID == db_array[0]))
    # return dbOldArray


# Called in Parser.py
def check_existence(username):
    db_existence = db.get(DBQuery.ID == username)
    return db_existence


def read_from_db(username):
    db_old_entry = []
    db_old_query = db.get(DBQuery.ID == username)
    db_old_entry.append(db_old_query['ID'])
    db_old_entry.append(db_old_query['individualDepressionLevel'])
    db_old_entry.append(db_old_query['individualAnxietyLevel'])
    db_old_entry.append(db_old_query['individualStressLevel'])
    db_old_entry.append(db_old_query['financialdistress'])
    db_old_entry.append(db_old_query['employment'])
    db_old_entry.append(db_old_query['isCaretaker'])
    db_old_entry.append(db_old_query['getsEnoughSupport'])
    db_old_entry.append(db_old_query['caringForAdults'])
    db_old_entry.append(db_old_query['caringForU18Children'])
    db_old_entry.append(db_old_query['caringForDisabledChildren'])
    db_old_entry.append(db_old_query['enoughTimeForOneself'])
    db_old_entry.append(db_old_query['leisureTimePlanned'])
    db_old_entry.append(db_old_query['leisureTimePlannedExecuted'])
    db_old_entry.append(db_old_query['anySocialActivities'])
    db_old_entry.append(db_old_query['missedOutDueExternalFactors'])
    db_old_entry.append(db_old_query['alternativeMeeting'])
    db_old_entry.append(db_old_query['stayedOut'])
    db_old_entry.append(db_old_query['negativeSocialExchanges'])
    db_old_entry.append(db_old_query['resolved'])
    db_old_entry.append(db_old_query['futureStrategy'])
    db_old_entry.append(db_old_query['sensibleResolvePossible'])
    db_old_entry.append(db_old_query['maxIndValueOfDAS'])
    return db_old_entry

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
