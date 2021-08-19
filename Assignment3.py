def Quidditch(goal1,goal2,snitch):
    score1 = goal1*10;
    score2 = goal2*10;
    if(snitch==1):
        score1+=30
    elif(snitch==2):
        score2+=30
    print("Team 1 scored : "+str(score1)+"\n")
    print("Team 2 scored : "+str(score2))
    if score1>score2:
        print("\nTeam 1 won!")
    elif score2>score1:
        print("\nTeam 2 won!")
    else:
        print("\nIt's a tie!")

def Quarterback(comp,pass_yard,attempt,touchdown,inter):
    score = ((5*((comp/attempt)-0.3)) + (0.25*((pass_yard/attempt)-3)) + 20*(touchdown/attempt) + 2.375 - (25*(inter/attempt)))*100/6
    if score > 158.3:
        print("The player is a perfect passer\n")
    print("The player's rating is "+str(score))

def Gymnast(score,execute):
    mx = max(execute)
    mn = min(execute)
    rate = score + (sum(execute)-mx-mn)/3
    print("The gymnast scored "+str(rate)+" points")


n = input("Enter 1 for Quidditch, 2 for Quarterback, 3 for Gymnastics : ")
if n.isdigit() and int(n) <= 3 and int(n) >= 1:
    n = int(n)
else:
    print("Invalid input")
    sys.exit()
if n == 1:
    goal1 = input("Enter goals scored by Team 1 : ")
    if goal1.isdigit() and int(goal1) >= 0:
        goal1 = int(goal1)
    else:
        print("Invalid input")
        sys.exit()
    goal2 = input("Enter goals scored by Team 2 : ")
    if goal2.isdigit() and int(goal2) >= 0:
        goal2 = int(goal2)
    else:
        print("Invalid input")
        sys.exit()
    snitch = input("Enter 1 if Team 1 caught the snitch, 2 if Team 2, 0 if neither : ")
    if snitch.isdigit() and int(snitch) <= 2 and int(snitch) >= 0:
        snitch = int(snitch)
    else:
        print("Invalid input")
        sys.exit()
    Quidditch(goal1, goal2, snitch)

elif n == 2:
    completion = input("Enter completions : ")
    if completion.isdigit() and int(completion) >= 0:
        completion = int(completion)
    else:
        print("Invalid input")
        sys.exit()
    pass_yard = input("Enter passing yards : ")
    if pass_yard.isdigit() and int(pass_yard) >= 0:
        pass_yard = int(pass_yard)
    else:
        print("Invalid input")
        sys.exit()
    attempt = input("Enter attempts : ")
    if attempt.isdigit() and int(attempt) >= 0:
        attempt = int(attempt)
    else:
        print("Invalid input")
        sys.exit()
    if (attempt == 0):
        print("Divide by zero exception")
        sys.exit()
    touchdown = input("Enter touchdown passes : ")
    if touchdown.isdigit() and int(touchdown) >= 0:
        touchdown = int(touchdown)
    else:
        print("Invalid input")
        sys.exit()
    inter = input("Enter interceptions : ")
    if inter.isdigit() and int(inter) >= 0:
        inter = int(inter)
    else:
        print("Invalid input")
        sys.exit()
    Quarterback(completion, pass_yard, attempt, touchdown, inter)

elif (n == 3):
    score = input("Enter difficulty score : ")
    if score.isdigit() and int(score) >= 0:
        score = int(score)
    else:
        print("Invalid input")
        sys.exit()
    execute = []
    for i in range(5):
        temp = input("Enter execution score " + str(i + 1) + " : ")
        if temp.isdigit() and int(temp) >= 0:
            execute.append(int(temp))
        else:
            print("Invalid input")
            sys.exit()
    Gymnast(score, execute)
else:
    print("Invalid input")


