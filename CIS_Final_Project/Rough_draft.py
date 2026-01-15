#William Tauferner
#Seth Johnson
#Mark Munetsi

#Adventure Game CIS 121 Final Project
#Character Classes
class Character:
    def __init__(self, health, dmg_range):
        self.health = health
        self.attack_damage = dmg_range

    def attack(self):
        return random.randint(self.attack_damage)

#dmg range has a min damage and max damage 
import random

class Warrior:
    def __init__(self, health, damage):
        self.name = "Warrior"
        self.health = health
        self.damage = damage   # (min_damage, max_damage)

    def attack(self):
        return random.randint(self.damage[0], self.damage[1])


class Wizard:
    def __init__(self, health, damage):
        self.name = "Wizard"
        self.health = health
        self.damage = damage

    def attack(self):
        return random.randint(self.damage[0], self.damage[1])


class Dwarf:
    def __init__(self, health, damage):
        self.name = "Dwarf"
        self.health = health
        self.damage = damage

    def attack(self):
        return random.randint(self.damage[0], self.damage[1])
    
    def __str__(self):
        return f'You are {self.name} with {self.health} and deal {self.damage}'


#Enemy Classes
class Goblin:
    def __init__(self, health, damage):
        self.name = "Goblin"
        self.health = health
        self.damage = damage

    def attack(self):
        return random.randint(self.damage[0], self.damage[1])
    def __str__(self):
        return f'You are {self.name} with {self.health} and deal {self.damage}'

class Wolf:
    def __init__(self, health, damage):
        self.name = "Wolf"
        self.health = health
        self.damage = damage

    def attack(self):
        return random.randint(self.damage[0], self.damage[1])
    def __str__(self):
        return f'You are {self.name} with {self.health} and deal {self.damage}'

class Thanos:
    def __init__(self, health, damage):
        self.name = "Thanos"
        self.health = health
        self.damage = damage

    def attack(self):
        return random.randint(self.damage[0], self.damage[1])
#####Character Creation#####

#Press Enter to Start Game
#Ask User for Input for their name
user_name = print(input('Please select a name for your character'))
#Ask User to Pick a class between Warrior, Dwarf, or Wizard
print('Please select a class for your game, Warrior:Dwarf:Wizard')
user_class = int(input('select 1 for warrior, 2 for dwarf, and 3 for wizard'))
if user_class == 1:
    player = Warrior(120, (6, 10))
elif user_class == 2:
    player = Dwarf(130, (5, 12))
elif user_class == 3:
    player = Wizard(90, (8, 14))
else:
    print("Invalid choice")
####Gameplay####
#If you pick Warrior you start at "location 1" (Create origin story for warrior)
if self.name == 'Warrior':
    print('You have spawned in at cozycove with a sword and a health pot')
#if you pick Dwarf you start at 'location 2'    (create origin story for Dwarf)
elif self.name == 'Dwarf':
    print('You have spawned in at the dark mountains with a axe and a health pot')
#if you pick Wizard you start at 'location 3'   (create origin story for wizard)
elif self.name == 'Wizard':
    print('You have spawned in at the tall tower in the meadows with a staff and a health pot')
# You start at 'set location that is chosen based on class character' print the story for the set location
# Ask user if they want to loot for a chance at a better weapon(a random enemy attacks you), rest for added health, or continue towards Boss Fight
user_choice = input('Press 1 for loot, 2 for rest, or 3 to continue:')
if user_choice == 1:
    print('you chose to loot')
elif user_choice == 2:
    print('you chose to rest for added health!')
elif user_choice ==3:
    print('YOu chose to continue onwards!')
#Continue to Final Boss destination
#Prompt your stats and ask if you still wanna loot or fight
    #if loot use pre made functions that spawn in enemy and give loot
    #else fight Thanos which prompts the combat system
#If you beat thanos print statement saying you won the game
#Else you die print statement saying you lost the game


####Combat Plan####
#Run for loops and while loops for each encounter with random enemy and Final Boss
# While both the player and enemy are alive, keep looping combat
# while player.hp > 0 and enemy.hp > 0:
    # Display HP for player and enemy each round
    # Ask player for combat choice
    # Process combat action
    # Enemy attacks after player's turn

#Character Classes
#Warrior(Health, attack damage)
#Wizard(Health, attack damage)
#Dwarf(Health, attack damage)
import random

#Goblin(Health, attack damage)  #Part of random encounter event
#Wolf(Health, Attack damage)    #Part of random encounter event
#Final Boss
    #Thanos(Health, Attack Damage)  #Part of Final destination

#Use dictionary for different weapons

#Use dictionary for different potions