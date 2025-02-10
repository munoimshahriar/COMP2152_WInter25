import random

# I created a function to handle collecting loot from the environment.
# It needs the player's belt (where loot can be stored) and
# whatever loot_options I had available.
# It will return the updated belt and the remaining loot_options.
def collect_loot(belt, loot_options):
    print("Collecting loot...")
    
    # Here, I'm simulating picking up "Gold coins" from my loot_options, 
    # but you can replace this with your own logic if needed.
    if "Gold coins" in loot_options:
        print("Nice! Found Gold coins!")
        belt.append("Gold coins")
        loot_options.remove("Gold coins")

    # I return the updated belt and loot_options so I can use them later in the code.
    return belt, loot_options

# This function lets me use any loot I've collected.
# It needs my belt (to see what's inside) and my current health_points 
# so I can change them if I use a healing item.
def use_loot(belt, health_points):
    print("Using loot...")

    # If I have a "Potion" in my belt, I might want to drink it and gain some HP.
    # This is just a sample; you can replace with your own item logic.
    if "Potion" in belt:
        print("Drinking a potion... +10 HP!")
        health_points += 10
        belt.remove("Potion")

    # Return the updated belt and health_points after using the item.
    return belt, health_points

# This function handles going deeper into the dream.
# If the user decides to keep going, we add 1 and call the function again recursively.
# If not, we return 2 as a base case.
def inception_dream():
    deeper = input("Do you want to go deeper into the dream? (y/n): ").strip().lower()
    if deeper == 'y':
        # Recursive call adds 1 for each deeper level, plus whatever the deeper calls add.
        return 1 + inception_dream()
    else:
        # Base case: returning 2 when the user decides not to go deeper.
        return 2

def main():
    # 1) Ask for Hero name in two words; loop until it’s valid.
    while True:
        hero_name = input("Enter your Hero's name (in two words): ").strip()
        parts = hero_name.split()
        if len(parts) == 2 and parts[0].isalpha() and parts[1].isalpha():
            break
        else:
            print("Invalid input! Please enter two alphabetical words (e.g. 'Strong John').")

    # Extract each word separately.
    first_word, second_word = parts[0], parts[1]
    
    # 2) Create short_name using slicing: first two chars of the first word,
    #    plus first char of the second word.
    short_name = first_word[:2] + second_word[:1]

    # 3) In this game, let's say the hero just earned some stars. I'll store it in stars_display.
    stars_display = 5
    # Print the stars message including the short_name:
    print(f"Hero {short_name} gets {stars_display} stars")

    # 4) Set up belt, loot_options, and health_points. (These are just examples.)
    belt = []
    loot_options = ["Gold coins", "Potion", "Sword"]
    health_points = 100
    
    # 5) Collect loot using the function instead of hard-coded logic.
    belt, loot_options = collect_loot(belt, loot_options)
    
    # 6) Use loot if available.
    belt, health_points = use_loot(belt, health_points)

    # Quick debug prints to see updated values (optional).
    print("Belt now contains:", belt)
    print("Remaining loot options:", loot_options)
    print("Current health points:", health_points)

    # 7) Roll a dice (1-6) to see who attacks first.
    attack_roll = random.randint(1,6)
    print(f"Attack roll result: {attack_roll}")
    if attack_roll in [1, 3, 5]:
        print("Hero attacks first!")
        # hero_attack()  # If you have a hero_attack() function, call it here.
        # monster_attack()  # If you have a monster_attack() function, call it next.
    else:
        print("Monster attacks first!")
        # monster_attack()  # If you have a monster_attack() function, call it first.
        # hero_attack()     # Then let the hero respond.

    # 8) Recursion: We call inception_dream() to see how crazy things get.
    crazy_level = inception_dream()

    # After returning from the dream, we lose 1 health but gain crazy_level to our combat strength.
    health_points -= 1
    combat_strength = 10  # Example base combat strength
    combat_strength += crazy_level

    print(f"After emerging from the dream, your hero's health is {health_points}, "
          f"and combat_strength is {combat_strength} (crazy_level={crazy_level}).")

# Standard Python practice: call main() only when this script is the entry point.
if __name__ == "__main__":
    main()