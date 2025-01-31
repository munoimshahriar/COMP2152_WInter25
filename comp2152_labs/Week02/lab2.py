import random

# Define the weapons array
weapons = ["Fist", "Knife", "Club", "Gun", "Bomb", "Nuclear bomb"]

try:
    # Roll the dice (1-6)
    weaponRoll = random.randint(1, 6)
    print(f"You rolled: {weaponRoll}")

    # Add weaponRoll to hero's combat strength
    hero_combat_strength = 10  # Example combat strength
    hero_combat_strength += weaponRoll
    print(f"Hero's combat strength: {hero_combat_strength}")

    # Use weaponRoll as an index into the weapons array
    weapon = weapons[weaponRoll - 1]
    print(f"Hero's weapon: {weapon}")

    # Conditions based on weaponRoll
    if weaponRoll <= 2:
        print("You rolled a weak weapon, friend.")
    elif weaponRoll <= 4:
        print("Your weapon is meh.")
    else:
        print("Nice weapon, friend!")

    # Check if the weapon is not a Fist
    if weapon != "Fist":
        print("Thank goodness you didn't roll the Fist...")

except Exception as e:
    print(f"An error occurred: {e}")
import random

# Define the weapons array
weapons = ["Fist", "Knife", "Club", "Gun", "Bomb", "Nuclear bomb"]

def roll_dice(min_value, max_value):
    return random.randint(min_value, max_value)

def get_weapon(weapon_roll):
    if 1 <= weapon_roll <= len(weapons):
        return weapons[weapon_roll - 1]
    else:
        return "Invalid roll"

def evaluate_weapon(weapon_roll):
    if weapon_roll <= 2:
        return "You rolled a weak weapon, friend."
    elif weapon_roll <= 4:
        return "Your weapon is meh."
    else:
        return "Nice weapon, friend!"

def main():
    try:
        # Roll the dice (1-6)
        weapon_roll = roll_dice(1, 6)
        print(f"You rolled: {weapon_roll}")

        # Add weapon_roll to hero's combat strength
        hero_combat_strength = 10  # Example combat strength
        hero_combat_strength += weapon_roll
        print(f"Hero's combat strength: {hero_combat_strength}")

        # Use weapon_roll as an index into the weapons array
        weapon = get_weapon(weapon_roll)
        print(f"Hero's weapon: {weapon}")

        # Conditions based on weaponRoll
        print(evaluate_weapon(weapon_roll))

        # Check if the weapon is not a Fist
        if weapon != "Fist":
            print("Thank goodness you didn't roll the Fist...")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
rm -rf .git
