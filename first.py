import random
import time

weapons = []
items = []
exp = []

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

def new_func():
    return 0

fist_Dmg = random.randint(1, 10)
monster_Dmg = random.randint(1, 5)

#crtl^c to stop input line :/

def attackSystem():
  global monsterHp, selfHp
  monsterHp = monsterHp - fist_Dmg
  selfHp = selfHp - monster_Dmg
  time.sleep(0.2)
  print('The monster now has, ' + str(monsterHp) + ' hp')
  time.sleep(1)
  print('Ouch, now you have, ' + str(selfHp) + ' hp')
  return monsterHp, selfHp
  

def combat():
  counter = new_func()
  if counter == 0:
        while True:
            time.sleep(0.275212)
            line = input('> ')
            if line.lower().strip() == 'attack' :
                attackSystem()
            else:
                print('That is not "attack", try again')

while monsterHp >= 0:
  combat()

#if monsterHp <=0: