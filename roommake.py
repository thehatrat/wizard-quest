from random import choice
from random import randint


# THIS FILE IS USED TO MAKE ROOMS FOR MAIN.PY AND IS USED TO IMPORT FUNCTIONS

def decaps(capitalized):
    caps = {
"A":1, "B":2, "C":3, "D":4, "E":5, "F":6, "G":7, "H":8, "I":9, "J":10,"K":11,"L":12,"M":13,
"N":14,"O":15,"P":16,"Q":17,"R":18,"S":19,"T":20,"U":21,"V":22,"W":23,"X":24,"Y":25,"Z":26,
 }
    lowcase = {
"a":1, "b":2, "c":3, "d":4, "e":5, "f":6, "g":7, "h":8, "i":9, "j":10,"k":11,"l":12,"m":13,
"n":14,"o":15,"p":16,"q":17,"r":18,"s":19,"t":20,"u":21,"v":22,"w":23,"x":24,"y":25,"z":26,
 } 
    approved_letters = [
    ]
    list_capitalized = list(capitalized)
    for letter in list_capitalized:
        list_caps = list(caps) 
        if letter in list_caps:            
            cap_key = caps[letter]#turns A to 1           
            for key, value in lowcase.items():
                if cap_key == value:
                    lowcaseletter = key   # turn 1 to a
                    approved_letters.append(lowcaseletter)
                    break
        else: approved_letters.append(letter)
    decapitalized = ''.join(approved_letters)
    return decapitalized
 
types = [
    "cavern",  # 1
    "throne room",  # 2
    "hallway",  # 3
    "dungeon",  # 4
    "courtyard",  # 5
    "kitchen",  # 6
    "garden",  # 7
    "tower",  # 8
    "armory",  # 9
    "library",  # 10
    "stable",  # 11
    "chaple",  # 12
]
adjectives = [
    "dusty",  # 1
    "old",  # 2
    "dark",  # 3
    "eerie",  # 4
    "strange",  # 5
    "long",  # 6
    "massive",  # 7
    "eroded",  # 8
    "modest",  # 9
]
adjectives2 = [
    "yet for some reason calming",  # 1
    "and chilly",  # 2
    "and warm",  # 3
    "and humid",  # 4
    "yet oddly soothing",  # 5
    "and curved",  # 6
    "and dusty",  # 7
    "and foggy",  # 8
]
features = [
    "life sized copper robot",  # 1
    "gilded chest",  # 2
    "huge plant sprout",  # 3
    "tree with silver leaves",  # 4
    "chainmail suit of armor",  # 5
    "greatsword half inside a rock",  # 6
    "skeletal hand holding a necklace",  # 7
    "a crumbled statue of a king, its head is gone",  # 8
]
def printbar():
    print("    ----------------------------")

def get_input(choices):
    print(
        """
    Actions"""
    )
    printbar()
    for choiced in choices:
        print(f"    {choiced}")
    print("")
    player_choice = decaps(input("What is your decision? "))
    return player_choice


def create_room(shopluck):
    if shopluck is False:
        shop_chance = randint(1, 8)
    elif shopluck is True:
        shop_chance = randint(1, 7)
        
    if shop_chance == 1:
        shop = True
        return shop
    else:
        feature = choice(features)
        room_type = choice(types)
        adj_1 = choice(adjectives)
        adj_2 = choice(adjectives2)
        description = f"""You look around and see the room containing you. It seems like a {adj_1}
{adj_2} {room_type}, in the center of the {room_type} lies a {feature}."""
    return description


          