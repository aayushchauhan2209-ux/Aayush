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
   return attemp 

def Max_Score(score):
    try:
        with open("score.txt", "r") as file:
            data = file.read().strip()
            n = int(data) if data else 0
    except FileNotFoundError:
        n = 0
    if n is None or score < n:
        with open("score.txt", "w") as file:
            file.write(str(score))
        return score
    else:
        return n

   
from random import randint
Deficulty()
while True:
    a,matumpt,D = Deficulty()
    n = int((randint(1, a)))
    atumpt = 1
    num = 0
    while(atumpt <= matumpt):
        num = int(input("Enter your guess: "))
        print("It is your ", atumpt, "attempt" )
        if(num != n):
            num = int(input("Enter your guess: "))
            print("It is your ", atumpt, "attempt" )
            atumpt += 1
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
    else:
       print("Your Attempts are over! The number was:", n)

        
    A = str(input("Do you want to play again? (yes/no): "))
    if A.lower() != "yes":
        print("Thank you for playing! Goodbye!")
