import random as r
import time as t

import tools as tool

import sql_data as sql

# make gold a seperate variable
# maybe add a pet
# add more functions to tools.py cause this is getting overwhelming
class main:

    weapDict = {"fist": 2}
    gold = 0

    def __init__(self, mobHp, mobAttk, mobDefe, name, addingWep, mobList):
        """
        WE REALLY COULD JUST PUT THIS ALL INTO A SQL DATABASE INSTEAD OF REDEFINING IT EVERY TIME
        """
        self.hp = 50
        self.defe = 0
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
        self.inv = {}

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
            return "" # check if this actually works

        t.sleep(0.5)
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
            self.input = input('> ').lower()

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

                    tool.printingInv(self.inv)

                case "adv":
                    print("WIP")
                    break

                case _:
                    print("Please type in a allowed command", '\n')
                    continue

    def attk_RNGESUS(self, input: str) -> int:
        dice = r.randint(1, 12)
        counter = 1.0
        if dice >= 11:
            return [int(self.weapDict.get(input) ** 1.3 - self.mobDefe), 1, dice]
        
        while dice >= 6:
            counter += 0.045
            dice -= 1
            if dice < 6:
                return [int(self.weapDict.get(input) ** counter - self.mobDefe), 0, dice]

        while dice < 6:
            counter += 0.0475
            dice += 1
            if dice < 6:
                return [int(self.weapDict.get(input) - self.mobDefe ** counter), 0, dice]

    def defe_RNGESUS(self, attk: int, dice: int):
        print("does this actually appear")
        counter = 1.0
        if dice >= 11:
            return [int(attk ** 0.8 - self.defe)]
        
        while dice >= 6:
            counter -= 0.035
            dice -= 1
            if dice >= 6:
                print(int(attk-self.defe ** counter))
                return [int(attk - self.defe ** counter)] # MAYBE THE IF STATEMENT IS COMPLETEY IGRNOING TEH DICE >= 6

        while dice < 6:
            counter -= 0.040
            dice += 1
            if dice < 6:
                print(int(attk ** counter - self.defe))
                return [int(attk ** counter - self.defe)]

    def addingWeapons(self) -> dict:
        match self.addingWep: 
            case 1:
                return self.weapDict['Rusty Sword', 3]
            case 2:
                return self.weapDict['Sword', 5]

    def selectWeapon(self) -> None:
        possibleWeapList = ["fist", "goblin_sword"]
        sel_wep = list(self.weapDict.keys())
        for xy in self.weapDict:
            for y in possibleWeapList:
                if sel_wep[xy] == possibleWeapList[y]: # Change the weapDict keys into a seperate list of keys
                    if xy == 0:
                        print("____________________________", '\n')
                    print(f"{sel_wep[xy]}")
                    if xy+1 == len(self.weapDict):
                        print("____________________________")
                        break

    def insertingMobDrops(self, preinv: list) -> None:
        if self.mob == "goblin":
            for i in range(len(preinv)):

                match i:

                    case 0:
                        try:

                            if "goblin_hide" not in self.inv:
                                self.inv.update({"goblin_hide": 0})

                            self.inv["goblin_hide"] += preinv[i]

                        except Exception:
                            raise Exception("0st case")

                    case 1:
                        try:

                            if "goblin_leg" not in self.inv:
                                self.inv.update({"goblin_leg": 0})

                            self.inv["goblin_leg"] += preinv[i]

                        except Exception:
                            raise Exception("1st case")
                    case 2:
                        try:

                            if "goblin_sword" not in self.inv:
                                self.inv.update({"goblin_sword": 0})

                            self.inv["goblin_sword"] += preinv[i]

                        except Exception:
                            raise Exception("2nd case")

                    case 3:
                        try:

                            if "goblin_staff" not in self.inv:
                                self.inv.update({"goblin_staff": 0})

                            self.inv["goblin_staff"] += preinv[i]

                        except Exception:
                            raise Exception("3rd case")

                    case _:
                        raise Exception("oh no")
                    
    def main_attack(self) -> None:
        crit = None

        print(
            f"Encountered '{self.mob}'! || Hp: {self.mobHp}, Attk: {self.mobAttk}, Def: {self.mobDefe}")
        print("Type attack to attack your opponent!")

        maxHp = self.hp
        maxMobHp = self.mobHp

        while True:
            self.input = input('> ').lower()
            if self.input in ["attack", "atk", "attk", "q"]:

                attk = self.attk_RNGESUS("fist") # change this into the userinput
                defe = self.defe_RNGESUS(r.randint(2, 3), attk[2]) # change this r.randint, obv.

                if len(attk) == 2:
                    self.mobHp -= attk[0]
                    crit = attk[1]
                else:
                    self.mobHp -= attk[0]

                self.hp -= defe[0]

                if self.hp <= 0:
                    pass # do something about this

                if self.mobHp <= 0:
                    break

                else:
                    print("+===========================+",
                          f"% Rolled: {attk[2]}",
                          f"- Lost: {defe[0]}hp", sep='\n')

                if crit:
                    print(f"CRIT! Dealt: {attk[0]}hp",
                            f"Your Hp: {self.hp}/{maxHp}",
                            f"Enemy Hp: {self.mobHp}/{maxMobHp}", 
                            "+===========================+", 
                            sep='\n')
                    t.sleep(0.133)
                else:
                    print(f"+ Dealt: {attk[0]}hp",
                            f"Your Hp: {self.hp}/{maxHp}",
                            f"Enemy Hp: {self.mobHp}/{maxMobHp}", 
                            "+===========================+", 
                            sep='\n')
                    t.sleep(0.133)
            else:
                print("Please type in attack", '\n')
                continue

        print("You have defeated the Goblin!")


        preinv = tool.counting_drop(tool.drops(1, self.mob), self.mob)

        self.insertingMobDrops(preinv)
        tool.printingDrops(preinv, self.mob)


