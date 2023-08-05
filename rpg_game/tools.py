import random as r

        
def drops(level: int, luck: int) -> list:
    """
    level: current mob level
    luck: current luck stat | self.luck
    """
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

def counting_drop(test: list, mob: str):
    """
    Input the list
    """

    match mob:

        case "goblin":
            g_hide = test.count("goblin_hide")

            g_leg = test.count("goblin_leg")
            
            g_sword = test.count("goblin_sword")

            g_staff = test.count("goblin_staff")

            return [g_hide, g_leg, g_sword, g_staff]
    
        case _:
            raise Exception("UH OH")



if __name__ == '__main__':
    a = drops(0, 10)
    print(counting_drop(a, "goblin"))