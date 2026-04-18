# Number gussing game with different levels of difficulty and score system
def Deficulty():
    print("Welcome to the Guess the Number Game!")
    print("Enter 1 for Easy(RAnge 1 - 50 and atumps = 10)")
    print("Enter 2 for Medium(RAnge 1 - 100 and atumps = 7)")
    print("Enter 3 for Hard(RAnge 1 - 200 and atumps = 5)")
    D = int(input("Enter the difficulty level: "))
    if D == 1:
        a = 50
        matumpt = 10
        return a,matumpt,D
    elif D == 2:
        a = 100
        matumpt = 7 
        return a,matumpt,D
    elif D == 3:
        a = 200
        matumpt = 5
        return a,matumpt,D

    else:
        print("Invalid input! Please enter a valid difficulty level.")
        return 0
    
    
    
    
def Score(attemp):
    if attemp == 1:
        return 100
    elif attemp == 2:
        return 90  
    elif attemp == 3:
        return 80
    elif attemp == 4:
        return 70
    elif attemp == 5:
        return 60
    elif attemp == 6:
        return 50
    elif attemp == 7:
        return 40
    elif attemp == 8:
        return 30
    elif attemp == 9:
        return 20
    elif attemp == 10:
        return 10
    else:
       return 0


def Max_Score(score):
    with open("C:\\Users\\Ayush\\OneDrive\\Desktop\\Python\\Aayush\\score.txt", "r+") as file:
        try:    
            max_score = int(file.read())
        except:
            max_score = 0
        if score > max_score:
            file.seek(0)
            file.write(str(score))
            return score
        else:
            return max_score 
        
from random import randint
while True:
    a,matumpt,D = Deficulty()
    n = int((randint(1, a)))
    atumpt = 1
    num = 0
    print(n)
    while(atumpt <= matumpt):
        if(num != n):
            print("It is your ", atumpt, "attempt" )
            num = int(input("Enter your guess: "))
            if(num >= n+5 ):
                print("Too high")
            elif(num <= n-5):
                print("Too low")
            elif(num > n):
                print("Close enough, but still high")
            elif(num < n):
                print("Close enough, but still low")
            else:
                print("Congratulations! You guessed the number.")
                print("The number was:", n)
                score = Score(atumpt)
                print("Your score is:", score)
                max_score = Max_Score(score)
                print("The maximum score is:", max_score)
                break
            atumpt += 1
    else:
       print("Your Attempts are over! The number was:", n)

        
    A = str(input("Do you want to play again? (yes/no): "))
    if A.lower() != "yes":
        print("Thank you for playing! Goodbye!")
