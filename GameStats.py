################################################################################################
# Game Stats

# You were bored, so you decided to try out a new game you recently downloaded. There are 
# five types of characters, each with their own level of attack power, defense, and speed. 
# There are also five types of armor, weapons, and boots. Each type of item has a different 
# cost of gold and a different level of attack power, defense or speed. 
# Create a function that takes the type of character and the amount of gold. The function 
# should return the maximum amount of attack power possible, the maximum amount of 
# defense possible, and the maximum speed possible in a list, in that order. 

# Examples 
# ->    max_stats('Robot', 160)     -> [210, 220, 26]
# ->    max_stats('Fairy', 50)      -> [91, 120, 22]
# ->    max_stats('Warrior', 70)    -> [210, 211, 14]

# Notes 
# ->    Calculate the attack power, defense, and speed seperately. Do not calculate 
#       combinations of items. 
# ->    Check the Resources tab for the list of characters and items. 
# ->    Hint: Add the character's stats to the items' stats for the result. 
################################################################################################
## Made by Oliver Parry
##
## 27/04/2021
################################################################################################

stats = {
    'Characters': {
        'Knight': '120 attack, 140 defense, 6 speed',
        'Warrior': '180 attack, 71 defense, 8 speed',
        'Fairy': '71 attack, 100 defense, 16 speed',
        'Robot': '160 attack, 120 defense, 11 speed',
        'Giant': '160 attack, 200 defense, 4 speed'
    },
 
    'Weapons': {
        'Simple Sword': '10 attack, 20 gold',
        'Katana': '20 attack, 40 gold',
        'Sharpened Sword': '30 attack, 60 gold',
        'Great Sword': '40 attack, 80 gold',
        'Forgotten Sword': '50 attack, 100 gold'
    },
    
    'Armor': {
        'Bronze Armor': '20 defense, 30 gold',
        'Iron Armor': '40 defense, 60 gold',
        'Steel Armor': '60 defense, 90 gold',
        'Obsidian Armor': '80 defense, 120 gold',
        'Dragonhide Armor': '100 defense, 150 gold'
    },
    
    'Boots': {
        'Simple Boots': '3 speed, 24 gold',
        'Leather Boots': '6 speed, 48 gold',
        'Strong Boots': '9 speed, 72 gold',
        'Compound Boots': '12 speed, 96 gold',
        'Soft Boots': '15 speed, 120 gold'
    }
}

for category in stats:
    for item in stats[category]:
        statsString = stats[category][item]
        stats[category][item] = {}
        for stat in statsString.split(', '):
            split = stat.split(' ')
            stats[category][item][split[1]] = split[0]

def max_stats(className, gold):
    _class = stats['Characters'][className]