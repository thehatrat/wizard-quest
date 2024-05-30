import combat
import roommake
from random import randint
from random import choice
import shop


# functions
def show_player_stats():
    player_stats = f""" 
    {player["name"]}
    ----------------------------
    Health : {player["health"]}
    Health potions : {player["potions"]}
    Gold : {player["gold"]}
    Current weapon : {player["weapon"]}
    ----------------------------
    """
    print(player_stats)




def search():
    luck = randint(1, 12)  # trapx3, enemyx1, goldx3, weaponx2, healx1, nothingx2
    if luck == 1 or luck == 2 or luck == 3:
        traps = (
            "falling chandelier",
            "bear trap",
            "mimic",
        )
        trap = choice(traps)
        trap_damage = randint(5, 20)
        print(f"You were hurt by a {trap}! It dealt {trap_damage} damage.")
        player["health"] -= trap_damage
    elif luck == 4:
        print("You were attacked!")
        combat.combat(player, weapons)
          # enemy
    elif luck == 5 or luck == 6 or luck == 7:
        get_loot()
    elif luck == 8 or luck == 9:
        weapon()
    elif luck == 10:
        print("You found a health potion!")
        player["potions"] += 1
    else:
        print("You didn't find anything.")


def get_loot():
    loot = randint(100, 1000)
    print(f"You found {loot} gold!")
    player["gold"] += loot




def weapon():
    new_weap = choice(list(weapons))
    if new_weap == player["weapon"] and new_weap == "Fists":
        print("You didn't find anything.")
    elif new_weap == player["weapon"]:
        print(f"You found another {new_weap} but didn't need it.")
    else:
        if new_weap == "Fists":
            print("You are thinking of just using your fists instead.")
        else:
            print(f"You found a {new_weap}!")
        change_weap = roommake.decaps(input(
            f"Stop using {player['weapon']} in favor of {new_weap}? (y/n) "
        ))

        if change_weap == "y":
            player["weapon"] = new_weap

# variables


weapons = {
    "Stick": 0.1,
    "Dart Quiver": 0.2,
    "Broken Sword": 0.4,
    "Fists": 0.5,
    "Old sword": 0.6,
    "Dagger": 0.8,
    "Steel sword": 1.0,
    "Bow": 1.5,
    "Crossbow": 1.7,
    "Greatsword": 2.0,
}

player = {
    "health": 100,
    "potions": 1,
    "gold": 0,
    "weapon": "Fists",
}
rooms = 0
choices = ["Move on", "Heal", "Search", "Quit"]
weap_mult = weapons[player["weapon"]]
print(
    """┏┓┏┓┏┓╋╋╋╋╋╋╋╋╋╋╋┏┓┏━━━┓╋╋╋╋╋╋╋╋┏┓
┃┃┃┃┃┃╋╋╋╋╋╋╋╋╋╋╋┃┃┃┏━┓┃╋╋╋╋╋╋╋┏┛┗┓
┃┃┃┃┃┣┳━━━┳━━┳━┳━┛┃┃┃╋┃┣┓┏┳━━┳━┻┓┏┛
┃┗┛┗┛┣╋━━┃┃┏┓┃┏┫┏┓┃┃┃╋┃┃┃┃┃┃━┫━━┫┃
┗┓┏┓┏┫┃┃━━┫┏┓┃┃┃┗┛┃┃┗━┛┃┗┛┃┃━╋━━┃┗┓
╋┗┛┗┛┗┻━━━┻┛┗┻┛┗━━┛┗━━┓┣━━┻━━┻━━┻━┛
╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋┗┛
"""
)
player["name"] = input("What is your name, adventurer? ")
print(f"Hello, {player['name']}.")
shopluck = False
while True:
    show_player_stats()
    room = roommake.create_room(shopluck)
    if room is not True:
        print(room)
        rooms += 1
        action = roommake.get_input(choices)
        if action == "quit":
            break
        elif action == "search":
            print("")
            print("You searched the room!")
            search()
            shopluck = False
            if player["health"] <= 0:
                print("You passed out from your injuries")
                break
        elif action == "heal":
            combat.heal(player)
            shopluck = False
        else:
            print("")
            print(action)
            print("    You escape to the next room!")
            shopluck = True
    else:
        player = shop.shop(
            weapons,
            player,      
            show_player_stats,
        )
        
    print("")
    input("Press enter to continue. ")
    roommake.printbar()

print(
    r"""
  ___|    \     \  | ____|   _ \\ \     / ____|  _ \  | 
 |       _ \   |\/ | __|    |   |\ \   /  __|   |   | | 
 |   |  ___ \  |   | |      |   | \ \ /   |     __ < _| 
\____|_/    _\_|  _|_____| \___/   \_/   _____|_| \_\_) 
                                                        
"""
)
print(
    f"You have traveled through {rooms} rooms and have gotten {player['gold']} golden dabloons!"
)
