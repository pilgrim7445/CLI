
consoleWillRun = True
loggedIn = False

cmdListLoggedIn = ["signout"]
cmdListLoggedOut = ["singin"]
cmdListCommon = ["list", "calc", "quit", "help", "3x+1"]
cmdList = list(set(cmdListLoggedIn+cmdListLoggedOut+cmdListCommon))

def getCredentials():
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    return [username, password]

def singin():
    credentials = getCredentials()
    if credentials[0] == "gamer" and credentials[1] == "gamer":
        login()
    elif credentials[0] == "quit" or credentials[1] == "quit":
        console()
    else:
        singin()

def help():
    print("calc: Calculate a maths expression")
    print("singin: Sign in")
    print("signout: Sign out")
    print("quit: Works in every app, quits to console or, in console, quits console.")

def login():
    print('Logged in')
    loggedIn = True

def logout():
    print('Logged out')
    loggedIn = False

def calc():
    while True:
        expression = input('Input a maths expression: ')
        if expression == "quit":
            break
            consoleWillRun = True
        else:
            return eval(expression)

def collatz():
    print("3x+1 solver")

    mode = int(input("Mode (1 or 2): "))
    if mode == 1:
        num = int(input("Number: "))
        moddedNum = num
        iter = 0

        while True:
            if (moddedNum % 2) == 0:
                moddedNum = moddedNum/2
                print(int(moddedNum))
                iter += 1
            else:
                moddedNum = moddedNum*3+1
                print(int(moddedNum))
                iter += 1
            if moddedNum == 1:
                break
        print(f"The number {num} took {iter} iterations to get to 1.")
        consoleWillRun = True
    if mode == 2:
        length = int(input("How many numbers: "))

        for num in range(1, length + 1):
            modedNum = num
            iterations = 0

            while modedNum != 1:
                if modedNum % 2 == 0:
                    modedNum //= 2
                else:
                    modedNum = modedNum * 3 + 1
                iterations += 1

            print(f"The number {num} took {iterations} iterations to get to 1.")
        consoleWillRun = True

def console():
    command = input("Enter a command: ")
    if command == "":
        console()
    elif command in cmdList:
        if command == "calc":
            consoleWillRun = False
            print(calc())
        elif command == "singin":
            consoleWillRun = False
            singin()
        elif command == "signout":
            consoleWillRun = False
            logout()
        elif command == "quit":
            consoleWillRun = False
            quit()
        elif command == "help":
            consoleWillRun = False
            help()
        elif command == "list":
            consoleWillRun = False
            mkList()
        elif command == "3x+1":
            consoleWillRun = False
            collatz()

def getStart():
    try:
        fstart = int(input("Starting Number: "))
        return fstart
    except ValueError:
        print("Invalid input")
        return getStart()

def getEnd():
    try:
        fend = int(input("Ending Number: "))
        return fend
    except ValueError:
        print("Invalid input")
        return getEnd()

def getNums():
    fstart = getStart()
    fend = getEnd()
    while fstart > fend:
        print("Starting number must be less than ending number")
        fstart = getStart()
        fend = getEnd()
    return [fstart, fend]

def mkList():
    ls = getNums()
    sep = input("Separator (default: ,): ") or ","
    lbracket = input("Left Character (default: ): ") or ""
    rbracket = input("Right Character (default: ): ") or ""
    lStart = ls[0]
    lEnd = ls[1]

    print(lbracket + sep.join(str(i) for i in range(lStart, lEnd + 1)) + rbracket)

    consoleWillRun = True

print("Type 'help' for help")

while consoleWillRun:
    console()
