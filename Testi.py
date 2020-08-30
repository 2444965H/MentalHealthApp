
import database
import json

# InputArray = []
# for x in range(0,22):
#     InputArray.append("Yay")
if database.checkExistence("Klaus") is None:
    print("Yay")
else:
    print(database.readFromDB("Klaus"))
if database.checkExistence("John") is None:
    print("Yay")
recordset = database.readFromDB("John")
print(recordset)