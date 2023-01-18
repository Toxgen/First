import random
import time

global weapons
weapons = []
items = []
exp = 0

global monsterHp
monsterHp = 10
global selfHp
selfHp = 50

def beginning():
    print('The day is the September 1st, a peaceful and normal day')
    time.sleep(1.5)
    print('You wake up and feel refresed from yesterday')
    time.sleep(1.7666)
    print('You get ready for your morning stroll around the woods')
    time.sleep(2)
    print('However, when you went outside, you saw a disgusting, huge creature')
    time.sleep(2.785)
    print('The mouth was full of teeth, which were stained yellow, and standing up to 8 feet')
    time.sleep(2)
    print("You didn't carry anything, unfortunately, but you still tried to attack it")
    time.sleep(1.12)
    print('The monster has ' + str(monsterHp) + ' hp')
    time.sleep(2.75)
    print('While you have ' + str(selfHp) + ' hp')
    time.sleep(3.1)
    print('You will always attack first no matter what')
    time.sleep(2)
    print("\n")
    print('In order to attack, you need to type "attack"')

beginning()

# crtl^c to stop input line :/

def attackSystem():
    global monsterHp, selfHp
    fist_Dmg = random.randint(1, 3)
    monster_Dmg = random.randint(2, 4)
    monsterHp = monsterHp - fist_Dmg
    selfHp = selfHp - monster_Dmg
    for i in range(1):
        if not monsterHp == [0, -1, -2] or not monsterHp > 0:
            time.sleep(0.2)
            print('\n')
            print('The monster now has, ' + str(monsterHp) + ' hp')
            time.sleep(1)
            print('Ouch, now you have, ' + str(selfHp) + ' hp')
            return monsterHp, selfHp
        else:
            break

#cant fix if neg monsterHp happens, idk if haeve free time do this

def bruh():
    print('Congratulations, you have defeated the monster')
    time.sleep(0.6667)
    print('Gotten "wooden cub"')
    time.sleep(0.333)
    print('P.S. the "wooden cub does 3-5 DMG')
    time.sleep(0.333)
    print('Gained 8 XP')

def combat():
    if monsterHp > 0:
         while True:
            time.sleep(0.25)
            line = input('> ')
            if line.lower().strip() == 'attack' :
                    attackSystem()
            else:
                print('That is not "attack", try again')
            
            if monsterHp < 0:
                break
combat()

# somehow make if the value of monsterHp goes neg, then ignore everying printed 

bruh()

# https://stackoverflow.com/questions/23271575/printing-bold-colored-etc-text-in-ipython-qtconsole (scrol down)

weapons.append("wooden cub")
Exp =+ 8

def Continuation():
    print('\x1b[3;30;40m' + 'test' + '\x1b[0m') # <-- the print statement is just a test

Continuation()
