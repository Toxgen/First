import random as r
import time as t

"""
TYPE IN YES TWICE QUICK: DIDNT REGISTER SOMEHOW I DUNNO
"""



class game:

    def __init__(self, hp, defe, mobHp, mobAttk, mobDefe, input, name, mobList, inv, weapDict):
        self.hp = hp
        self.defe = defe
        self.mobHp = mobHp
        self.mobAttk = mobAttk
        self.mobDefe = mobDefe
        self.input = input
        self.name = name
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
            if len(self.name) > 11:
                print("Too Long, Retry", '\n')
                continue
            elif len(self.name) < 2:
                print("Too Short, Retry", '\n')
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
        return self.weapDict.items()[0] - self.mobDefe # Make this a user selected weapon, but currently too many things to worry about rn
    def defe_RNGESUS(self):
        return self.mobAttk - self.defe

    def adventure(self, time):
        atk_RNGESUS = 0
        dee_RNGESUS = 0
        self.mobList.append("goblin") # add all enemies
        if time == 0:
            for q in range(len(self.mobList)):
                if 'goblin' in self.mobList[q]:
                    self.mobHp = 10
                    self.mobAttk = r.randint(1,3)
                    self.mobDefe = 1

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
            
gaming = game(20, 1, 0, 0, 0, '', '', list(), dict(), ('fist', r.randint(1,3)))

def start():
    print('u live in cabin and want explore', 'choose name', '\n', sep='\n')
    name = gaming.naming()
    print(f'{name}, nice name, now go out in the world!')
    t.sleep(2.5)
    print("Type in adv to start an adventure!")
    gaming.adventure(0)
start()

