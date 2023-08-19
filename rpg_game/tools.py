
def drops(level: int, mob: str) -> list:
    """
    very complicated drops
    (the mob level, self.luck, self.mob)
    """

    import random as r
    from random import randint

    luck = r.randint(1, 6)

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
                
            for _i in range(luck):

                if not _i: # guaranteed 1
                    returning.append("goblin_hide")

                _x = r.randint(0, 100)

                if len(returning) >= 3:
                    _x = r.randint(0, 150)

                if _x <= 5:  
                    returning.append("goblin_staff")
                    continue

                if _x <= 8:  
                    returning.append("goblin_sword")
                    continue

                if _x <= 12:  
                    returning.append("goblin_leg")
                    continue

                if _x <= 25: 
                    returning.append("goblin_hide")
                    continue

            return returning

        case _:
            raise Exception("Error: This shouldn't happen, p.s. check mob arg")

            
            

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
            raise Exception("Error: This shouldn't happen, p.s. check mob arg")
        
def printingDrops(preinv: list, mob: str):
    """
    print em drops
    (the counted drop list, self.mob)
    """

    import time as t
    from time import sleep

    match mob:

        case "goblin":

            for _q in range(len(preinv)):

                match _q:

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
            raise Exception("Error: This shouldn't happen, p.s. check mob arg")
        
def printingInv(inv: dict) -> None:
    """
    print inventory
    (the inventory)
    """

    import time as t
    from time import sleep

    __quit = False

    print("+======|inv|======+")
    for _i, (key, value) in enumerate(inv.items()):
        print(f'+ {value} x {key}')

        t.sleep(0.05)

        if _i % 8 == 0 and _i > 1:
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

            while _i % 8 != 0:
                print(f"+ {value[i]} x {key[i]}")

    print("+=================+")

if __name__ == '__main__':
    pass
"""
dropes = ["apples", "banana", 1, 1, 1, 1, 1, 1, 1, 1, 1,1]
ewj = []
for _ in dropes:
    ewj.append([])

print(ewj)
"""
