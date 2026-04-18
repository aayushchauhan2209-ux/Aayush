#Gussing a number game 
from random import randint
print("Welcome to the Guess the Number Game!")
while True:
    a = int(input("Enter the range for the number (1 to n): "))
    n = int((randint(1, a)))
    num = 0
    while True:
       if(num != n):
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
                break
        
    A = str(input("Do you want to play again? (yes/no): "))
    if A.lower() != "yes":
        print("Thank you for playing! Goodbye!")
        break
