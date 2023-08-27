import random as r
import time as t

import tools as tool

import sql_data as sql

"""
Tutorial has to return something
PLEASE SQL WORK
what is this not registering
"""
class main:

    weapDict = {"fist": 2}
    gold = 0

    @staticmethod
    def sqlParseQuery(connection):
        sql.execute_query(connection=connection, query="""
                          SELECT * FROM stats;
                          SELECT id FROM stats WHERE id > 3 LIMIT 4;
                          SELECT FOUND_ROWS();""")
        

    def __init__(self, name):
        self.hp = 50
        self.defe = 0
        self.input = ''
        self.ccWeap = ''
        self.xp_sys = [0, 4, 0]
        self.name = name
        self.inv = {}
        self.location = "woods"

    def xp(self) -> None:
        cc_level = self.xp_sys[0]

        self.xp_sys[0] = 0
        print(round(1.5 * (cc_level ** 1.15)))

        if round(1.5 * (cc_level ** 1.15)) <= self.xp_sys[1]:
            self.xp_sys[0] += 1
        
        while self.xp_sys[2] > round(1.5 * (self.xp_sys[0] ** 1.15) + 10):
            self.xp_sys[0] += 1
                    
        if cc_level > self.xp_sys[0]:
            print(f"Congrats! You gained {self.xp_sys[0] - cc_level}")
            
    def naming(self) -> (str | None):
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
            return None

        t.sleep(0.5)
        print("Name?", "p.s. 1 - 12 characters long & no special characters", sep='\n')

        while True:
            self.name = input('> ').strip()
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
                    print("Type in either { yes } or { no }")
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

    def attk_RNGESUS(self, input: str, defe: int) -> int:
        dice = r.randint(1, 12)
        dice2 = dice
        counter = 1.0
        
        if dice2 >= 11:
            return [round(self.weapDict.get(input) ** 1.75 - defe) + 2, 1, dice]
        
        while dice2 >= 6:
            counter += 0.1
            if dice2 == 6:
                return [round(self.weapDict.get(input) ** counter - defe) + 1, 0, dice]
            dice2 -= 1

        while dice2 <= 6:
            counter -= 0.1
            if dice2 == 6: # maybe add something if only it was lower than >2 or >3
                return [round(self.weapDict.get(input) ** counter - defe) - 1, 0, dice]
            dice2 += 1

    def defe_RNGESUS(self, attk: int, dice: int) -> int:
        counter = 1.0
        
        if dice >= 11:
            return [round((attk ** 0.6) - (self.defe + 2))]
        
        while dice >= 6:
            counter -= 0.0325
            if dice >= 6:
                return [round((attk ** counter) - (1 + self.defe))]
            dice -= 1

        while dice < 6:
            counter += 0.03
            if dice < 6:
                return [round((attk ** counter) - (self.defe - 1))]
            dice += 1

    def selectWeapon(self) -> None:
        possibleWeapList = ["fist", "goblin_sword"] # maybe just throw this into a database or something to that 
        # extent with other varibles similar to this, for organization
        sel_wep = list(self.weapDict.keys())
        for xy in self.weapDict:
            for y in possibleWeapList:
                if sel_wep[xy] == possibleWeapList[y]:
                    if xy == 0:
                        print("____________________________", '\n')
                    print(f"{sel_wep[xy]}")
                    if xy+1 == len(self.weapDict):
                        print("____________________________")
                        break

    def insertingMobDrops(self, preinv: list, mob: str) -> None: # how would you transform this into the tools.py bc this takes a space
        # possibly search up a function that gets what it returns and then adds it on this main class
        if mob == "goblin": # match case
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
        mob_list = tool.returnMob(self.hp, "woods") # Woods for now, but implement a system later

        mob = mob_list[0]
        mobHp = mob_list[1]
        mobAttk = [x for x in mob_list if 2 in x if 3 in x] 
        mobDefe = mob_list[4]
            
        print(
            f"Encountered '{mob}'! || Hp: {mobHp}, Attk: {mobAttk[0]} - {mobAttk[1]}, Def: {mobDefe}")
        print("Type attack to attack your opponent!")

        maxHp = self.hp
        maxMobHp = mobHp

        while True:
            self.input = input('> ').lower()
            if self.input in ["attack", "atk", "attk", "q"]:

                attk = self.attk_RNGESUS(self.ccWeap, mobDefe)
                mobDefe = self.defe_RNGESUS(r.randint(mobAttk[0], mobAttk[1]), attk[2])

                if len(attk) == 2:
                    mobHp -= attk[0]
                    crit = attk[1]
                else:
                    mobHp -= attk[0]

                self.hp -= mobDefe[0]

                if self.hp <= 0:
                    quit("WIP")

                if mobHp <= 0:
                    break

                else:
                    print("+===========================+",
                          f"% Rolled: {attk[2]}",
                          f"- Lost: {mobDefe[0]}hp", sep='\n')

                if crit:
                    print(f"CRIT! Dealt: {attk[0]}hp",
                            f"Your Hp: {self.hp}/{maxHp}",
                            f"Enemy Hp: {mobHp}/{maxMobHp}", 
                            "+===========================+", 
                            sep='\n')
                    t.sleep(0.133)
                else:
                    print(f"+ Dealt: {attk[0]}hp",
                            f"Your Hp: {self.hp}/{maxHp}",
                            f"Enemy Hp: {mobHp}/{maxMobHp}", 
                            "+===========================+", 
                            sep='\n')
                    t.sleep(0.133)
            else:
                print("Please type in attack", '\n')
                continue

        print("You have defeated the Goblin!") # akso gotta change this cause u dont always be defeating goblins


        preinv = tool.counting_drop(tool.drops(1, mob), mob)

        self.insertingMobDrops(preinv)
        tool.printingDrops(preinv, mob)


