import time as t

"""
notes

for both nums and ops 
might have to loop through those
actually i have 0 idea



uaayaya
"""


def opsTranslate(list) -> list:
    for a in range(len(list)):  # maybe we dont need to make a new list, but like changing whats in that list. make that change later, this currently works
        if list[a] == 1:
            lst_ops.append("+")
        if list[a] == 2:
            lst_ops.append("-")
        if list[a] == 3:
            lst_ops.append("*")
        if list[a] == 4:
            lst_ops.append("/")
    return lst_ops

def calculator() -> int:
    global lst_ops
    lst_ops = []
    list_num = []
    ops = []

    print("How Many Numerical Values Would You Like In Your Calculation? *fyi, up to 10") 

    while True: 
        amount = input("Amount: ")
        try:
            amt = int(amount)
        except ValueError:
            print("Not int", '\n')
            continue
        if amt <= 1:
            print("Please Type in a Number Between 2 - 10", '\n')
            continue
        if amt > 10:
            print("Please Type Something Lower Than 11", '\n')
        else:
            print('\n')
            break

    for i in range(amt): 
        while True:
            userInput = input("Enter A Number: ") # when inputs number in here, it does the equation automatically using a different fufnctions
            try:
                num = int(userInput)
            except ValueError:
                print("Not int", '\n')
                continue
            else:
                break
        list_num.append(num)

    print("""
    In order to enter a operation, you have to enter a code for that specific operation

    1 -> +
    2 -> -
    3 -> *
    4 -> /
    """, "\n")

    t.sleep(4.2)

    for x in range(amt-1):
        while True:
            userInput = input("Enter a Operation Code: ") 
            try:
                opss = userInput
                if int(opss) > 5:
                    raise Exception()
                if int(opss) < 0:
                    raise Exception()
            except Exception:
                print("Not Valid", '\n')
                continue
            else:
                break
        ops.append(int(opss))

    print("translating over...")
    t.sleep(1.444)
    opsTranslate(ops)

    try:
        int2 = "{0} & {1}".format(
            list_num[0], list_num[1])
        int3 = "{0} & {1} & {2}".format(
            list_num[0], list_num[1], list_num[2])
        int4 = "{0} & {1} & {2} & {3}".format(
            list_num[0], list_num[1], list_num[2], list_num[3])
        int5 = "{0} & {1} & {2} & {3} & {4}".format(
            list_num[0], list_num[1], list_num[2], list_num[3], list_num[4])
        int6 = "{0} & {1} & {2} & {3} & {4} & {5}".format(
            list_num[0], list_num[1], list_num[2], list_num[3], list_num[4], list_num[5])
        int7 = "{0} & {1} & {2} & {3} & {4} & {5} & {6}".format(
            list_num[0], list_num[1], list_num[2], list_num[3], list_num[4], list_num[5], list_num[6])
        int8 = "{0} & {1} & {2} & {3} & {4} & {5} & {6} & {7}".format(
            list_num[0], list_num[1], list_num[2], list_num[3], list_num[4], list_num[5], list_num[6], list_num[7])
        int9 = "{0} & {1} & {2} & {3} & {4} & {5} & {6} & {7} & {8}".format(
            list_num[0], list_num[1], list_num[2], list_num[3], list_num[4], list_num[5], list_num[6], list_num[7], list_num[8])
        int10 = "{0} & {1} & {2} & {3} & {4} & {5} & {6} & {7} & {8} & {9}".format(
            list_num[0], list_num[1], list_num[2], list_num[3], list_num[4], list_num[5], list_num[6], list_num[7], list_num[8], list_num[9])  # maybe add the signs for the spaces inbetween the and signs
    except Exception:
        print("Declaring Variables...", '\n')
        t.sleep(3)
    
    if amt == 2:
        print(int2, '\n')
    elif amt == 3:
        print(int3, '\n')
    elif amt == 4:
        print(int4, '\n')
    elif amt == 5:
        print(int5, '\n')
    elif amt == 6:
        print(int6, '\n')
    elif amt == 7:
        print(int7, '\n')
    elif amt == 8:
        print(int8, '\n')
    elif amt == 9:
        print(int9, '\n')
    elif amt == 10:
        print(int10, '\n')
    else:
        raise Exception("Something Went Wrong, Retry")
    
calculator()