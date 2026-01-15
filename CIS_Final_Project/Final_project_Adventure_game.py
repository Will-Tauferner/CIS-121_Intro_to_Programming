# CIS 121 Final Project - Adventure Battle Game 
# Group Members:
# William Tauferner
# Seth Johnson
# Mark Munetsi

# Classes 
import random
class Player:
    
    #Player-controlled character.
    #name, class, health, damage range, potions, and inventory.


    def __init__(self, name, character_class, health, dmg_range):
        # Core stats
        self.name = name
        self.character_class = character_class
        self.health = health
        self.max_health = health
        # dmg_range is a tuple: (min_damage, max_damage)
        self.dmg_range = dmg_range

        # Player-specific collections:
        # dictionary of potions and a list inventory
        self.potions = {
            "small": 2,   # number of small potions
            "large": 1    # number of large potions
        }
        self.inventory = []

    def attack(self):
        #Return a random damage value within the player's damage range
        return random.randint(self.dmg_range[0], self.dmg_range[1])

    def is_alive(self):
        #Check if the player is still alive
        return self.health > 0

    def heal(self, amount):
        #Restore health by the given amount, up to max_health
        self.health = min(self.max_health, self.health + amount)

    def use_potion(self):
    
        #Use the best available potion if any exist.
                
        missing = self.max_health - self.health

        if self.potions["large"] > 0 or self.potions["small"] > 0:
            # Prefer large potion if we are missing a lot of health
            if self.potions["large"] > 0 and missing > 25:
                self.heal(25)
                self.potions["large"] -= 1
                print("You drink a large potion and recover 25 HP.")
            elif self.potions["small"] > 0:
                self.heal(15)
                self.potions["small"] -= 1
                print("You drink a small potion and recover 15 HP.")
            else:
                print("You are out of usable potions.")
        else:
            print("You have no potions left!")


class Goblin:
    #A basic enemy with low health and damage.

    def __init__(self):
        self.name = "Goblin"
        self.health = 50
        self.max_health = 50
        self.dmg_range = (3, 7)

    def attack(self):
        return random.randint(self.dmg_range[0], self.dmg_range[1])

    def is_alive(self):
        return self.health > 0


class Wolf:
    #A slightly tougher enemy

    def __init__(self):
        self.name = "Wolf"
        self.health = 60
        self.max_health = 60
        self.dmg_range = (4, 8)

    def attack(self):
        return random.randint(self.dmg_range[0], self.dmg_range[1])

    def is_alive(self):
        return self.health > 0


class Thanos:
    #Final boss with high health and damage.

    def __init__(self):
        self.name = "Thanos"
        self.health = 120
        self.max_health = 120
        self.dmg_range = (10, 20)

    def attack(self):
        return random.randint(self.dmg_range[0], self.dmg_range[1])

    def is_alive(self):
        return self.health > 0


# File I/O 

def write_combat_log(enemy_name, damage_dealt, damage_taken, result):
    #I/) file for storing who you battle against
    with open("combat_log.csv", "a") as f:
        f.write(f"{enemy_name},{damage_dealt},{damage_taken},{result}\n")

#  Helper Functions 

def create_player():
    #Ask the user for their character name and class, then return a Player object
    print(" Welcome to the Adventure Battle Game! ")
    name = input("Please enter a name for your character: ")

    # Loop until a valid class is selected
    while True:
        print("\nPlease select a class for your character:")
        print("1 - Warrior (High health, steady damage)")
        print("2 - Dwarf   (Very tanky, moderate damage)")
        print("3 - Wizard  (Low health, high damage)")
        choice = input("Enter 1, 2, or 3: ")

        if choice == "1":
            # Warrior stats
            return Player(name, "Warrior", 120, (6, 10))
        elif choice == "2":
            # Dwarf stats
            return Player(name, "Dwarf", 130, (5, 12))
        elif choice == "3":
            # Wizard stats
            return Player(name, "Wizard", 90, (8, 14))
        else:
            print("Invalid choice, please try again.")


def describe_starting_location(player):
    #Print the starting location story based on the player's class
    print("\n Your Story Begins !!!")
    if player.character_class == "Warrior":
        print("You awaken in Cozy Cove with a trusty sword and a health potion.")
    elif player.character_class == "Dwarf":
        print("You awaken in the Dark Mountains with a heavy axe and a health potion.")
    elif player.character_class == "Wizard":
        print("You awaken in the Meadow Tower with an ancient staff and a health potion.")
    else:
        print("You awaken in a mysterious land with no memory of how you got here.")


def show_player_stats(player):
    #Print the player's current stats
    print("\n--- Your Stats ---")
    print(f"Name: {player.name}")
    print(f"Class: {player.character_class}")
    print(f"Health: {player.health}/{player.max_health}")
    print(f"Damage Range: {player.dmg_range[0]} - {player.dmg_range[1]}")
    print(f"Potions (small/large): {player.potions['small']}/{player.potions['large']}")
    if player.inventory:
        print(f"Inventory: {', '.join(player.inventory)}")
    else:
        print("Inventory: Empty")


