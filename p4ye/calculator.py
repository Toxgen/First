import time as t

print("just a calculator")

num1 = 0 # Declaring Variables
num2 = 0
ans = 0
continueOperation = None

def add(x, y): # Addition
    return x + y
def sub(x, y): # Subtraction
    return x - y
def multi(x, y): # Multiplication
    return x * y
def divid(x, y): # Division
    if x + y == 0:
        return "Infinity"
    else:
        return x / y
    
def checkingEquation():
    while True: # Main Loop
        amount1 = input("Number 1: ") 
        try:
            num1 = int(amount1)
        except ValueError:
            print("Not int", '\n')
            continue

        amount2 = input("Number 2: ") 
        try: 
            num2 = int(amount2)
            print('\n')
        except ValueError:
            print("Not int", '\n')
            continue

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
                else:
                    raise Exception
            except Exception:
                print("Not an Operation", '\n')
                continue

        print(f"Does this Equation Look Right: {num1} {userInput} {num2}?", "y for yes, n for no", sep='\n') 
    
def calculator():
    global continueOperation

    while True: # Maybe add something to check if they put ans in the amount1 <===
        amount1 = input("Number 1: ")
        try:
            num1 = int(amount1)
        except ValueError:
            print("Not int", '\n')
            continue

        amount2 = input("Number 2: ") 
        try: 
            num2 = int(amount2)
            print('\n')
        except ValueError:
            print("Not int", '\n')
            continue

        print("\n")
        print("Please type in either '-', '+', '*', or '/'")

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
                else:
                    raise Exception
            except Exception:
                print("Not an Operation", '\n')
                continue

        print(f"Does this Equation Look Right: {num1} {userInput} {num2}?", "y for yes, n for no", sep='\n') 

        if userInput == "+": 
            ans = add(num1, num2)
        elif userInput == "-":
            ans = sub(num1, num2)
        elif userInput == "*":
            ans = multi(num1, num2)
        elif userInput == "/": 
            ans = divid(num1, num2)
            if ans == "Infinity":
                raise Exception("Infinity") # maybe add smth to actually say infinity
        print(f"The ans is {ans}")
        t.sleep(1.32)
        break

calculator()

while True:
    print("Continue Operation?: y for yes & n for no")
    try:
        continueOperation = input('> ').lower().strip()

        if continueOperation == "y":
            calculator()
        elif continueOperation == "n":
            break
        else:
            raise Exception()
    except Exception:
        print("Please type in y or n", sep='\n')
        continue
print("Calculation Ended")
