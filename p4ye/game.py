import random as r
import time as t

"""
ADD SOME KIND OF FOOD SYSTEM PROB, AND BUGTEST THIS POOP PROGRAM
"""



class game:
    hp = 20
    defe = 0
    crit_chance = 10
    crit_dmg = 1.5
    luck = 0
    input = ''
    weaprn = ''
    mob = ''

    weapDict = {}

    def __init__(self, mobHp=0, mobAttk=0, mobDefe=0, name='', addingWep=[], mobList=[], inv={}):
        self.mobHp = mobHp
        self.mobAttk = mobAttk
        self.mobDefe = mobDefe
        self.name = name
        self.addingWep = addingWep
        self.mobList = mobList
        self.mobList.append("goblin")
        self.inv = inv


    def naming(self):
        special_chara = "~!@#$%^&*()_+`{|}[]\:;<,>.?/*-'"
        c = 0
        if len(self.name) > 0:
            print("Rename?", "Type in no or yes", sep='\n')
            while True:
                gameinput = input('> ').lower().strip()
                if game.input == "yes":
                    break
                elif game.input == "no":
                    game.input = True
                else:
                    print("Please Type in yes or no", '\n')

        if game.input == True:
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
            game.input = input('> ').lower().strip()
            if game.input == "yes":
                return self.name
            elif game.input == "no":
                self.name = ''; print('\n')
                game.naming(self)
            else:
                print("Type in either yes or no")
                continue

                
    def help_ccmd(self):
        print("Type In cmd For Commands & stop to stop", "\n")
        t.sleep(0.5)
        while True:
            game.input = input('> ').lower().strip()
            if game.input == "cmd":
                print("""The Following Commands Are:

                        'Stats': To show your stats
                        'Inv': To show your inventory
                        'Adv': To start an adventure 
                        'Swi': To switch current weapon
                        """)
                t.sleep(1.0)
                continue
            if game.input == "stats":
                print("yay")
            elif game.input == "inv":
                for key, value in self.inv:
                   print(f'{key}:{value}')
                   t.sleep(0.075)
                   if key // 2 == float:
                       print('\n')
                   else:
                       print(sep='   ')
                break
            elif game.input == "adv":
                self.adventure(self, 1)
                break
            else: 
                print("Please type in a allowed command", '\n')
                continue

    def attk_RNGESUS(self):
        if game.crit_chance == 100:
            return game.weapDict.get(game.input) * game.crit_dmg - self.mobDefe
        for i in range(1 + game.crit_chance):
            chance = r.randint(1, 100)
            if chance == game.crit_chance:
                return game.weapDict.get(game.input) * game.crit_dmg - self.mobDefe
            else:
                print("No lucky...")
        return game.weapDict.get(game.input) - self.mobDefe 
    

    def defe_RNGESUS(self): 
        return self.mobAttk - game.defe
    
    
    def addingWeapons(self):
        if self.addingWep == 0:
            game.weapDict['fist'] = 2
        elif self.addingWep == 1:
            game.weapDict['stick'] = 3
        else:
            pass
        
    def selectWeapon(self):
            
        print(f"""_______________________________
                    {game.weapDict.get("Fist", '')} 
                    {game.weapDict.get("Stick", 'Not Yet Unlocked!')}
                  ________________________________""")
            
    def lootTables(self):
        if game.mob == 'goblin':
            for i in range(10+game.luck):
           #     self.inv.append("Place holder", 6) # This will defintely add a error

    def adventure(self, time):
        
        
        atk_RNGESUS = 0
        dee_RNGESUS = 0
        if time:
            self.mobHp = 10
            self.mobAttk = r.randint(1,3)
            self.mobDefe = 0
            self.selectWeapon()
            print("New Adventure!", '\n')
            print(f"Encountered 'Goblin'! || Hp: {self.mobHp}, Attk: {self.mobAttk}, Def: {self.mobDefe}") # For encountered goblin make some system that appends that enemy bc of that
            print("Type attack to attack your opponent!")
            game.mob = "goblin"
            while True:
                game.input = input('> ').lower().strip()
                if game.input == "attack":
                    atk_RNGESUS = game.attk_RNGESUS(self)
                    self.mobHp -= atk_RNGESUS
                    if self.mobHp <= 0:
                        break
                    else:
                        print(f"The goblin health is at {self.mobHp}")
                    dee_RNGESUS = game.defe_RNGESUS(self)
                    game.hp -= dee_RNGESUS
                    if game.hp <= 0:
                        break
                    else:
                        print(f"Oh no, your health is at {self.hp}")
                        continue
                else:
                    print("Please type in attack", '\n')
                    continue
                
                print("You have defeated the Goblin!")
                # Add some loot system here <------------------------- god so much work?
        else:
            pass # Add what after tutorial will look like



            
gaming = game()

def start():
    print('u live in cabin and want explore', 'choose name', '\n', sep='\n')
    name = gaming.naming()
    print(f'{name}, nice name, now go out in the world!')
    t.sleep(2.5)
    print("Type in adv to start an adventure!")
    gaming.adventure(1)
start()

