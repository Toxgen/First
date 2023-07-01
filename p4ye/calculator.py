import time as t

num1 = 0  # Declaring Variables
num2 = 0
ans = 0
preAns = None
continueOperation = False
check = ()
xyz = 2

def add(x, y):  
    return x + y
def sub(x, y):  
    return x - y
def multi(x, y):  
    return x * y
def divid(x, y):  
    if x + y == 0:
        return "Undefined"
    else:
        return x / y
def power(x, y):
    return pow(x, y)

def checkingEquation():
<<<<<<< HEAD
    global continueOperation, preAns, xyz, num1, num2, userInput
    while True: 
        if continueOperation == True:
            print("You can write 'ans' to input the previous answer")
            continueOperation = None
        amount1 = input("Number 1: ").lower().strip()
        if amount1 == "ans" and continueOperation == None:
            amount1 = preAns
=======
    while True: # Main Loop
        amount1 = input("Number 1: ") 
>>>>>>> 50fcdc8a672a9529af35107b936db16fae189d86
        try:
            num1 = int(amount1)
            print('\n')
        except ValueError:
            print("Not int", '\n')
            continue

<<<<<<< HEAD
        amount2 = input("Number 2: ").lower().strip()
        if amount2 == "ans" and continueOperation == None:
            amount2 = preAns
        try:
=======
        amount2 = input("Number 2: ") 
        try: 
>>>>>>> 50fcdc8a672a9529af35107b936db16fae189d86
            num2 = int(amount2)
            print('\n')
        except ValueError:
            print("Not int", '\n')
            continue

<<<<<<< HEAD
        print("Please type in either '-', '+', '*', '/', or '^'")

        while True:
            userInput = input("Operation: ")
            try:
=======
        while True: 
            userInput = input("Operation: ") 
            try: 
>>>>>>> 50fcdc8a672a9529af35107b936db16fae189d86
                if userInput == "+":
                    break
                elif userInput == "-":
                    break
                elif userInput == "*":
                    break
                elif userInput == "/":
                    break
                elif userInput == "^":
                    break
                else:
                    raise Exception
            except Exception:
                print("Not an Operation", '\n')
                continue

        print(f"Does this Equation Look Right: {num1} {userInput} {num2}?", "y for yes, n for no", sep='\n')
        while True:
            try:
                right = input('> ').lower().strip()

                if right == 'y':
                    break
                elif right == 'n':
                    checkingEquation()
                else:
                    raise Exception
            except Exception:
                print("Please type in either 'y' or 'n'", sep='\n')
                continue
            break
        break

def calculator():
<<<<<<< HEAD
    global continueOperation, preAns, xyz
    while True: 
        if continueOperation == True and xyz // 2 != float:
            print("You can write 'ans' to input the previous answer") 
            continueOperation = None
            xyz += 1
        amount1 = input("Number 1: ").lower().strip()
        if amount1 == "ans" and continueOperation == None:
            amount1 = preAns
=======
    global continueOperation

    while True: # Maybe add something to check if they put ans in the amount1 <===
        amount1 = input("Number 1: ")
>>>>>>> 50fcdc8a672a9529af35107b936db16fae189d86
        try:
            num1 = int(amount1)
            print('\n')
        except ValueError:
            print("Not int", '\n')
            continue

<<<<<<< HEAD
        amount2 = input("Number 2: ").lower().strip()
        if amount2 == "ans" and continueOperation == None:
            amount2 = preAns
            continueOperation = True
        try:
=======
        amount2 = input("Number 2: ") 
        try: 
>>>>>>> 50fcdc8a672a9529af35107b936db16fae189d86
            num2 = int(amount2)
            print('\n')
        except ValueError:
            print("Not int", '\n')
            continue

        print("Please type in either '-', '+', '*', '/', or '^'")

        while True:
            userInput = input("Operation: ")
            try:
                if userInput == "+":
                    break
                elif userInput == "-":
                    break
                elif userInput == "*":
                    break
                elif userInput == "/":
                    break
                elif userInput == "^":
                    break
                else:
                    raise Exception
            except Exception:
                print("Not an Operation", '\n')
                continue

        print(f"Does this Equation Look Right: {num1} {userInput} {num2}?", "y for yes, n for no", sep='\n')
        while True:
            try:
                right = input('> ').lower().strip()

                if right == 'y':
                    break
                elif right == 'n':
                    print('\n')
                    checkingEquation()
                    break
                else:
                    raise Exception
            except Exception:
                print("Please type in either 'y' or 'n'", sep='\n')

        if userInput == "+":
            ans = add(num1, num2)
        elif userInput == "-":
            ans = sub(num1, num2)
        elif userInput == "*":
            ans = multi(num1, num2)
        elif userInput == "^":
            ans = pow(num1, num2)
        elif userInput == "/":
            ans = divid(num1, num2)
<<<<<<< HEAD
            if ans == "Undefined":
                quit("Undefined")
            
=======
            if ans == "Infinity":
                raise Exception("Infinity") # maybe add smth to actually say infinity
>>>>>>> 50fcdc8a672a9529af35107b936db16fae189d86
        print(f"The ans is {ans}")
        preAns = ans
        t.sleep(1.32)
        break


calculator()

while True:
    print("Continue Operation?: y for yes & n for no")
    try:
        continue1 = input('> ').lower().strip()

        if continue1 == "y":
            calculator()
            if continueOperation == False:
                continueOperation = True
        elif continue1 == "n":
            break
        else:
            raise Exception()
    except Exception:
        print("Please type in y or n", sep='\n')
        continue
<<<<<<< HEAD
    
print("Calculation Ended")
=======
print("Calculation Ended")
>>>>>>> 50fcdc8a672a9529af35107b936db16fae189d86
