print("try")

print(x)
'''
import time
import random

global weapons
inv = dict()
items = dict()
weapons = 1
weaponsdict = {

    "weapon(s)": weapons,
}
exp = 0

inv = 

global monsterHp
monsterHp = 10
global selfHp
selfHp = 50

weapons.update({"wooden club": 1})
Exp = + 8

def naming():
    global name
    print("Make a Username")
    time.sleep(2.2)
    print('The Username can only be 1-8 characters long')
    name = input('> ')
    dummy = len(name)
    while dummy >= 9:
        print('\n')
        print('3-8 characters')
        time.sleep(1.0)
        print('Try again')
        name = input('> ')
        dummy = len(name)
        if dummy <= 9:
            break
    if len(name) != 0:
        print('\n')
        print('You typed in "' + name + '". Are you Sure? Type in "yes" or "no"')
        Sureness = input('> ')
        if Sureness.lower().strip() == 'yes':
            print('Your name now will be "' + name + '" ')

        elif Sureness.lower().strip() != 'no':
           while Sureness.lower().strip() != 'yes':
            print('Type in Yes or No')
            Sureness = input('> ')
            if Sureness.lower().strip() == 'yes':
                print('Your name is "' + name + '"')
                break

            elif Sureness.lower().strip() == 'no':
                time.sleep(0.22)
                print('\n')
                while Sureness.lower().strip() == 'no':
                    print("What's your new name")
                    name = input('> ')
                    dummy = len(name)
                    while dummy >= 9:
                        print('\n')
                        print('3-8 characters')
                        time.sleep(1.0)
                        print('Try again')
                        name = input('> ')
                        dummy = len(name)
                        if dummy <= 9:
                            break
                    if len(name) != 0:
                        print('You typed in "' + name +
                              '". Are you Sure? Type in "yes" or "no"')
                        Sureness = input('> ')
                        if Sureness.lower().strip() == 'yes':
                            print('Your name now will be "' + name + '" ')
                            break
                        else:
                            print('')
            else:
                print('\n')

        else:
            time.sleep(0.22)
            while Sureness.lower().strip() == 'no':
                print('\n')
                print("What's your new name ")
                name = input('> ')
                dummy = len(name)
                while dummy >= 9:
                    print('\n')
                    print('3-8 characters')
                    time.sleep(1.0)
                    print('Try again')
                    name = input('> ')
                    dummy = len(name)
                    if dummy <= 9:
                        break
                if len(name) != 0:
                    print('You typed in "' + name +
                          '". Are you Sure? Type in "yes" or "no"')
                    Sureness = input('> ')
                    if Sureness.lower().strip() == 'yes':
                        print('Your name is "' + name + '" ')
                        break
                    else:
                        print('')
                else:
                    print('\n')
                    naming()
    else:
        print('\n')
        naming()


naming()

print('What do you want to do, ' + name)

print('\n')
time.sleep(1.2223)

print('Type in "help" to find your commands')


def bk():
    global commands
    help1 = input('> ')
    while help1.lower().strip() == "help":
        if help1.lower().strip() == "help":
            commands = ['stats', 'inv', 'adv']
            print(*commands, sep='\n')
            time.sleep(0.34)
            break
    else:
        print('type in "help"')
        print('\n')
        bk()

bk()

time.sleep(1)
print('Try to type one of the printed words out!!')
time.sleep(0.2)

def picking101():
    help2 = input('> ')
    if help2.lower().strip() == commands[0]:
        print('Here are your stats')
        stats = dict()
        stats = {
            "name": name,
            "exp": exp,
            "health": selfHp
        }
        print(sep=' ')
        for key, value in stats.items():
            if key == 'name':
                    print('------------------------')
                    print(key + ':')
                    print('"' + value + '" ')
                    print('------------------------')
            elif key == 'exp':
                    print(key + ':')
                    print(str(value) + '/10')
                    print('------------------------')
            elif key == 'health':
                    print(key + ':')
                    print(str(value) + '/50')
                    print('------------------------')
                    break
    elif help2.lower().strip() == commands[1]:
        print('Here is your inventory')
        for key, value in inv.items():
        
    elif help2.lower().strip() == commands[2]:
        print('WORK IN PROGRESS')
    else:
        print('\n')
        print('Type in one of the words above ("stats", "inv", "adv")')
        picking101()


picking101()
'''
