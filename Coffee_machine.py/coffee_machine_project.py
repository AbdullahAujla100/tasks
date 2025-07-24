Menu= {
        "espresso":{
            "ingrediants":{
                "water":20,
                "milk":5,
                "coffee":10,
            },
            "cost": 100,

        },
        "latte":{
            "ingrediants":{
                "water":25,
                "milk":10,
                "coffee":15,
            },
            "cost": 80,

        },
        "cappuccino":{
            "ingrediants":{                           
                "water":35,
                "milk":27,
                "coffee":20,
            },
            "cost": 80,

        },

}
profit=0
resources ={
    "water": 200,
    "milk" : 50,
    "coffee":75,
}


def check_resource(ingrediants):
    for item in ingrediants:
        if ingrediants[item]> resources[item]:
            print("===Sorry Not enough Resources===")
            return False
    return True


def calculate_money():
    five_ruppee=int(input("How many coins of 5 :"))
    ten_ruppee=int(input("How many coins of 10 :"))
    twenty_ruppee=int(input("How many coins of 20 :"))
    total= five_ruppee*5 + ten_ruppee*10 +twenty_ruppee*20
    return total

def check_money(cost_of_coffee,money_recieved):
    global profit
    if money_recieved>cost_of_coffee:
        change= money_recieved-cost_of_coffee
        print(f"your change is : Rs {change}  ")
        profit+=cost_of_coffee
        return True
    else:
        print("sorry you do not have enogh money  ")  
        print(f"You need Rs {cost_of_coffee-money_recieved} more") 
        return False

def resources_deduction(ingrediants):
    for item in ingrediants:
        resources[item] -=ingrediants[item]
    print(f"Here is your '{choice}' ☕")

print("===WELCOME TO COFFEE SHOP===")

is_on=True
while is_on:
    print("Type 'off' to exit and 'report' to show remaining ingrediants")
    choice=input("What would you like to have? (espresso/latte/cappuccino): ")
    if choice not in ("off","report","latte","espresso","cappuccino"):
        print("Cant understand Please type again!!!")
    
    elif choice=="off":
        is_on=False

    elif choice =="report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}grams")
        print(f"Profit is: RS{profit}")

    else:
        coffee_type=Menu[choice]
        print("==INGREDIANTS==")
        print(f"Water: {coffee_type['ingrediants']['water']}ml")
        print(f"Milk: {coffee_type['ingrediants']['milk']}ml")
        print(f"Coffee: {coffee_type['ingrediants']['coffee']}grams")
        print(f"Cost: {coffee_type['cost']} Rs")

        
        if check_resource(coffee_type['ingrediants']):
            print("==ENTER-MONEY==")
            money_recieved=calculate_money()
            if check_money(coffee_type['cost'],money_recieved):
                resources_deduction(coffee_type["ingrediants"])

