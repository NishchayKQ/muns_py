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
                # 2301021210
                timeOfPurchase = time.strftime("%d %b %I:%M%p", current_time)

                if (timeE := input("""change time of purchase?
                                   format: <date><hrs><mins><am> \ <month><date>...
                                   : """)):
                    if len(timeE) % 2 != 0:
                        raise ValueError(
                            "Please enter 01 not 1 for dates and months")
                    # 12 is length of timeOfPurchase
                    temp = 12-len(timeE)
                    timeOfPurchase = uniqueID[:temp] + timeE
                    current_time = time.strptime(
                        timeOfPurchase, "%y%m%d%I%M%p")

                print(uniqueID)
                print(timeOfPurchase)
                print(current_time)

            except ValueError as err:
                print(
                    f"{'Enter an integer !' if str(err)[:15] == 'invalid literal' else( 'invalid time format entered, ' + str(err) if str(err)[:9] == 'time data' else err) }")

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
