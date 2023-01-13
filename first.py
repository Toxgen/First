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
    time.sleep(1)
    print('You have woken on your bed in a peaceful cabin')
    time.sleep(1.5)
    print('Today your gonna get your adventure badge!')
    time.sleep(2)
    print('But then, you find yourself between a monster')
    time.sleep(2)
    print('You know that you haven\'t gotten your badge yet, but you still attack it')
    time.sleep(2.785)
    print('The monster has ' + str(monsterHp) + ' hp')
    time.sleep(3)
    print('While you have ' + str(selfHp) + ' hp')
beginning()


def first_attack():

    time.sleep(3.1)
    print('You will always attack first no matter what')
    time.sleep(2)
    print('In order to atack, you need to type "attack"')


first_attack()

# Maybe add description or more things to make the text sound more 'interesting'


# crtl^c to stop input line :/

def attackSystem():
    fist_Dmg = random.randint(1, 3)
    monster_Dmg = random.randint(2, 4)
    global monsterHp, selfHp
    monsterHp = monsterHp - fist_Dmg
    selfHp = selfHp - monster_Dmg
    time.sleep(0.2)
    print('The monster now has, ' + str(monsterHp) + ' hp')
    time.sleep(1)
    print('Ouch, now you have, ' + str(selfHp) + ' hp')
    return monsterHp, selfHp


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
            print(monsterHp)
            time.sleep(0.25)
            line = input('> ')
            if line.lower().strip() == 'attack' :
                    attackSystem()
            else:
                print('That is not "attack", try again')
            
            if monsterHp < 0:
                break
combat()

# somehow make if the value of monsterHp goes neg, then ignore everying printed.

bruh()

weapons.append("wooden cub")
Exp =+ 8