class starting_phase(main):
    def __init__(self):
        super().__init__(mobHp=10, mobAttk="2 - 3", mobDefe=0, name='', addingWep=[], mobList=[])

    def __repr__(self):
        return "Tutorial!"

    def main(self):
        crit = 0

        print(
            f"Encountered 'Goblin'! || Hp: {self.mobHp}, Attk: {self.mobAttk}, Def: {self.mobDefe}, Level: 1")
        print("Type attack to attack your opponent!")

        self.mob = "goblin"
        maxHp = self.hp
        maxMobHp = self.mobHp

        while True:
            self.input = input('> ').lower()
            if self.input in ["attack", "atk", "attk", "q"]:

                __attk = super().attk_RNGESUS("fist")
                print(__attk)
                __defe = super().defe_RNGESUS(r.randint(2, 3), __attk[2])

                print(__defe, __attk)

                if len(__attk) == 2:
                    self.mobHp -= __attk[0]
                    crit = __attk[1]
                else:
                    self.mobHp -= __attk[0]

                print(__attk[2])

                self.hp -= __defe[0]

                if self.hp <= 0:
                    quit("ERROR 1: Died unexpected")

                if self.mobHp <= 0:
                    break

                else:
                    print("+===========================+",
                          f"% Rolled: {__attk[2]}",
                          f"- Lost: {__defe[0]}hp", sep='\n')

                if crit:
                    print(f"CRIT! Dealt: {__attk[0]}hp",
                            f"Your Hp: {self.hp}/{maxHp}",
                            f"Enemy Hp: {self.mobHp}/{maxMobHp}", 
                            "+===========================+", 
                            sep='\n')
                    t.sleep(0.133)
                else:
                    print(f"+ Dealt: {__attk[0]}hp",
                            f"Your Hp: {self.hp}/{maxHp}",
                            f"Enemy Hp: {self.mobHp}/{maxMobHp}", 
                            "+===========================+", 
                            sep='\n')
                    t.sleep(0.133)
            else:
                print("Please type in attack", '\n')
                continue

        print("You have defeated the Goblin!")


        preinv = tool.counting_drop(tool.drops(1, self.mob), self.mob)

        super().insertingMobDrops(preinv)
        tool.printingDrops(preinv, self.mob)

if __name__ == "__main__":
    gaming = main(0, 0, 0, '', [], [])
    tutorial = starting_phase()

    def start():
        t.sleep(1)
        print(tutorial, "=========", sep='\n')
        print(gaming.defe_RNGESUS(10, 6))
        tutorial.main()
        print("Very cool, now ur ready for ur awesome gameplay")

    start()
