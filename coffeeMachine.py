import sys

quarterValue = 0.25
dimeValue = 0.10
nickelValue = 0.05
pennyValue = 0.01

MENU = {
    "espresso":{
        "ingredients":{
            "water":50,
            "coffee":18

        },
        "cost":1.5

    },

    "latte":{
        "ingredients":{
            "water":200,
            "milk":150,
            "coffee":24


        },
        "cost":2.5
    },
    "cappuccino":{
        "ingredients":{
            "water":250,
            "milk":100,
            "coffee":24

        },
        "cost":3.0


    }

}

resources = {
    "water":300,
    "milk":200,
    "coffee":100,
    "money":0
}

def main():

    print("Welcome to the Coffee Machine")
    userInput = input("What would you like? (espresso/latte/cappuccino):")
    if userInput in MENU.keys():
        isvalid=True
        if not resources["water"] >= MENU[userInput]["ingredients"]["water"]:
            print("Sorry there is not enough water")
            isvalid=False

        if not resources["coffee"] >= MENU[userInput]["ingredients"]["coffee"]:
           print("Sorry there is not enough coffee")
           isvalid=False

        if not userInput=="espresso":

            if not resources["milk"] >= MENU[userInput]["ingredients"]["milk"]:
               print("Sorry there is not enough milk")
               isvalid=False

        print(f"The cost of {userInput} is ${MENU[userInput]['cost']}")

        if isvalid:
            while True:
                quarterInput = input("How many quarters of coins? :")
                if quarterInput=="":
                    break
                elif  quarterInput.isdigit() :

                    quarterInput = int(quarterInput)
                    print(f" The sum of quarter coins ${quarterInput*quarterValue}")

                    break
                else:
                    print("Invalid input ")

            while True:
                dimeInput = input("How many dimes of coins? :")
                if dimeInput=="":
                    break
                elif dimeInput.isdigit() :
                    dimeInput = int(dimeInput)
                    print(f" The sum of dimes ${dimeInput*dimeValue}")
                    break
                else:
                    print("Invalid input ")
            while True:
                nickelInput = input("How many nickels of coins? :")
                if nickelInput=="":
                    break
                elif nickelInput.isdigit():
                    nickelInput = int(nickelInput)
                    print(f" The sum of nickels ${nickelInput*nickelValue}")
                    break
                else:
                    print("Invalid input ")

            while True:
                pennyInput = input("How many pennies of coins? :")
                if pennyInput=="":
                    break
                elif pennyInput.isdigit():
                    pennyInput = int(pennyInput)
                    print(f" The sum of pennies ${pennyInput*pennyValue}")
                    break
                else:
                    print("Invalid input ")

            if quarterInput=='' and dimeInput=='' and nickelInput=='' and pennyInput=='':
                print("You enter no coins")
            else:
                totalCostCost=0
                if not quarterInput=="":
                    quarterInput = int(quarterInput)
                    totalCostCost += quarterInput*quarterValue

                if not dimeInput=="":

                    dimeInput = int(dimeInput)
                    totalCostCost += dimeInput*dimeValue
                if not nickelInput=="":

                    nickelInput = int(nickelInput)
                    totalCostCost += nickelInput*nickelValue
                if not pennyInput=="":
                    pennyInput = int(pennyInput)
                    totalCostCost += pennyInput*pennyValue


                print(f"Total cost of  coins is ${totalCostCost}")
                if totalCostCost>=MENU[userInput]['cost']:
                    remainder=totalCostCost-MENU[userInput]['cost']
                    if remainder ==0:
                        pass
                    else:
                        print(f"Here is ${totalCostCost - MENU[userInput]['cost']} in change")



                    if resources["water"] >= MENU[userInput]["ingredients"]["water"]:

                        resources["water"] -= MENU[userInput]['ingredients']['water']
                        if resources["coffee"] >= MENU[userInput]["ingredients"]["coffee"]:
                            resources["coffee"] -= MENU[userInput]['ingredients']['coffee']
                            if userInput=="espresso":
                                print(f"Here is your {userInput}. Enjoy!!!")
                                resources['money'] += MENU[userInput]['cost']
                            else:

                                if resources["milk"] >= MENU[userInput]["ingredients"]["milk"]:
                                    resources['milk'] -= MENU[userInput]['ingredients']['milk']
                                    print(f"Here is your {userInput}. Enjoy!!!")
                                    resources['money'] += MENU[userInput]['cost']


                                else:
                                    print("Sorry there is not enough milk")



                        else:
                            pass


                    else:
                        pass




                else:
                    pass

    elif userInput=="off":
        print("Goodbye!")
        sys.exit()

    elif userInput=="report":
        print("---Available Resources---")
        print(f"Water : {resources['water']}ml")
        print(f"Milk  : {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money : ${resources['money']}")
    else:
        print("Invalid input")

while True:
    main()
