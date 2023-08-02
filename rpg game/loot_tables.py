import random as r

# luck system is absolutely flawwed
class goblin:
    def __init__(self, level, luck):
        self.level = level
        self.luck = luck

    def __repr__(self):
        return f"{self.level} and {self.luck}"
        
    def mob_drops(self, level: int, luck: int) -> list:
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
            print("running")
            if not i: # guaranteed 1
                returning.append("goblin_hide")

            x = r.randint(-1, 101)

            if 60 <= x >= 80: # about 20% chance
                returning.append("goblin_hide")

            elif 30 <= x >= 40: # about 10% chance
                returning.append("goblin_leg")

            elif 15 <= x >= 20: # about 5% chance
                returning.append("goblin_sword")

            elif 10 <= x >= 12: # about 2% chance
                returning.append("goblin_staff")
            else: # about 10% chance: nothing
                continue
        
        return returning
                
if __name__ == "__main__":
    test = goblin(10, 10)
    print(test)
    g = []
    g = test.mob_drops(10, 10)
    print(g)