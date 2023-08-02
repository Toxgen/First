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
        c = None
        
        if self.name:
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

        t.sleep(0.5); print("Name?", "p.s. 1 - 12 characters long & no special characters", sep='\n')

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
                for i in self.name:
                    if self.name[i] in special_chara:
                        print("No Special Characters", '\n')
                        c = True
                if c:
                    c = False
                    continue
                else:
                    t.sleep(0.22)
                    print("Are You Sure? { yes } or { no }")

            while True:
                self.input = input('> ').lower()
                if self.input.strip() == "yes":
                    t.sleep(0.3333)
                    return str(self.name)
                elif self.input == "no":
                    self.name = ''
                    print("Name?", sep='\n')
                    break
                else:
                    print("Type in either { yes } or { no")
                    continue

                
    def help_ccmd(self):
        print("Type In { help } For Commands", "\n")
        t.sleep(0.5)
        while True:
            self.input = input('> ').lower().strip()
            match self.input:

                case "help":
                    print("""The Following Commands Are:

                            'Stats': To show your stats
                            'Inv': To show your inventory
                            'Adv': To start an adventure 
                            'Swi': To switch current weapon
                            """)
                    t.sleep(1.0)
                    continue

                case "stats":
                    print("WIP")
                    break

                case "inv":
                    for key, value in self.inv:
                        print(f'{key}:{value}')
                        t.sleep(0.075)
                        if key // 2 == float:
                            print('\n')
                        else:
                            print(sep='   ')

                case "adv":
                    print("WIP")
                    break

                case _: 
                    print("Please type in a allowed command", '\n')
                    continue


    def attk_RNGESUS(self, input: str) -> int: # it might return a decimal :/
        if self.crit_chance == 100:
            return [int(self.weapDict.get(input) * self.crit_dmg - self.mobDefe), 1]
        for i in range(5 + self.crit_chance):
            chance = r.randint(13, 90)
            
            if chance == 89:
                return [int(self.weapDict.get(input) * self.crit_dmg - self.mobDefe), 1]
            
        return [int(self.weapDict.get(input) - self.mobDefe)]
    

    def defe_RNGESUS(self, attk: int) -> int: 
        return [int(attk - self.defe)]
        # Add special effects like posion or smth to that extent
    
    
    def addingWeapons(self):
        # maybe do match?
        if self.addingWep == 1:
            return self.weapDict['Rusty Sword', 3]
        elif self.addingWep == 2:
            return self.weapDict['Sword', 5]
        else:
            pass
        
    def selectWeapon(self):
        sel_wep = list(self.weapDict.keys())
        for xy in self.weapDict:
            for y in self.possibleWeaponDict:
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

    def adventure(self):
        pass
           

class tutorial(game):
    def __init__(self):
        super().__init__(mobHp=10, mobAttk="2 - 3", mobDefe=0, name='', addingWep=[], mobList=[], inv={})

    def __repr__(self):
        return "Tutorial!"

    def main(self) -> int:
        crit = 0

        print(f"Encountered 'Goblin'! || Hp: {self.mobHp}, Attk: {self.mobAttk}, Def: {self.mobDefe}")
        print("Type attack to attack your opponent!")
        self.mob = "goblin"
        while True:
            self.input = input('> ').lower()
            if self.input in ["attack", "atk", "attk", "q"]: # "q"
                i = super().attk_RNGESUS("Fist")

                if len(i) == 2:
                    self.mobHp -= i[0]
                    crit = i[1]
                else:
                    self.mobHp -= i[0]

                if self.mobHp <= 0:
                    break
                else:
                    if crit:
                        print("+===========================+",
                            f"Enemy Hp: {self.mobHp}", f"CRITCAL HIT! {i[0]} DMG", sep='\n')
                    else:
                        print("+===========================+",
                              f"Enemy Hp: {self.mobHp} || Dmg: {i[0]}", sep='\n')
                
                i = super().defe_RNGESUS(r.randint(2, 3))
                self.hp -= i[0]

                if self.hp <= 0:
                    break
                else:
                    print(f"Hp: {self.hp} || Dmg: {i[0]}",
                          "+===========================+", sep='\n')
                    continue
            else:
                print("Please type in attack", '\n')
                continue

        print("You have defeated the Goblin!")
       # super.

if __name__ == "__main__":
    gaming = game(0, 0, 0, '', [], [], {})
    tutorial = tutorial()

    def start():
        t.sleep(1)
        print(tutorial, "=========", sep='\n')
        tutorial.main()

    start()
