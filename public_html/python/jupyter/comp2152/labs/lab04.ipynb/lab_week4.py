# Import the random library to use for dice rolls and loot selection
import random

# Q1: Define Monster's Special Powers
monster_powers = {
    "Fire Magic": 2,       # Strength of 2
    "Freeze Time": 4,      # Strength of 4
    "Super Hearing": 6     # Strength of 6
}

# Q4: Define an empty array for the belt (stores loot collected by the player)
belt = []

# Hero's Attack Function
def hero_attacks(combat_strength, m_health_points):
    ascii_image = """
                                @@   @@ 
                                @    @  
                                @   @   
               @@@@@@          @@  @    
            @@       @@        @ @@     
           @%         @     @@@ @       
            @        @@     @@@@@     
               @@@@@        @@       
               @    @@@@                
          @@@ @@                        
       @@     @                         
   @@*       @                          
   @        @@                          
           @@                                                    
         @   @@@@@@@                    
        @            @                  
      @              @                  
      """
    print(ascii_image)
    print("Player's weapon (" + str(combat_strength) + ") ---> Monster (" + str(m_health_points) + ")")
    if combat_strength >= m_health_points:
        m_health_points = 0
        print("You have killed the monster")
    else:
        m_health_points -= combat_strength
        print("You have reduced the monster's health to " + str(m_health_points))
    return m_health_points

# Monster's Attack Function
def monster_attacks(m_combat_strength, health_points):
    ascii_image2 = """                                                                 
           @@@@ @                           
      (     @*&@  ,                         
    @               %                       
     &#(@(@%@@@@@*   /                      
      @@@@@.                                
               @       /                    
                %         @                 
            ,(@(*/           %              
               @ (  .@#                 @   
                          @           .@@. @
                   @         ,              
                      @       @ .@          
                             @              
                          *(*  *      
             """
    print(ascii_image2)
    print("Monster's Claw (" + str(m_combat_strength) + ") ---> Hero (" + str(health_points) + ")")
    if m_combat_strength >= health_points:
        health_points = 0
        print("You have killed the monster")
    else:
        health_points -= m_combat_strength
        print("The monster has reduced your health to " + str(health_points))
    return health_points

# Q2: Roll for Monster's Magic Power
input("\nPress Enter to roll for the monster's magic power...")
monster_magic = random.choice(list(monster_powers.keys()))  # Selects a random power

# Q3: Update Monster's Combat Strength based on rolled power (max limit is 6)
m_combat_strength = random.randint(1, 6)  # Initial strength
m_combat_strength = min(6, m_combat_strength + monster_powers[monster_magic])
print(f"The monster's new combat strength is {m_combat_strength} using {monster_magic} power.")

# Q5 & Q6: Player collects loot (first and second items)
loot_options = ["Health Potion", "Poison Potion", "Secret Note", "Leather Boots", "Flimsy Gloves"]
good_loot_options = ["Health Potion", "Leather Boots"]
bad_loot_options = ["Poison Potion"]

print("\nYou found a loot bag! Rolling for 2 loot items...")
for _ in range(2):  # Rolls twice for two loot items
    input("Press Enter to roll for loot...")
    loot_item = random.choice(loot_options)
    loot_options.remove(loot_item)  # Remove item from available loot
    belt.append(loot_item)  # Store in player's belt
print(f"Your loot belt: {belt}")

# Q7: Organizing the Loot Belt alphabetically
print("\nOrganizing your loot...")
belt.sort()
print(f"Organized loot belt: {belt}")

# Q8: Using the first loot item and applying its effects
print("\nA monster is approaching! You must use your first loot item.")
used_item = belt.pop(0)  # Remove and use the first item in the belt

# Q8: Adjust player's health based on the loot effect
health_points = random.randint(1, 6)  # Initial health
if used_item in good_loot_options:
    health_points = min(6, health_points + 2)  # Max health is 6
    print(f"You used {used_item} and gained health. Your health is now {health_points}.")
elif used_item in bad_loot_options:
    health_points = max(0, health_points - 2)  # Min health is 0
    print(f"You used {used_item} and lost health. Your health is now {health_points}.")
else:
    print(f"{used_item} did not provide any advantage.")

# Compare Player vs Monster's strength
print(f"\nPlayer strength: {health_points}, Monster strength: {m_combat_strength}")
print("--- You are matched in strength:", health_points == m_combat_strength)
print("--- You have a strong player:", (health_points + m_combat_strength) >= 15)

# Fight Sequence Begins
print("\nBattle begins!")
while health_points > 0 and m_combat_strength > 0:
    input("\nPress Enter to attack the monster...")
    m_combat_strength = hero_attacks(health_points, m_combat_strength)
    
    if m_combat_strength == 0:
        print("\nThe hero has won the battle! Hero receives three stars.")
        break

    input("\nPress Enter to defend against the monster's attack...")
    health_points = monster_attacks(m_combat_strength, health_points)

    if health_points == 0:
        print("\nThe hero has been defeated. Hero receives one star.")
        break
#Munoim Shahriar