def random_enemy():
    
    #Return a random enemy instance.
    enemy_types = [Goblin, Wolf]
    enemy_class = random.choice(enemy_types)
    return enemy_class()


def loot(player):
    
    #Perform a loot action:
    #Random enemy encounter
    #If player survives, there is a chance to find a better weapon.
    #Demonstrates use of a dictionary for weapon choices.
    enemy = random_enemy()
    survived, damage_dealt, damage_taken = combat(player, enemy)

    result = "victory" if survived else "defeat"
    write_combat_log(enemy.name, damage_dealt, damage_taken, result)

    if not survived:
        print("You were defeated while looting...")
        return False

    # Dictionary of possible weapon upgrades: name -> damage_range (tuple)
    weapon_upgrades = {
        "Steel Sword": (8, 12),
        "Runic Axe": (7, 14),
        "Crystal Staff": (10, 16)
    }

    print("\nYou search the fallen enemy for loot...")
    found_weapon = random.choice(list(weapon_upgrades.keys()))
    new_range = weapon_upgrades[found_weapon]
    print(f"You found a {found_weapon}! Damage range {new_range[0]} - {new_range[1]}.")

    # Add to inventory list and equip the weapon
    player.inventory.append(found_weapon)
    player.dmg_range = new_range
    print(f"You equip the {found_weapon}. You feel stronger!")

    return True


def rest(player):
    #Rest and recover some health
    print("\nYou decide to rest for a while...")
    before = player.health
    player.heal(20)
    recovered = player.health - before
    print(f"You recover {recovered} HP. Your health is now {player.health}/{player.max_health}.")


def combat(player, enemy):
    
    #A while loop that continues while both are alive.
    #Nested selection statements inside the loop for player actions.
    #Returns (survived, total_damage_dealt, total_damage_taken)
    
    print(f"\n A wild {enemy.name} appears! ")

    total_damage_dealt = 0
    total_damage_taken = 0

    # Loop until someone dies
    while player.is_alive() and enemy.is_alive():
        print(f"\nYour HP: {player.health}/{player.max_health}")
        print(f"{enemy.name} HP: {enemy.health}/{enemy.max_health}")
        print("Choose an action:")
        print("1 - Attack")
        print("2 - Use Potion")
        print("3 - Attempt to Run")

        action = input("Enter 1, 2, or 3: ")

        if action == "1":
            # Player attacks
            dmg = player.attack()
            enemy.health -= dmg
            total_damage_dealt += dmg
            print(f"\nYou strike the {enemy.name} for {dmg} damage!")
        elif action == "2":
            #Player takes health potion
            player.use_potion()
        elif action == "3":
            # Try to run (50% chance)
            if random.random() < 0.5:
                print("\nYou successfully escaped!")
                return True, total_damage_dealt, total_damage_taken
            else:
                print("\nYou try to run, but the enemy blocks your path!")
        else:
            print("\nInvalid action, you hesitate...")

        # Enemy's turn if it is still alive
        if enemy.is_alive():
            enemy_dmg = enemy.attack()
            player.health -= enemy_dmg
            total_damage_taken += enemy_dmg
            print(f"The {enemy.name} hits you for {enemy_dmg} damage!")

    # After the loop, check who survived
    if player.is_alive():
        print(f"\nYou have defeated the {enemy.name}!")
        return True, total_damage_dealt, total_damage_taken
    else:
        print(f"\nYou were defeated by the {enemy.name}...")
        return False, total_damage_dealt, total_damage_taken


def final_boss_sequence(player):
    #Final battle against Thanos
    print("\nYou geared up and march toward the final destination...")
    thanos = Thanos()
    survived, damage_dealt, damage_taken = combat(player, thanos)
    result = "victory" if survived else "defeat"
    write_combat_log(thanos.name, damage_dealt, damage_taken, result)

    if survived:
        print("\n CONGRATULATIONS! You have defeated Thanos and won the game!")
    else:
        print("\n GAME OVER. Thanos has ended your adventure")

    return survived


def main():
    #Main game
    player = create_player()
    describe_starting_location(player)
    show_player_stats(player)

    #game loop
    game_over = False
    while player.is_alive() and not game_over:
        print("\nWhat would you like to do next?")
        print("1 - Loot for better gear (random encounter)")
        print("2 - Rest and recover")
        print("3 - Continue toward Thanos")
        print("4 - View your stats")
        print("5 - Quit game")
        choice = input("Enter 1, 2, 3, 4, or 5: ")

        if choice == "1":
            if not loot(player):
                game_over = True
        elif choice == "2":
            rest(player)
        elif choice == "3":
            # Proceed to final boss; after that, game ends
            final_boss_sequence(player)
            game_over = True
        elif choice == "4":
            show_player_stats(player)
        elif choice == "5":
            print("\nYou decide to end your journey for now.")
            game_over = True
        else:
            print("Invalid choice, please try again.")

        if not player.is_alive():
            print("\nYou have fallen in your journey. Game over.")
            game_over = True

    print("\nThank you for playing the Adventure Game!")

if __name__ == "__main__":
    main()