import random as r
from random import randint

import time as t
from time import sleep


def drops(level: int, luck: int, mob: str) -> list:
    """
    very complicated drops
    (the mob level, self.luck, self.mob)
    """

    match mob:

        case "goblin":

            returning = []
            
            if level > 40:
                pass
            elif level > 30:
                pass
            elif level > 20:
                pass
            elif level > 10:
                pass
            else:
                pass
                
            for i in range(luck):

                if not i: # guaranteed 1
                    returning.append("goblin_hide")

                x = r.randint(0, 100)

                if len(returning) >= 3:
                    x = r.randint(0, 150)

                if x <= 5:  
                    returning.append("goblin_staff")
                    continue

                if x <= 8:  
                    returning.append("goblin_sword")
                    continue

                if x <= 12:  
                    returning.append("goblin_leg")
                    continue

                if x <= 25: 
                    returning.append("goblin_hide")
                    continue

            return returning

        case _:
            raise Exception("1st: Oh NAHHHHHHHHHHHHHHHHH")

            
            

def counting_drop(list: list, mob: str):
    """
    count em
    (the drops, self.mob)
    """

    match mob:

        case "goblin":
            g_hide = list.count("goblin_hide")

            g_leg = list.count("goblin_leg")
            
            g_sword = list.count("goblin_sword")

            g_staff = list.count("goblin_staff")

            return [g_hide, g_leg, g_sword, g_staff]
    
        case _:
            raise Exception("2nd: UH OH")
        
def printingDrops(preinv: list, mob: str):
    """
    print em drops
    (the counted drop list, self.mob)
    """

    match mob:

        case "goblin":

            for q in range(len(preinv)):

                match q:

                        case 0:
                            if preinv[q] > 1:
                                print("+=======================+",
                                    f"Earned {preinv[q]} goblin_hides", sep='\n')
                            else:
                                print("+=======================+",
                                    f"Earned {preinv[q]} goblin_hide", sep='\n')

                            t.sleep(0.33)
                            continue

                        case 1:
                            if preinv[q]:
                                if preinv[q] > 1:
                                    print(f"Earned {preinv[q]} goblin_legs")
                                else:
                                    print(f"Earned {preinv[q]} goblin_leg")

                                t.sleep(0.33)
                            continue

                        case 2:
                            if preinv[q]:
                                if preinv[q] > 1:
                                    print(f"Earned {preinv[q]} goblin_swords")
                                else:
                                    print(f"Earned {preinv[q]} goblin_sword")

                                t.sleep(0.33)
                            continue

                        case 3:
                            if preinv[q]:
                                if preinv[q] > 1:
                                    print(f"Earned {preinv[q]} goblin_staffs",
                                        "+=======================+", sep='\n')
                                else:
                                    print(f"Earned {preinv[q]} goblin_staff",
                                        "+=======================+", sep='\n')
                            else:
                                print("+=======================+")

                                t.sleep(0.33)
            
        case _:
            raise Exception("3rd: OH NAHHHHHH JIT TRIPPING")
        
def printingInv(inv: dict):

    def __contPrtint(inv: dict):
        
    """
    print inventory
    (the inventory)
    """
    __quit = False
    print("+======|inv|======+")
    for i, (key, value) in enumerate(inv.items()):
        print(f'+ {value} x {key}')

        if i > 8:
            print("+=================+")

            while True:
                check = input("Continue? ").lower()
                if check in ["yes", "ye", "y", "continue", "cont"]:
                    print("+=================+")
                    break
                elif check in ["no", "n"]:
                    __quit = True
                    break
                else:
                    continue

            if __quit:
                break

            __key = list(inv)
            __value = list(inv.values())
        
            for x in range(len(inv)):

                try:
                   print(f'+ {__value[x+9]} x {__key[x+9]}')

                except IndexError:
                   break

                break

            break

    print("+=================+")

if __name__ == '__main__':
    inv = {
        "lol": 2,
        "k": 1,
        "ld": 231,
        "d": 312,
        "dw": 321,
        "dwad": 32131,
        "elwakd": 231312,
        "ejwadj": 23131,
        "euj21ij": 231,
        "eedwjjd": 213,
        "LLO": 213
    }
    printingInv(inv)

"""
dropes = ["apples", "banana", 1, 1, 1, 1, 1, 1, 1, 1, 1,1]
ewj = []
for _ in dropes:
    ewj.append([])

print(ewj)
"""