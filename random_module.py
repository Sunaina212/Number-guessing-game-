import random 
print("Welcome to the. number guessing game!")

while True :
    level = input("Please slect the level of the game (Easy,Medium,Hard)")
    if level == "Easy":
        start,end,max_attempt = 1,50,10
    elif level == "Medium":
        start,end,max_attempt=1,100,7
    elif level == "Hard":
        start,end,max_attempt=1,500,5
    else :
        print("Invalid choice, please select from given levels (Easy,Medium,Hard)")
        continue

    secret_num  = random.randint(start,end) 
    attempts = 0 
    print(f"You have chosen a number between {start} and {end}")  
    print(f"You have {max_attempt} attempts for the game!") 

    while attempts < max_attempt :
        guess = int(input("Enter your guess:"))
        attempts +=1

        if guess < secret_num :
            print("Your guess Too low, Try again!")
        elif guess >secret_num:
            print("Your guess is Too high ,Try again!")
        else :
            print("You nailed it ! correct guess")       
            print("Attempts :",attempts) 

            score = 100 - (attempts-1) *10 
            if score <  0 :
                score = 0 
            print("Your score is :",score )   
            break 
    else :
        print("You Lost!")
        print(f"Correct number is {secret_num}")
    play = input("You want to play more (Yes,No)").lower()
    if play != "Yes":
        print("Thanks for playing..")
        break    

