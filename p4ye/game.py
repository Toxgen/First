import random as r
import time as t

"""
TYPE IN YES TWICE QUICK: DIDNT REGISTER SOMEHOW I DUNNO
"""



class game:
    def __init__(self, hp, defe, mobHp, mobAttk, mobDefe, luck, input, name, addingWep, mobList, inv, weapDict):
        self.hp = hp
        self.defe = defe
        self.mobHp = mobHp
        self.mobAttk = mobAttk
        self.mobDefe = mobDefe
        self.luck = luck
        self.input = input
        self.name = name
        self.addingWep = addingWep
        self.mobList = mobList
        self.inv = inv
        self.weapDict = weapDict


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
        while True:
            self.input = input('> ').lower().strip()
            if self.input == "cmd":
                print("""The Following Commands Are:

                        'Stats': To show your stats
                        'Inv': To show your inventory
                        'Adv': To start an adventure 
                        """)
                t.sleep(1.0)
            if self.input == "stats":
                print("yay")
            elif self.input == "inv":
               for key, value in self.inv:
                   print(f'{key}:{value}')
                   if key // 2 == float:
                       print('\n')
                   else:
                       print(sep='   ')
            elif self.input == "adv":
                print("YAY")
            else: 
                if self.input == 'cmd':
                    continue
                else:
                    print("Please type in a allowed command", '\n', self.input)
                continue

    def attk_RNGESUS(self):
        print("Which weapons would you like to attack with?", self.weapDict.keys(), sep='\n', end='\n') # scoot this down to the adventure(self)
        while True:
            self.input = input('> ').lower().strip()
            if self.input == 'fist' and self.addingWep >= 0:
                print("ok")
                break
            elif self.input == "stick":
                if self.addingWep >= 1:
                    print("ok")
                    break
                else:
                    print("you have yet to obtain this yet, retry", '\n')
                    continue
            else:
                print("Type in a valid weapon")
                
        return self.weapDict.get(self.input) + r.randint(self.luck, self.luck + 3) - self.mobDefe  # Maybe add something like critcal hit 
    
    def defe_RNGESUS(self):
        return self.mobAttk - self.defe
    def addingWeapons(self):
        if self.addingWep == 0:
            self.weapDict['fist'] = 2
        elif self.addingWep == 1:
            self.weapDict['stick'] = 3
        else:
            pass
    def adventure(self, time):
        atk_RNGESUS = 0
        dee_RNGESUS = 0
        self.mobList.append("goblin") # add all enemies
        self.weapDict['fist'] = r.randint(1, 3)
        if time == 0:
            for q in range(len(self.mobList)):
                if 'goblin' in self.mobList[q]:
                    self.mobHp = 10
                    self.mobAttk = r.randint(1,3)
                    self.mobDefe = 0

            print("New Adventure!", '\n')
            print(f"Encountered 'Goblin'! || Hp: {self.mobHp}, Attk: {self.mobAttk}, Def: {self.mobDefe}") # For encountered goblin make some system that appends that enemy bc of that
            print("Type attack to attack your opponent!")
            while True:
                self.input = input('> ').lower().strip()
                if self.input == "attack":
                    atk_RNGESUS = game.attk_RNGESUS(self)
                    self.mobHp -= atk_RNGESUS
                    print(f"The goblin health is at {self.mobHp}")
                    dee_RNGESUS = game.defe_RNGESUS(self)
                    self.hp -= dee_RNGESUS
                    print(f"Oh no, your health is at {self.hp}")
                else:
                    print("Please type in attack", '\n')

            
gaming = game(20, 1, 0, 0, 0, 0, '', '', 0, list(), dict(), dict())

def start():
    print('u live in cabin and want explore', 'choose name', '\n', sep='\n')
    name = gaming.naming()
    print(f'{name}, nice name, now go out in the world!')
    t.sleep(2.5)
    print("Type in adv to start an adventure!")
    gaming.adventure(0)
start()

