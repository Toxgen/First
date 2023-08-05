import random as r
import time as t

import tools as tool

class main:

    possibleWeaponDict = ["Fist", "Rusty Sword", "Sword"]
    weapDict = {"Fist": 2}

    def __init__(self, mobHp, mobAttk, mobDefe, name, addingWep, mobList, inv):
        self.hp = 20
        self.defe = 0
        self.crit_chance = 100
        self.crit_dmg = 1.5
        self.luck = 5
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
        self.inv = [[], [], [], [], [], [], []]


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

        if self.input:
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

                
    def help_ccmd(self) -> None:
        print("Type In { help } For Commands", "\n")
        t.sleep(0.5)
        while True:
            self.input = input('> ').lower().strip()
            match self.input:

                case "help":
                    print("""The Following Commands Are:

                            'Stats': To show your stats
                            'Inventory or inv': To show your inventory
                            'Adventure or adv': To start an adventure 
                            'Switch or swi': To switch current weapon
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
    
    
    def addingWeapons(self) -> dict:
        match self.addingWep: # Prob move this
            case 1:
                return self.weapDict['Rusty Sword', 3]
            case 2:
                return self.weapDict['Sword', 5]
        
    def selectWeapon(self) -> None:
        sel_wep = list(self.weapDict.keys())
        for xy in self.weapDict:
            for y in self.possibleWeaponDict: # make possibleweapondict a local variable wirhour self.
                if sel_wep[xy] == self.possibleWeaponDict[y]: # Change the weapDict keys into a seperate list of keys
                    if xy == 0:
                        print("____________________________", '\n')
                    print(f"{sel_wep[xy]}")
                    if xy+1 == len(self.weapDict):
                        print("____________________________")
                        break

    def insertingMobDrops(self, placeholder: list) -> None:
        if self.mob == "goblin":
            for i in range(len(placeholder)):

                match i:

                    case 0:
                        try:
                            
                            self.inv[0].insert(0, "goblin_hide")
                            self.inv[0].insert(1, placeholder[i])
                        
                        except Exception:
                            raise Exception("0st case")

                    case 1:
                        try:
                        
                            self.inv[1].insert(0, "goblin_leg")
                            self.inv[1].insert(1, placeholder[i])

                        except Exception:
                            raise Exception("1st case")
                    case 2:
                        try:

                            self.inv[2].insert(0, "goblin_sword")
                            self.inv[2].insert(1, placeholder[i])

                        except Exception:
                            raise Exception("2nd case")

                    case 3:
                        try:

                            self.inv[3].insert(0, "goblin_staff")
                            self.inv[3].insert(1, placeholder[i])
                        
                        except Exception:
                            raise Exception("3rd case")

                    case _:
                        print("OH NAHHHHHHHHHHHHHHHHHHHHH")
                        while True:
                            raise ChildProcessError("NOOOOOOOOOOOOOOOOOOOOOOOOOO")
                        
            while [] in self.inv: # Removes all the nested lists
                self.inv.remove([])
        
                
class starting_phase(main):
    def __init__(self):
        super().__init__(mobHp=10, mobAttk="2 - 3", mobDefe=0, name='', addingWep=[], mobList=[], inv=[])

    def __repr__(self):
        return "Tutorial!"

    def main(self):
        crit = 0

        
        print(f"Encountered 'Goblin'! || Hp: {self.mobHp}, Attk: {self.mobAttk}, Def: {self.mobDefe}, Level: 1")
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
                        t.sleep(0.133)
                    else:
                        print("+===========================+",
                              f"Enemy Hp: {self.mobHp} || Dmg: {i[0]}", sep='\n')
                        t.sleep(0.133)
                
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

        loots = tool.drops(1, 100)
        placeholder = tool.counting_drop(loots, self.mob)

        super().insertingMobDrops(placeholder)
        for q in range(len(placeholder)): 

            match q:

                case 0:
                    if placeholder[q] > 1:
                        print("+=======================+",
                            f"Earned {placeholder[q]} goblin_hides", sep='\n')
                    else:
                        print("+=======================+",
                            f"Earned {placeholder[q]} goblin_hide", sep='\n')
                        
                    t.sleep(0.33)
                    continue
                
                case 1:
                    if placeholder[q]:
                        if placeholder[q] > 1:
                            print(f"Earned {placeholder[q]} goblin_legs")
                        else:
                            print(f"Earned {placeholder[q]} goblin_leg")

                        t.sleep(0.33)
                    continue

                case 2:
                    if placeholder[q]:
                        if placeholder[q] > 1:
                            print(f"Earned {placeholder[q]} goblin_swords")
                        else:
                            print(f"Earned {placeholder[q]} goblin_sword")

                        t.sleep(0.33)
                    continue

                case 3:
                    if placeholder[q]:
                        if placeholder[q] > 1:
                            print(f"Earned {placeholder[q]} goblin_staffs", 
                                    "+=======================+", sep='\n')
                        else:
                            print(f"Earned {placeholder[q]} goblin_staff",
                                  "+=======================+", sep='\n')
                    else:
                        print("+=======================+")
                            
                        t.sleep(0.33)
        print(self.inv)

if __name__ == "__main__":
    gaming = main(0, 0, 0, '', [], [], [[], [], [], []])
    tutorial = starting_phase()

    def start():
        t.sleep(1)
        print(tutorial, "=========", sep='\n')
        tutorial.main()

    start()
