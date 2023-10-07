import json
with open("bankrupt.json") as munFile:
    mainDict = json.load(munFile)


# def io(textOut: str, newline: bool = True) -> str:
#     pass


runAmine = True
# data format = {availavle balance,}


def cmdGiven():
    global runAmine
    if runAmine:
        print(""" available commands :   \n
                                   1 : edit muns
                                   2 : add a purchase
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
            pass

        else:
            print("invalid command!")
            cmdGiven()

    decider()


cmdGiven()

with open("bankrupt.json", mode="w") as heheFile:
    json.dump(mainDict, heheFile)
