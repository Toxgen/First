import random as r
import time as t

"""
ADD SOME KIND OF FOOD SYSTEM PROB, AND BUGTEST THIS POOP PROGRAM
"""



class game:
    def __init__(self, hp=20, defe=1, mobHp=0, mobAttk=0, mobDefe=0, crit_chance=10, crit_dmg=1.5, input='', name='', addingWep=[], mobList=[], inv={}, weapDict={}):
        self.hp = hp
        self.defe = defe
        self.mobHp = mobHp
        self.mobAttk = mobAttk
        self.mobDefe = mobDefe
        self.crit_chance = crit_chance
        self.crit_dmg = crit_dmg
        self.input = input
        self.name = name
        self.addingWep = addingWep
        self.mobList = mobList
        self.mobList.append("goblin")
        self.inv = inv
        self.weapDict = weapDict
        self.weapDict['fist'] = r.randint(1, 3)


    def naming(self):
        special_chara = "~!@#$%^&*()_+`{|}[]\:;<,>.?/*-'"
        c = 0
        if len(self.name) > 0:
            print("Rename?", "Type in no or yes", sep='\n')
            while True:
                self.input = input('> ').lower().strip()
                if self.input == "yes":
                    break
                elif self.input == "no":
                    self.input = True
                else:
                    print("Please Type in yes or no", '\n')

        if self.input == True:
            pass
        t.sleep(1.5)
        print("Name?", "p.s. 3 - 10 characters long & no special characters", sep='\n')
        while True:
            self.name = input('Name: ')
            if len(self.name) <= 2:
                print("Retry", '\n')
                continue
            elif len(self.name) >= 11:
                print("Retry", '\n')
                continue
            else:
                self.name.split()
                for i in range(len(self.name)):
                    if self.name[i] in special_chara:
                        print("No Special Characters", '\n')
                        c += 1
                        break
                if c:
                    c -= 1
                    continue
                else:
                    print("Are You Sure? Yes or No")
                    break

        while True:
            self.input = input('> ').lower().strip()
            if self.input == "yes":
                return self.name
            elif self.input == "no":
                self.name = ''; print('\n')
                game.naming(self)
            else:
                print("Type in either yes or no")
                continue

                
    def help_ccmd(self):
        print("Type In cmd For Commands & stop to stop", "\n")
        t.sleep(0.5)
        while True:
            self.input = input('> ').lower().strip()
            if self.input == "cmd":
                print("""The Following Commands Are:

                        'Stats': To show your stats
                        'Inv': To show your inventory
                        'Adv': To start an adventure 
                        'Swi': To switch current weapon
                        """)
                t.sleep(1.0)
                continue
            if self.input == "stats":
                print("yay")
            elif self.input == "inv":
                for key, value in self.inv:
                   print(f'{key}:{value}')
                   t.sleep(0.075)
                   if key // 2 == float:
                       print('\n')
                   else:
                       print(sep='   ')
                break
            elif self.input == "adv":
                self.adventure(self, 1)
                break
            else: 
                print("Please type in a allowed command", '\n')
                continue

    def attk_RNGESUS(self):
        if self.crit_chance == 100:
            return self.weapDict.get(self.input) * self.crit_dmg - self.mobDefe
        for i in range(1 + self.crit_chance):
            chance = r.randint(1, 100)
            if chance == self.crit_chance:
                return self.weapDict.get(self.input) * self.crit_dmg - self.mobDefe
        
        return self.weapDict.get(self.input) - self.mobDefe 
    

    def defe_RNGESUS(self): # Add critcal chance for mob?
        return self.mobAttk - self.defe
    
    
    def addingWeapons(self):
        if self.addingWep == 0:
            self.weapDict['fist'] = 2
        elif self.addingWep == 1:
            self.weapDict['stick'] = 3
        else:
            pass


    def adventure(self, time): # somehow return something true if critical like make variable inside function and in the attacking function make it true
        
        
        atk_RNGESUS = 0
        dee_RNGESUS = 0
        if time:
            self.mobHp = 10
            self.mobAttk = r.randint(1,3)
            self.mobDefe = 0

            print("New Adventure!", '\n') # for line 149 maybe add like add a list of mobs possible for that area, maybe even add a photo???. like make a character hased photo i dunnk
            print(f"Encountered 'Goblin'! || Hp: {self.mobHp}, Attk: {self.mobAttk}, Def: {self.mobDefe}") # For encountered goblin make some system that appends that enemy bc of that
            print("Type attack to attack your opponent!")
            while True:
                self.input = input('> ').lower().strip()
                if self.input == "attack":
                    atk_RNGESUS = game.attk_RNGESUS(self)
                    self.mobHp -= atk_RNGESUS
                    if self.mobHp <= 0:
                        break
                    else:
                        print(f"The goblin health is at {self.mobHp}")
                    dee_RNGESUS = game.defe_RNGESUS(self)
                    self.hp -= dee_RNGESUS
                    if self.hp <= 0:
                        break
                    else:
                        print(f"Oh no, your health is at {self.hp}")
                else:
                    print("Please type in attack", '\n')
                
                print("You have defeated the Goblin!")
                # Add some loot system here <------------------------- god so much work?
        else:
            pass # Add what after tutorial will look like



            
gaming = game()

def start():
    print('u live in cabin and want explore', 'choose name', '\n', sep='\n') # obv gotta change this, but really just focus oj bugs first
    name = gaming.naming()
    print(f'{name}, nice name, now go out in the world!')
    t.sleep(2.5)
    print("Type in adv to start an adventure!")
    gaming.adventure(1)
start()

