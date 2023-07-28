import random as r
import time as t

class game:

    possibleWeaponDict = ["Fist", "Rusty Sword", "Sword"]
    weapDict = {"Fist": 2}

    def __init__(self, mobHp, mobAttk, mobDefe, name, addingWep, mobList, inv):
        self.hp = 20
        self.defe = 0
        self.crit_chance = 10
        self.crit_dmg = 1.5
        self.luck = 0
        self.input = ''
        self.weaprn = ''
        self.mob = ''
        self.mobHp = mobHp
        self.mobAttk = mobAttk
        self.mobDefe = mobDefe
        self.name = name
        self.addingWep = addingWep
        self.mobList = mobList
        self.mobList.append("goblin")
        self.inv = inv


    def naming(self) -> str:
        special_chara = "~!@#$%^&*()_+`{|}[]\:;<,>.?/*-'="
        c = 0
        if len(self.name) > 1:
            print("Rename?", "Type in { yes } or { no }", sep='\n')
            while True:
                self.input = input('> ').lower().strip()
                if self.input == "yes":
                    break
                elif self.input == "no":
                    self.input = True
                else:
                    print("Please Type in { yes } or { no }", '\n')

        if self.input == True:
            pass

        t.sleep(1.5)
        print("Name?", "p.s. 1 - 12 characters long & no special characters", sep='\n')
        while True:
            self.name = input('> ')
            if len(self.name) <= 0:
                print("Retry", '\n')
                continue
            elif len(self.name) >= 13:
                print("Retry", '\n')
                continue
            else:
                self.name.split()
                for i in range(len(self.name)):
                    if self.name[i] in special_chara:
                        print("No Special Characters", '\n')
                        c += 1
                if c:
                    c -= 1
                    continue
                else:
                    print("Are You Sure? { yes } or { no }")

            while True:
                self.input = input('> ').lower()
                if self.input.strip() == "yes":
                    return self.name
                elif self.input == "no":
                    self.name = ''
                    print('\n', "Name?")
                    break
                else:
                    print("Type in either { yes } or { no")
                    continue

                
    def help_ccmd(self):
        print("Type In { help } For Commands", "\n")
        t.sleep(0.5)
        while True:
            self.input = input('> ').lower().strip()
            if self.input == "help":
                print("""The Following Commands Are:

                        'Stats': To show your stats
                        'Inv': To show your inventory
                        'Adv': To start an adventure 
                        'Swi': To switch current weapon
                        """)
                t.sleep(1.0)
                continue
            elif self.input == "stats":
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
               # self.(self, 1)      <------ change it
                break
            else: 
                print("Please type in a allowed command", '\n')
                continue

    def attk_RNGESUS(self) -> int:
        if self.crit_chance == 100:
            return self.weapDict.get(self.input) * self.crit_dmg - self.mobDefe
        for i in range(1 + self.crit_chance):
            chance = r.randint(1, 100)
            if chance == self.crit_chance:
                return self.weapDict.get(self.input) * self.crit_dmg - self.mobDefe
            else:
                print("No lucky...")
        return self.weapDict.get(self.input) - self.mobDefe 
    

    def defe_RNGESUS(self) -> int: 
        return self.mobAttk - self.defe
    
    
    def addingWeapons(self):
        if self.addingWep == 1:
            self.weapDict['Rusty Sword'] = 3 # maybe change to return instead appending
            pass
        elif self.addingWep == 2:
            self.weapDict['Sword'] = 5
            pass
        else:
            pass
        
    def selectWeapon(self):
        sel_wep = list(self.weapDict.keys())
        for xy in range(len(self.weapDict)):
            for y in range(len(self.possibleWeaponDict)):
                if sel_wep[xy] == self.possibleWeaponDict[y]: # Change the weapDict keys into a seperate list of keys
                    if xy == 0:
                        print("____________________________", '\n')
                    print(f"{sel_wep[xy]}")
                    if xy+1 == len(self.weapDict):
                        print("____________________________")
                        break


    def lootTables(self):
        if self.mob == 'goblin':
            for i in range(10+self.luck):
                if r.randint(1, 100) / 2 > 25:
                    self.inv.append("") # Add something here for like armor, what they drop (goblin teeth ish i dunnow), s-word

    def first_attk(self):
            self.mobHp = 10
            self.mobAttk = r.randint(1,3)
            self.mobDefe = 0
            self.selectWeapon()
            print("New Adventure!", '\n')
            print(f"Encountered 'Goblin'! || Hp: {self.mobHp}, Attk: {self.mobAttk}, Def: {self.mobDefe}") # For encountered goblin make some system that appends that enemy bc of that
            print("Type attack to attack your opponent!")
            self.mob = "goblin"
            while True:
                self.input = input('> ').lower().strip()
                if self.input == "attack":
                    self.mobHp -= self.attk_RNGESUS(self)
                    if self.mobHp <= 0:
                        break
                    else:
                        print(f"The goblin health is at {self.mobHp}")
                    self.hp -= self.defe_RNGESUS(self)
                    if self.hp <= 0:
                        break
                    else:
                        print(f"Oh no, your health is at {self.hp}")
                        continue
                else:
                    print("Please type in attack", '\n')
                    continue
                
            print("You have defeated the Goblin!")


class tutorial(game):
    def __init__(self):
        super().__init__(mobHp=0, mobAttk=0, mobDefe=0, name='', addingWep=[], mobList=[], inv={})
    
    def first_attk(self) -> int:
        self.mobHp = 10
        self.mobAttk = r.randint(1, 3)
        self.mobDefe = 0
        self.selectWeapon()
        print("New Adventure!", '\n')
        print(f"Encountered 'Goblin'! || Hp: {self.mobHp}, Attk: {self.mobAttk}, Def: {self.mobDefe}")
        print("Type attack to attack your opponent!")
        self.mob = "goblin"
        while True:
            self.input = input('> ').lower().strip()
            if self.input == "attack":
                self.mobHp -= self.attk_RNGESUS(self)
                if self.mobHp <= 0:
                    break
                else:
                    print(f"The goblin health is at {self.mobHp}")
                self.hp -= self.defe_RNGESUS(self)
                if self.hp <= 0:
                    break
                else:
                    print(f"Oh no, your health is at {self.hp}")
                    continue
            else:
                print("Please type in attack", '\n')
                continue

        print("You have defeated the Goblin!")


gaming = game(0, 0, 0, '', [], [], {})
start = tutorial()

def start():
    print('u live in cabin and want explore', 'choose name', '\n', sep='\n') 
    t.sleep(2.5)
    start.tutorial

start()