class starting_phase(main):
    def __init__(self):
        super().__init__(name='')

    def __repr__(self):
        return "Tutorial!"

    def start(self) -> list:
        crit = 0

        __mobHp = 10
        mobAttk = "2 - 3"
        __mobDefe = 0

        print(
            f"Encountered 'Goblin'! || Hp: {__mobHp}, Attk: {mobAttk}, Def: {__mobDefe}, Level: 1")
        print("Type attack to attack your opponent!")

        self.mob = "goblin"
        maxHp = self.hp
        maxMobHp = __mobHp

        while True:
            self.input = input('> ').lower()
            if self.input in ["attack", "atk", "attk", "q"]:

                __attk = super().attk_RNGESUS("fist", __mobDefe)
                __defe = super().defe_RNGESUS(r.randint(2, 3), __attk[2])


                if len(__attk) == 2:
                    __mobHp -= __attk[0]
                    crit = __attk[1]
                else:
                    __mobHp -= __attk[0]
                    
                self.hp -= __defe[0]

                if self.hp <= 0:
                    quit("ERROR 1: Died unexpected")

                if __mobHp <= 0:
                    break

                else:
                    print("+===========================+",
                          f"% Rolled: {__attk[2]}",
                          f"- Lost: {__defe[0]}hp", sep='\n')

                if crit:
                    print(f"CRIT! Dealt: {__attk[0]}hp",
                            f"Your Hp: {self.hp}/{maxHp}",
                            f"Enemy Hp: {__mobHp}/{maxMobHp}", 
                            "+===========================+", 
                            sep='\n')
                    t.sleep(0.133)
                else:
                    print(f"+ Dealt: {__attk[0]}hp",
                            f"Your Hp: {self.hp}/{maxHp}",
                            f"Enemy Hp: {__mobHp}/{maxMobHp}", 
                            "+===========================+", 
                            sep='\n')
                    t.sleep(0.133)
            else:
                print("Please type in attack", '\n')
                continue

        print("You have defeated the Goblin!")

        preinv = tool.counting_drop(tool.drops(1, self.mob), self.mob)

        super().insertingMobDrops(preinv, "goblin")
        print("+=====================+",
              "You gained 4 xp!",
              "+=====================+", sep="\n")
        tool.printingDrops(preinv, self.mob)

        return [self.hp, preinv]

if __name__ == "__main__":

    connection = sql.create_server_connection("localhost", "root", sql.pw)
    sql.create_db_connection("localhost", "root", sql.pw, "rpg_stats")
    #main.sqlParseQuery(connection)

    main = main("")
    tutorial = starting_phase()

    t.sleep(1)
    print(tutorial, "=========", sep='\n')
    tutorial.start()
    print("Very cool, now ur ready for ur awesome gameplay") # add some more text after this