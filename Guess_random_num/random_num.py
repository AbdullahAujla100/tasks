import random
num=random.randint(1,25)
hard_lives=5
easy_lives=8
print("========WELCOME TO RANDOM NUMBER GAME==========")
difficulty=input("Enter your difficulty easy or hard : ").lower()
game_over=False
while not game_over:
    if difficulty=="easy":    
        guessed_number=int(input("Enter your guessed number between(1-25) : "))
        if guessed_number > num:
            print(" Guess a lower number ")
            easy_lives-=1
            print(f"You have {easy_lives} chances left ")
            if easy_lives == 0:
                print("You loose")
                game_over=True  


        elif guessed_number < num:
            print(" Guess a higher number ")  
            easy_lives-=1
            print(f"You have {easy_lives} left ")
            if easy_lives == 0:
                print("You loose")
                game_over=True  

        elif guessed_number == num:
            print("you guessed the right number")
            print("====YOU WIN=====")
            game_over=True

    elif difficulty=="hard":
        guessed_number=int(input("Enter your guessed number between(1-25) : "))
        if guessed_number > num:
            print("Guess a lower number  ")
            hard_lives-=1
            print(f"You have {hard_lives} chances left ")
            if hard_lives == 0:
                print("You loose")
                print(f"The actual number was {num}")
                game_over=True  


        elif guessed_number < num:
            print("Guess a higher number ")  
            hard_lives-=1
            print(f"You have {hard_lives} chances left ")
            if hard_lives == 0:
                print("You loose")
                print(f"The actual number was {num}")
                game_over=True  

        elif guessed_number == num:
            print("you guessed the right number")
            print("====YOU WIN=====")
            game_over=True

    else:
        print("You have entered invalid choice  ")
        break