
import database

# InputArray = []
# for x in range(0,22):
#     InputArray.append("Yay")
if database.readFromDB("Klaus") is None:
    print("Yay")
print(database.readFromDB("Klaus"))