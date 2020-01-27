import random
#!/usr/bin/env python

# In this simple RPG game, the hero fights the goblin. He has the options to:

# 1. fight goblin
# 2. do nothing - in which case the goblin will attack him anyway
# 3. flee

class Character:
    def __init__(self, name, health, power, probability):
        self.name = name
        self.health = health
        self.power = power
        self.probability = probability
        

    def attack(self, other_attacked):
        if(random.random() <= self.probability):
            damage = self.power * 2
            print("Attack power doubled")
        else:
            damage = self.power
            print("Attack WAS NOT doubled ")
        if(other_attacked.name == "Shadow"):
            if(random.random() >= self.probability):
                damage = 0 
                print("Shadow has dodged ")
        other_attacked.health -= damage
        
            
            
        
        
        
    def alive(self):
        if(self.health > 0):
            return True
        else:
            print(f' {self} is alive {self.health}')
            return False 
    def print_status(self):
        print(f'You have {self.health} health and {self.power} power.')


class Hero(Character): #DONT FORGET YOU PUT HEALTH AND POWER AS STRINGS
    pass
    # def __init__(self, health, power):
     
        # super().__init__(health, power)
        
        

    # def attack(self, other_guy):
    #     other_guy.health -= self.power
    # def alive(self):
    #     if(self.health > 0):
    #         return True
    #     else:
    #         print(f' Hero is alive {self.health}')
    #         return False 
    # def print_status(self):
    #     print(f'You have {self.health} health and {self.power} power.')






class Goblin(Character):
    pass
    # def __init__ (self, health, power):
    #     super().__init__(health, power)
    # def attack(self, hero_attacked):
    #     hero_attacked.health -= self.power
    # def alive(self):
    #     if(self.health > 0):
    #         return True
    #     else:
    #         print(f' Goblin is not alive {self.health}')
    #         return False
             
    # def print_status(self, health, power):
    #     print(f'You have {self.health} health and {self.power} power.')
 
class Medic(Character):
    def medic_health(self):
        if(random.random() <= self.probability):
            self.health += 2
            print("Health recuperated ")
        else:
            print("Health did not recuperate")
    def attack(self, other_guy): # You have your own attack method here because of the minor differences. You're just adding something onto it.
        self.medic_health()
        super().attack(other_guy)

class Shadow(Character):
    pass
        


class Zombie(Character):
    def zombie_Health(self, heros_attack ):
        heros_attack.power = 0



        




            

Meryem = Hero("Meryem",40 , 20, 0.2)
Marhab = Goblin("Marhab",60, 10, 0.0)
Medic = Medic("Medic",90, 20, 0.2) #This is an obj of medic class. Medic class is the child of the Character class
# So self in Medic class will refer to the Medic character.
Shadow = Shadow("Shadow", 1, 20, .1)
Zombie = Zombie("Zombie", float('inf'), 10, 0.0)

def the_battle(enemy, hero):
        while enemy.alive() and hero.alive():
            print()
            print("What do you want to do?")
            print(f"1. fight {enemy.name}")
            print("2. do nothing")
            print("3. flee")
            print("> ", end=' ')
            raw_input = input()
            if raw_input == "1":
                # Hero attacks goblin
                hero.attack(enemy)
                print("You do {} damage to the enemy.".format(hero.power))
                if enemy.alive():
                    print("Bastard is alive ")
                else:
                    print("He is dead")
            elif raw_input == "2":
                pass
            elif raw_input == "3":
                print("Goodbye.")
                break
            else:
                print("Invalid input {}".format(raw_input))

            if enemy.health > 0:
                # Goblin attacks hero
                enemy.attack(hero)
                print(f'The {enemy.name} does {enemy.power} damage to you.')
                print(hero.alive())
                if hero.health > 0:
                    print("You are alive ")
                elif hero.health == 0:
                    print ("Play again ")
def main():
    choice = input("Press 1 to fight Marhab,\n Press 2 to fight Medic,\n Press 3 to fight Shadow,\n Press 4 to fight Zombie ")
    if(choice == "1"):
        enemy = Marhab
    elif(choice == "2"):
        enemy = Medic
    elif(choice == "3"):
        enemy = Shadow
    elif(choice == "4"):
        enemy = Zombie
    else:
        print("Pick 1 or 2 or 3, or 4")
    hero = Meryem
    the_battle(enemy, hero)





main()
