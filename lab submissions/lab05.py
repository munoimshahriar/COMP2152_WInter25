import random
import functions_lab05 as funcs

# 1) Ask user for Hero Name in two words
#    Loop until valid: must have exactly two words, both alphabetical
while True:
    hero_name = input("Enter your Hero's name (in two words): ").strip()
    parts = hero_name.split()
    if len(parts) == 2 and parts[0].isalpha() and parts[1].isalpha():
        break
    else:
        print("Invalid input. Please enter two alphabetic words, e.g. 'Strong John'.")

# Create short_name from first two letters of first word plus first letter of second word
first_word, second_word = parts[0], parts[1]
short_name = first_word[:2] + second_word[:1]

# 2) Define Dice
small_dice_options = list(range(1, 7))
big_dice_options = list(range(1, 21))

# 3) Define Weapons
weapons = ["Fist", "Knife", "Club", "Gun", "Bomb", "Nuclear Bomb"]

# 4) Define Loot
loot_options = ["Health Potion", "Poison Potion", "Secret Note", "Leather Boots", "Flimsy Gloves"]
good_loot_options = ["Health Potion", "Leather Boots"]
bad_loot_options = ["Poison Potion"]
belt = []

# 5) Monster Powers
monster_powers = {
    "Fire Magic": 2,
    "Freeze Time": 4,
    "Super Hearing": 6
}

# 6) Ask user for Hero and Monster combat strengths (1-6), with up to 5 tries
input_invalid = True
attempts = 0
while input_invalid and attempts < 5:
    print("    ------------------------------------------------------------------")
    p_str = input("Enter your combat Strength (1-6): ")
    m_str = input("Enter the monster's combat Strength (1-6): ")

    if not p_str.isnumeric() or not m_str.isnumeric():
        print("One or more invalid inputs. Enter integer numbers only.")
        attempts += 1
        continue

    if int(p_str) not in range(1, 7) or int(m_str) not in range(1, 7):
        print("Enter a valid integer between 1 and 6 only.")
        attempts += 1
        continue

    # Valid inputs
    combat_strength = int(p_str)
    m_combat_strength = int(m_str)
    input_invalid = False

# If still invalid after 5 tries, you could exit or set defaults
if input_invalid:
    print("Too many invalid attempts. Setting default values.")
    combat_strength = 3
    m_combat_strength = 3

# 7) Roll for a weapon and add it to player's combat_strength
print("    |", end="    ")
input("Roll the dice for your weapon (Press enter)")

weapon_roll = random.choice(small_dice_options)
combat_strength = min(6, (combat_strength + weapon_roll))  # max out at 6 if needed
chosen_weapon = weapons[weapon_roll - 1]
print(f"    |    The hero’s weapon is: {chosen_weapon}")
if chosen_weapon != "Fist":
    print("    |    --- Thank goodness you didn't roll the Fist...")

# Quick analysis
if weapon_roll <= 2:
    print("--- You rolled a weak weapon, friend")
elif weapon_roll <= 4:
    print("--- Your weapon is decent")
else:
    print("--- Nice weapon, friend!")

# 8) Roll for player health points
input("Roll the dice for your health points (Press enter)")
health_points = random.choice(big_dice_options)
print("    |    Player rolled", health_points, "health points")

# 9) Roll for monster health points
input("Roll the dice for the monster's health points (Press enter)")
m_health_points = random.choice(big_dice_options)
print("    |    Monster's health points:", m_health_points)

# 10) Collect Loot (twice) via the collect_loot() function
print("!!You find a loot bag!! It contains 2 items:")
belt, loot_options = funcs.collect_loot(belt, loot_options)
belt, loot_options = funcs.collect_loot(belt, loot_options)

# Sort belt alphabetically (just as you had in your code)
print("You're super neat, so you organize your belt alphabetically:")
belt.sort()
print("Your belt:", belt)

# 11) Use Loot (first item in belt) via the use_loot() function
belt, health_points = funcs.use_loot(belt, health_points, good_loot_options, bad_loot_options)

# 12) Compare Player vs Monster's Strength
print("    ------------------------------------------------------------------")
print("    |    --- You are matched in strength:", (combat_strength == m_combat_strength))
print("    |    --- You have a strong player:", ((combat_strength + health_points) >= 15))

# 13) Monster gains a random Magic Power
input("Roll for Monster's Magic Power (Press enter)")
power_roll = random.choice(list(monster_powers.keys()))
power_amount = monster_powers[power_roll]
m_combat_strength = min(6, m_combat_strength + power_amount)
print(f"    |    The monster's combat strength is now {m_combat_strength} using {power_roll} magic power")

# 14) **Roll to see who attacks first** based on odd/even
attack_roll = random.choice(small_dice_options)
print(f"\nRolling a dice to see who attacks first... You got {attack_roll}")

# 15) Fight Sequence
print("You meet the monster. FIGHT!!")
num_stars = 0  # track how many stars we earn at the end

while m_health_points > 0 and health_points > 0:
    if attack_roll in [1,3,5]:
        # Hero attacks first
        input("Hero strikes first (Press Enter)")
        m_health_points = funcs.hero_attacks(combat_strength, m_health_points)
        if m_health_points == 0:
            num_stars = 3
            break
        input("Monster strikes next (Press Enter)")
        health_points = funcs.monster_attacks(m_combat_strength, health_points)
        if health_points == 0:
            num_stars = 1
            break
    else:
        # Monster attacks first
        input("Monster strikes first (Press Enter)")
        health_points = funcs.monster_attacks(m_combat_strength, health_points)
        if health_points == 0:
            num_stars = 1
            break
        input("Hero strikes next (Press Enter)")
        m_health_points = funcs.hero_attacks(combat_strength, m_health_points)
        if m_health_points == 0:
            num_stars = 3
            break

    num_stars = 2  # if both still alive, maybe we award 2 stars

# 16) Recursion: Ask if we want to dive deeper into a dream
crazy_level = funcs.inception_dream()
health_points -= 1  # lose 1 HP after the dream
combat_strength += crazy_level  # gain crazy_level to hero's combat strength

print(f"\nAfter the dream, your hero's health is {health_points}, and combat_strength is {combat_strength}.")
print(f"(crazy_level = {crazy_level})")

# 17) Final awarding of stars, with short_name
stars_display = "*" * num_stars
print(f"Hero {short_name} gets <{stars_display}> stars")