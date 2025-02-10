#lab 3 solutions

import random

# Dice options (1 to 6)
diceOptions = list(range(1, 7))

# Weapons list
weapons = ["Fist", "Knife", "Club", "Gun", "Bomb", "Nuclear Bomb"]

# Show available weapons
print("Available Weapons:")
for i, weapon in enumerate(weapons, start=1):
    print(f"{i}. {weapon}")

# Function to validate input
def get_valid_input(prompt):
    while True:
        try:
            value = int(input(prompt))
            if 1 <= value <= 6:
                return value
            else:
                print("Input must be an integer between 1 and 6.")
        except ValueError:
            print("Invalid input. Please enter an integer.")

# Main battle simulation
if __name__ == "__main__":
    try:
        # Get player and monster combat strengths
        combatStrength = get_valid_input("Enter your combat Strength (1-6): ")
        mCombatStrength = get_valid_input("Enter monster's combat Strength (1-6): ")

        # Simulate 10 rounds of battle
        for round_number in range(1, 20, 2):
            hero_roll = random.choice(diceOptions)
            monster_roll = random.choice(diceOptions)

            hero_total_strength = combatStrength + hero_roll
            monster_total_strength = mCombatStrength + monster_roll

            hero_weapon = weapons[hero_roll - 1]
            monster_weapon = weapons[monster_roll - 1]

            print(f"\nRound {round_number}: Hero rolled {hero_roll}, Monster rolled {monster_roll}.")
            print(f"Hero selected: {hero_weapon}, Monster selected: {monster_weapon}.")
            print(f"Hero Total Strength: {hero_total_strength}, Monster Total Strength: {monster_total_strength}.")

            if hero_total_strength > monster_total_strength:
                print("Hero wins the round!")
            elif hero_total_strength < monster_total_strength:
                print("Monster wins the round!")
            else:
                print("It's a tie!")

            # Break condition for "Battle Truce"
            if round_number == 11:
                print("\nBattle Truce declared at Round 11. Game Over!")
                break

    except Exception as e:
        print(f"An error occurred: {e}")
        print("Please ensure your environment supports the 'random' module and try again.")
#Munoim Shahriar