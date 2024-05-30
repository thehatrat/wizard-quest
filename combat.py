from random import choice, randint
import roommake
def battle_status(name, health, ename):
    namelength = len(list(name))
    healthlength = len(list(str(health)))
    space_length = " " * (namelength - healthlength)
    
    print(f"""
            {name}       {ename}
    HEALTH: {health}       {space_length}6
    WEAPON: 6

""")
def battle_status(player, ename, enemy_health):
    namelength = len(list(player['name']))
    healthlength = len(list(str(player['health'])))
    space_length = " " * (namelength - healthlength)
    print(f"""
            {player["name"]}       {ename}
    HEALTH: {player['health']}       {space_length}{enemy_health}
    WEAPON: {player['weapon']}

""")
    
def attack(weapons, player, enemy, enemy_health):
    bonus = randint(0, 20) #player turn
    if bonus == 0:
          print("You missed completely!")
    else:
        attack = round (weapons[player["weapon"]] * 15 + bonus)
        enemy_health -= attack
        print(f"You delt {attack} damage to the {enemy}")
        
    
    return enemy_health

def enemy_attack(player, enemy):
    bonus = randint(0, 20) #player turn
    if bonus == 0:
          print(f"The {enemy} missed completely!")
    else:
        attack = round (bonus * 1.5)
        player['health'] -= attack
        print(f"The {enemy} delt {attack} damage to you!")
        
    print("")
    return player
    
def heal(player):
    if player["health"] == 100:
        print("You already have full health!")
        return player
    elif player["potions"] == 0:
        print("You have no potions!")
        return player
    player["potions"] -= 1
    healing = randint(5, 15)
    player["health"] += healing
    if player["health"] > 100:
        player["health"] = 100
    print(f"You drank a health potion, healing {healing} health!")
    return player

def run(player, enemy_health):
    runchance = player["health"] - enemy_health
    runrandom = randint(1, 100)
    if runchance >= runrandom:
        print("You escaped succesfully")
        escape = True
    else:
        print("You failed to escape")
        escape = False
    return escape



def combat(player, weapons):
    enemies = [
        "Orc",
        "Troll",
        "Goblin",
        "Skeleton",
        "Zombie",
        "Demon",
        "Baby Dragon"

    ]
    choices = (
        "Attack",
        "Heal",
        "Run"
    )
    enemy = choice(enemies)
    print(f"A {enemy} jumped out from a shady corner!")
    roommake.printbar()
    enemy_health = randint(10, 40)
    while True:
        battle_status(player, enemy, enemy_health)
        action = roommake.get_input(choices)
        print("")
        if action == "run":
            escape = run(player, enemy_health)
            if escape == True:
                enemy_health = 0
        elif action == "heal":
            player = heal(player)
            
        else:
            enemy_health = attack(weapons, player, enemy, enemy_health)
         
        roommake.printbar()
        if enemy_health <= 0:
            break
        enemy_attack(player, enemy)
    print(f"You win the fight!")