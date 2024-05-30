import roommake
from random import choice, randint


def weapon_price(weapons, item, sell):

    fee = randint(0, 100) #random from 1 - 100
    weap_mult = weapons[item]
    
    if sell == True:
        fltprice = weap_mult * 100 + 725 - fee
    else:
        fltprice = weap_mult * 100 + 725 + fee
    cost = round(fltprice)
    return cost






def shop(weapons, player, stats):

    
    print("")
    print("You find yourself in a shop, standing at a counter is a merchant.")
    choices = ( "Buy", "Sell", "Talk", "Leave")
    talk_count = 0
    while True:
        stats()
        action = roommake.get_input(choices)
        if action == "talk":
            if talk_count == 0:
                print(
                    "    You talk to the shopkeeper, they tell you that stronger items appear in the shop less often."
                )
                talk_count += 1
            elif talk_count == 1:
                print(
                    "    You continue talking to the shopkeeper, they say that you should leave rooms quickly in order to find the shop again."
                )
                talk_count += 1
            else:
                print(    "The shop keeper doesn't seem to want to keep talking")
        elif action == "sell":
            sell = input("""What do you sell: 
    1. Your weapon
    2. Potions
    3+. Cancel """)
            if sell == "1":
                if player['weapon'] == "Fists":
                    print("You don't have a weapon to sell")
                else:
                    weapon_price(weapons, player['weapon'], True)
                    agree = roommake.decaps(input(f"Sell {player['weapon']} for {weapon_price} gold? (y/n) "))
                    if agree == "y":
                        player['gold'] += weapon_price
                        player['weapon'] = "Fists"
                        
            elif sell == "2":
                if player["potions"] == 0:
                    print("You don't have any potions to sell")
                else:
                    fee = randint(0, 100)
                    hprice = 1550 - fee

                    agree = roommake.decaps(input(f"Sell 1 potion for {hprice} gold? (y/n) "))
                    if agree == "y":
                        player['gold'] += hprice
                        player['potions'] -= 1
                        
        elif action == "leave" :
            print("    You leave the shop.")
            return player
        else:
            item1fist = True
            item2fist = True
            while item1fist:
                item1 = choice(list(weapons))
                if item1 != "Fists":
                    item1fist = False
            while item2fist:
                item2 = choice(list(weapons))
                if item2 != "Fists":
                    item2fist = False
            cost1 = weapon_price(weapons, item1, False)
            cost2 = weapon_price(weapons, item2, False)
            hfee = randint(0, 100)
            hcost = 1550 + hfee
            print(f"In the store you can see a {item1}, a {item2} and a health potion.")
            buy = input(f"""What would you like to buy? 
    1. a {item1} costing {cost1}
    2. a {item2} costing {cost2}
    3. a health potion costing {hcost}
    4+. Cancel
    """)
            if buy == "1":
                if player['gold'] < cost1:
                    print("You don't have enough gold.")
                else:
                    agree = roommake.decaps(input(f"Buy {item1} for {cost1} gold? (y/n) "))
                    if agree == "y":
                        player['gold'] -= cost1
                        player['weapon'] = item1
                        
            elif buy == "2":
                if player['gold'] < cost2:
                    print("You don't have enough gold.")
                else:
                    agree = roommake.decaps(input(f"Buy {item2} for {cost2} gold? (y/n) "))
                    if agree == "y":
                        player['gold'] -= cost2
                        player['weapon'] = item2
                        
            elif buy == "3":
                if player['gold'] < hcost:
                    print("You don't have enough gold.")
                else:
                    agree = roommake.decaps(input(f"Buy a health potion for {hcost} gold? (y/n) "))
                    if agree == "y":
                        player['gold'] -= hcost
                        player['potions'] += 1
                        