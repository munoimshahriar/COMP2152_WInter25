import random

# Will the line below print when you import function.py into main.py?
# print("Inside function.py")  # <-- Typically won't print unless you remove the comment

# ---------------------------------------------------------------------
# 1) Hero's Attack Function
# ---------------------------------------------------------------------
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
    print(f"    |    Player's weapon ({combat_strength}) ---> Monster ({m_health_points})")

    if combat_strength >= m_health_points:
        # Player was strong enough to kill monster in one blow
        m_health_points = 0
        print("    |    You have killed the monster")
    else:
        # Player only damaged the monster
        m_health_points -= combat_strength
        print("    |    You have reduced the monster's health to:", m_health_points)

    return m_health_points

# ---------------------------------------------------------------------
# 2) Monster's Attack Function
# ---------------------------------------------------------------------
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
    print(f"    |    Monster's Claw ({m_combat_strength}) ---> Player ({health_points})")

    if m_combat_strength >= health_points:
        # Monster was strong enough to kill player in one blow
        health_points = 0
        print("    |    Player is dead")
    else:
        # Monster only damaged the player
        health_points -= m_combat_strength
        print("    |    The monster has reduced Player's health to:", health_points)

    return health_points

# ---------------------------------------------------------------------
# 3) collect_loot() Function
#    - Takes the current belt and loot_options
#    - Allows the player to "roll" for loot from the bag
#    - Returns updated belt and loot_options
# ---------------------------------------------------------------------
def collect_loot(belt, loot_options):
    """Simulate picking loot randomly from loot_options and storing it in belt."""
    input("Roll for an item (Press Enter)")
    if len(loot_options) > 0:
        lootRoll = random.choice(range(1, len(loot_options) + 1))
        # Grab that loot
        loot = loot_options.pop(lootRoll - 1)
        belt.append(loot)
        print("You found:", loot)
        print("Your belt:", belt)
    else:
        print("No loot left to collect!")

    return belt, loot_options

# ---------------------------------------------------------------------
# 4) use_loot() Function
#    - Takes belt, health_points, plus any “good” or “bad” lists you might need
#    - Uses (pops) an item from the belt
#    - Returns updated belt, health_points
# ---------------------------------------------------------------------
def use_loot(belt, health_points, good_loot_options, bad_loot_options):
    """Use the first item in your belt. If it's good, gain HP; if bad, lose HP."""
    if len(belt) == 0:
        print("Nothing in your belt to use!")
        return belt, health_points

    print("!!You see a monster in the distance! So you quickly use your first item:")
    first_item = belt.pop(0)

    if first_item in good_loot_options:
        # Example: Increase HP by 2 (but cap at something, if you want)
        health_points = health_points + 2
        print(f"You used {first_item} to boost your health to {health_points}")
    elif first_item in bad_loot_options:
        # Decrease HP by 2 (but not below 0, if you want)
        health_points = max(0, (health_points - 2))
        print(f"You used {first_item} and it hurt your health to {health_points}")
    else:
        print(f"You used {first_item}, but it's not particularly helpful.")

    return belt, health_points

# ---------------------------------------------------------------------
# 5) inception_dream() - Recursive Function
#    - If user says yes, return 1 + inception_dream()
#    - If no, return 2 (base case)
# ---------------------------------------------------------------------
def inception_dream():
    deeper = input("Do you want to go deeper into the dream? (y/n): ").strip().lower()
    if deeper == 'y':
        return 1 + inception_dream()
    else:
        return 2