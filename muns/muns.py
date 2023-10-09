import json
import time
with open("bankrupt.json") as munFile:
    mainDict = json.load(munFile)


# Warning : json doesnt support int keys

# data format = {availavle balance,}


def cmdGiven(runAmine=False):
    if runAmine:
        print(""" available commands :   \n
                                   1 : muns #check bal, edit
                                   2 : add a purchase #remove a purchase for special input
                                   3 : category #register a purchase to specific category, make new category, delete a category...
                                   9 : \n""")
        runAmine = False

    cmd = input("\n: ")

    def decider():
        if cmd == "0":
            pass

        elif cmd == "1":
            try:
                whatToDo = int(input("enter money to add / subtract : "))
            except ValueError:
                print("enter an integer")
            else:
                mainDict["money"] = mainDict["money"] + whatToDo
                print(f"updated balance to {mainDict['money']}")
            cmdGiven()

        elif cmd == "2":
            try:
                purchased = int(input("Purchase price : "))
                detail = input("context : ")
                if not detail:
                    raise ValueError("No context provided, bad purchase!")
                current_time = time.localtime()
                uniqueID = time.strftime("%y%m%d%H%M%S", current_time)
                timeOfPurchase = time.strftime("%d %b %I:%M%p", current_time)
                if (timeE := input("change time of purchase?")):
                    pass
                print(uniqueID)
                print(timeOfPurchase)

            except ValueError as err:
                print(
                    f"{err if str(err)[:15] != 'invalid literal' else 'Enter an integer !'}")

            cmdGiven()

        elif cmd == "3":

            cmdGiven(runAmine=True)

        else:
            print(" invalid command!\n")
            cmdGiven(runAmine=True)

    decider()


cmdGiven(runAmine=True)

with open("bankrupt.json", mode="w") as heheFile:
    json.dump(mainDict, heheFile)
