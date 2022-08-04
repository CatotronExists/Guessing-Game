from random import randint as dice
import time

### For Custom Mode ###
setup = False
max_range = 0
min_range = 0
vaild_range_min = False
vaild_range_max = False
vaild_range_guess = False
gen_range = 0 # no. of numbers that are between min and max
custom_guesses = 0
###                 ###

###                           Other                                                 ###
difficulty_select = "n/a"
hint_numbers = [2, 3, 4, 5]
difficulty = 0
play_again = 1
hints = False
change_log_open = False
game_play = True
correct = False
###                                                                                 ###

###                         yes/no Vaild                                            ###
vaild_responses =["yes", "no", "y", "n", "Yes", "YES", "No", "NO"]
yes_responses = ["yes", "y","Yes", "YES"]
no_responses = ["no", "n","No", "NO"]
###                                                                     ###

###           Vaild Characters on Difficulty Selection                  ###
vaild_difficulty = ["1", "e", "E", "easy", "Easy", "2", "m", "M", "medium", "Medium", "3", "h", "H", "hard", "Hard", "4", "i", "I", "impossible", "Impossible", "5", "c", "C", "custom", "Custom", "6", "cl", "CL", "change log", "Change Log"]
vaild_difficulty_easy = ["1", "e", "E", "easy", "Easy"]
vaild_difficulty_medium = ["2", "m", "M", "medium", "Medium"]
vaild_difficulty_hard = ["3", "h", "H", "hard", "Hard"]
vaild_difficulty_impossible = ["4", "i", "I", "impossible", "Impossible"]
vaild_difficulty_custom =["5", "c", "C", "custom", "Custom"]
vaild_difficulty_change = ["6", "cl", "CL", "change log", "Change Log"]
###                                                                     ###

while game_play == True:
    while(difficulty == 0): # Main Menu & Setup
        print("\n-----------------------------------------------")
        print("Guess the number v1.3")
        print("\nChoose a Difficulty\n")
        print("Easy (1)")
        print("Medium (2)")
        print("Hard (3)")
        print("Impossible (4)")
        print("Custom (5)")
        print("Change Logs (6)")

        difficulty_select = (input("-->> ")) # difficulty num, 1 = e, 2 = m, 3 = h, 4 = i, 5 = c , 6 = cl,        
        if difficulty_select in vaild_difficulty:
            if difficulty_select in vaild_difficulty_easy:
                difficulty = 1
            elif difficulty_select in vaild_difficulty_medium:
                difficulty = 2
            elif difficulty_select in vaild_difficulty_hard:
                difficulty = 3
            elif difficulty_select in vaild_difficulty_impossible:
                difficulty = 4
            elif difficulty_select in vaild_difficulty_custom:
                difficulty = 5
            elif difficulty_select in vaild_difficulty_change:
                difficulty = 6
        else: 
            print("Invaild Option")
            difficulty_select = 0

        if difficulty in hint_numbers:
            while hints == False:
                hints = str(input("Hints (y/n) "))
                if hints in yes_responses:
                    hints = True
                elif hints in no_responses:
                    hints = False
                else: 
                    print("Invaild Option\n")
                    hints = 0

    while(difficulty == 1 and play_again == 1): # Easy
        print("-----------------------------------------------")
        print("Easy Difficulty\n")
        print("A number from 1 to 9 will be chosen at random")
        print("You will have 5 guesses to find the correct number")
        play_again = 0
        numbers_guessed = []
        secret_number = 0
        secret_number = dice(1, 9) 
        guesses_left = 5
        guess_number = 0
        correct = False
        print("\nYou have "+str(guesses_left)+ " guesses left")

        while(guesses_left > 0):
            guess_number = int(input("\nPut your guess here: ")) # Forces an int value
            numbers_guessed.insert(5, guess_number) # Adds guess to 'guess list'   
            guesses_left = guesses_left - 1 # lowers guesses left on each guess

            if guess_number == secret_number:
                correct = True
            
            if correct == False:
                if(guess_number != secret_number):
                    print("You guessed the wrong number! You still have "+str(guesses_left)+" Attempt(s)")

                if(guess_number > 9):
                    print("Invaild Number (Too High)") 
                if(guess_number < 1):
                    print("Invaild Number (Too Low)")

                while(guesses_left == 0):
                    guesses_left = False
                    print("\nYou ran out of guesses! The correct number was "+str(secret_number)+"!\n")  
                    print("Your guesses were;") 
                    print(numbers_guessed)
                    play_again = str(input("\nPlay again? (y/n) "))
                    if play_again in vaild_responses:
                        if play_again in yes_responses:
                            play_again = 1
                            guesses_left = -1
                            secret_number = 0
                            time.sleep(1)          
                        if play_again in no_responses:
                            play_again = 0
                            difficulty = -1 # ends program
                            game_play = False
                            print("...")        
                            print("-----------------------------------------------")
                            break
                    else: print("Invaild Choice (y/n)")    

            while(correct == True):
                print("You guessed the correct number!\n")
                print("Your guesses were;")
                print(numbers_guessed)
                play_again = str(input("\nPlay again? (y/n) "))
                if play_again in vaild_responses:
                    if play_again in yes_responses:
                        play_again = 1
                        guesses_left = -1 # Set to -1 so it breaks out of the loop
                        guess_number = 0
                        correct = 2
                        time.sleep(1)
                    if play_again in no_responses:
                        game_play = False
                        difficulty = -1
                        guesses_left = -1
                        play_again = 0
                        print("...")        
                        print("-----------------------------------------------")
                        break
                else: print("Invaild Choice (y/n)") 
         
    while(difficulty == 2 and play_again == 1): # Medium
        print("-----------------------------------------------")
        print("Medium Difficulty\n")
        print("A number from 1 to 50 will be chosen at random")
        print("You will have 7 guesses to find the correct number")
        play_again = 0
        numbers_guessed = []
        secret_number = 0
        secret_number = dice(1, 50) 
        guesses_left = 7
        guess_number = 0
        correct = False
        print("\nYou have "+str(guesses_left)+ " guesses left")

        while(guesses_left > 0):
            guess_number = int(input("\nPut your guess here: ")) # Forces an int value
            numbers_guessed.insert(7, guess_number) # Adds guess to 'guess list'      
            guesses_left = guesses_left - 1 # lowers guesses left on each guess
            
            if guess_number == secret_number:
                correct = True
            
            if correct == False:
                if(guess_number != secret_number):
                    print("You guessed the wrong number! You still have "+str(guesses_left)+" Attempt(s)")

                if(guess_number > 50):
                    print("Invaild Number (Too High)")
                if(guess_number < 1):
                    print("Invaild Number (Too Low)")

                if hints == True:                        
                    if(guess_number < secret_number):
                        print("The Secret Number is Higher!\n ")
                    if(guess_number > secret_number):
                        print("The Secret Number is Lower\n ")
         
                while(guesses_left == 0):
                    guesses_left = False
                    print("You ran out of guesses! The correct number was "+str(secret_number)+"!\n")  
                    print("Your guesses were;") 
                    print(numbers_guessed)
                    play_again = str(input("\nPlay again? (y/n) "))
                    if play_again in vaild_responses:
                        if play_again in yes_responses:
                            play_again = 1
                            guesses_left = -1
                            secret_number = 0
                            time.sleep(1)           
                        if play_again in no_responses:
                            play_again = 0
                            difficulty = -1 # ends program
                            game_play = False
                            print("...")        
                            print("-----------------------------------------------")
                            break
                    else: print("Invaild Choice (y/n)") 
        
            while(correct == True):
                print("You guessed the correct number!\n")
                print("Your guesses were;")
                print(numbers_guessed)
                play_again = str(input("\nPlay again? (y/n) "))
                if play_again in vaild_responses:
                    if play_again in yes_responses:
                        play_again = 1
                        guesses_left = -1 # Set to -1 so it breaks out of the loop
                        guess_number = 0
                        correct = 2
                        time.sleep(1)
                    if play_again in no_responses:
                        game_play = False
                        difficulty = -1
                        guesses_left = -1
                        play_again = 0
                        print("...")        
                        print("-----------------------------------------------")
                        break
                else: print("Invaild Choice (y/n)")    
          
    while(difficulty == 3 and play_again == 1): # Hard
        print("-----------------------------------------------")
        print("Hard Difficulty\n")
        print("A number from 1 to 99 will be chosen at random")
        print("You will have 11 guesses to find the correct number")
        play_again = 0
        numbers_guessed = []
        secret_number = 0
        secret_number = dice(1, 99) 
        guesses_left = 11
        guess_number = 0
        correct = False
        print("\nYou have "+str(guesses_left)+ " guesses left")

        while(guesses_left > 0):
            guess_number = int(input("\nPut your guess here: ")) # Forces an int value
            numbers_guessed.insert(11, guess_number) # Adds guess to 'guess list'  
            guesses_left = guesses_left - 1 # lowers guesses left on each guess

            if guess_number == secret_number:
                correct = True

            if correct == False:
                if(guess_number != secret_number):
                    print("You guessed the wrong number! You still have "+str(guesses_left)+" Attempt(s)")

                if(guess_number > 99):
                    print("Invaild Number (Too High)")    
                if(guess_number < 1):
                    print("Invaild Number (Too Low)")
                
                if hints == True:                        
                    if(guess_number < secret_number):
                        print("The Secret Number is Higher!\n ")
                    if(guess_number > secret_number):
                        print("The Secret Number is Lower\n ")
                
                while(guesses_left == 0):
                    print("You ran out of guesses! The correct number was "+str(secret_number)+"!\n")  
                    print("Your guesses were;") 
                    print(numbers_guessed)
                    play_again = str(input("\nPlay again? (y/n) "))
                    if play_again in vaild_responses:
                        if play_again in yes_responses:
                            play_again = 1
                            guesses_left = -1
                            secret_number = 0
                            time.sleep(1)           
                        if play_again in no_responses:
                            play_again = 0
                            difficulty = -1 # ends program
                            game_play = False
                            print("...")        
                            print("-----------------------------------------------")
                            break
                    else: print("Invaild Choice (y/n)")     

            while(correct == True):
                print("You guessed the correct number!\n")
                print("Your guesses were;")
                print(numbers_guessed)
                play_again = str(input("\nPlay again? (y/n) "))
                if play_again in vaild_responses:
                    if play_again in yes_responses:
                        play_again = 1
                        guesses_left = -1 # Set to -1 so it breaks out of the loop
                        guess_number = 0
                        correct = 2
                        time.sleep(1)
                    if play_again in no_responses:
                        game_play = False
                        difficulty = -1
                        guesses_left = -1
                        play_again = 0
                        print("...")        
                        print("-----------------------------------------------")
                        break
                else: print("Invaild Choice (y/n)")    
                        
    while(difficulty == 4 and play_again == 1): # Impossible
        print("-----------------------------------------------")
        print("Impossible Difficulty\n")
        print("A number from 1 to 999 will be chosen at random")
        print("You will have 20 guesses to find the correct number")
        play_again = 0
        numbers_guessed = []
        secret_number = 0
        secret_number = dice(1, 999) 
        guesses_left = 20
        guess_number = 0
        correct = False
        print("\nYou have "+str(guesses_left)+ " guesses left")

        while(guesses_left > 0):
            guess_number = int(input("\nPut your guess here: ")) # Forces an int value
            numbers_guessed.insert(20, guess_number) # Adds guess to 'guess list'       
            guesses_left = guesses_left - 1 # lowers guesses left on each guess

            if guess_number == secret_number:
                correct = True
            
            if correct == False:
                if(guess_number != secret_number):
                    print("You guessed the wrong number! You still have "+str(guesses_left)+" Attempt(s)")

                if(guess_number > 999):
                    print("Invaild Number (Too High)") 
                if(guess_number < 1):
                    print("Invaild Number (Too Low)")

                if hints == True:                        
                    if(guess_number < secret_number):
                        print("The Secret Number is Higher!\n ")
                    if(guess_number > secret_number):
                        print("The Secret Number is Lower\n ")

                while (guesses_left == 0):
                    print("You ran out of guesses! The correct number was "+str(secret_number)+"!\n")     
                    print("Your guesses were;") 
                    print(numbers_guessed)
                    play_again = str(input("\nPlay again? (y/n) "))
                    if play_again in vaild_responses:
                        if play_again in yes_responses:
                            play_again = 1
                            guesses_left = -1
                            secret_number = 0
                            time.sleep(1)
            
                        if play_again in no_responses:
                            play_again = 0
                            difficulty = -1 # ends program
                            game_play = False
                            print("...")        
                            print("-----------------------------------------------")
                            break
                    else: print("Invaild Choice (y/n)")
              
            while(correct == True):
                print("You guessed the correct number!\n")
                print("Your guesses were;")
                print(numbers_guessed)
                play_again = str(input("\nPlay again? (y/n) "))
                if play_again in vaild_responses:
                    if play_again in yes_responses:
                        play_again = 1
                        guesses_left = -1 # Set to -1 so it breaks out of the loop
                        guess_number = 0
                        correct = 2
                        time.sleep(1)
                    if play_again in no_responses:
                        game_play = False
                        difficulty = -1
                        guesses_left = -1
                        play_again = 0
                        print("...")        
                        print("-----------------------------------------------")
                        break
                else: print("Invaild Choice (y/n)")    
 
    while (difficulty == 5 and play_again == 1): # Custom    
        max_range = 0
        min_range = 0
        vaild_range = False
        gen_range = 0 # no. of numbers that are between min and max
        while setup == False:
            while vaild_range_min == False:
                while min_range == 0:
                    print("\n---------------------------------------------------")   
                    min_range = input("Input Minimum Number\n-->> ")
                    if min_range.isnumeric():
                        vaild_range_min = True
                    else:
                        print(" \nError: NaN (Not a Number)")
                        min_range = 0
            print(str(min_range) + " Chosen as Minimum")
            print("---------------------------------------------------")    
            vaild_range_max= False
            while vaild_range == False:
                max_range = input("What Should the Highest possible number be? \n-->> ")
                if(max_range.isnumeric()):     
                    if(min_range > max_range):
                        print("\nError: Max Cannot be larger than min")
                        vaild_range_max = False
                    if(min_range == max_range):
                        print("\nError: Min and Max can't be the same")
                        vaild_range_max = False
                    else: vaild_range_max = True
                    break
                else:
                    print("\nError: NaN (Not a Number)")
                    max_range = 0

            print(str(max_range) + " Chosen as Maximum")
            print("\n---------------------------------------------------")
            print("Min: " + str(min_range) + " | Max: " + str(max_range)+ "\n")
            max_range = int(max_range)
            min_range = int(min_range)
            gen_range = gen_range + (max_range - min_range)
            while vaild_range_guess == False:
                guesses_left = input("Enter Guess Limit\n-->> ")
                if guesses_left.isnumeric():
                    guesses_left = int(guesses_left)
                    if guesses_left < gen_range:
                        vaild_range_guess = True
                        setup = True
                        if guesses_left == 0:
                            print("You cant have 0 guesses!")
                            setup = False
                            vaild_range_guess = False
                    if guesses_left > gen_range:
                        vaild_range_guess = False
                        guesses_left = 0
                        print("You cant have more guesses than the range!")
                else:
                    print("\nError NaN (Not a Number")
                    guesses_left = 0
    
        print("\n---------------------------------------------------")
        print("Min: " + str(min_range) + " | Max: " + str(max_range))
        print("You will have " +str(guesses_left)+ " guesses!")
        custom_guesses = guesses_left
    
        while setup == True:
            print("---------------------------------------------------")
            print("Custom Difficulty\n")
            print("A number from " +str(min_range)+ " to " +str(max_range)+ " will be chosen at random")
            print("You will have " +str(custom_guesses)+ " guesses to find the correct number")
            play_again = 0
            numbers_guessed = []
            secret_number = 0
            secret_number = dice(min_range, max_range) 
            guesses_left = custom_guesses
            guess_number = 0
            correct = False
            print("\nYou have "+str(guesses_left)+ " guesses left")

            while(guesses_left > 0):
                guess_number = int(input("\nPut your guess here: ")) # Forces an int value
                numbers_guessed.insert(guesses_left, guess_number) # Adds guess to 'guess list'
                guesses_left = guesses_left - 1 # lowers guesses left on each guess

                if guess_number == secret_number: 
                    correct = True
                
                if correct == False:
                    if(guess_number != secret_number):
                        print("You guessed the wrong number! You still have "+str(guesses_left)+" Attempt(s)")

                    if(guess_number > max_range):
                        print("Invaild Number (Too High)") 
                    if(guess_number < min_range):
                        print("Invaild Number (Too Low)")

                    if hints == True:                        
                        if(guess_number < secret_number):
                            print("The Secret Number is Higher!\n ")
                        if(guess_number > secret_number):
                            print("The Secret Number is Lower\n ")

                    while (guesses_left == 0):
                        print("\nYou ran out of guesses! The correct number was "+str(secret_number)+"!\n")  
                        print("Your guesses were;") 
                        print(numbers_guessed)
                        play_again = str(input("\nPlay again? (y/n) "))
                        if play_again in vaild_responses:
                            if play_again in yes_responses:
                                play_again = 1
                                guesses_left = -1
                                secret_number = 0
                                time.sleep(1)
            
                            if play_again in no_responses:
                                play_again = 0
                                guesses_left = -1
                                difficulty = -1 # ends program
                                game_play = False
                                setup = False
                                print("...")        
                                print("-----------------------------------------------")
                                break
                        else: print("Invaild Choice (y/n)") 
                               
                while(correct == True):
                    print("You guessed the correct number!\n")
                    print("Your guesses were;")
                    print(numbers_guessed)
                    play_again = str(input("\nPlay again? (y/n) "))
                    if play_again in vaild_responses:
                        if play_again in yes_responses:
                            play_again = 1
                            guesses_left = -1 # Set to - 1 so it break out of the loop
                            guess_number = 0
                            correct = 2
                            time.sleep(1)

                        if play_again in no_responses:
                            game_play = False
                            setup = False
                            difficulty = -1   
                            guesses_left = -1   
                            print("...\n-----------------------------------------------")
                    else: print("Invaild Choice (y/n)")    
          
    while(difficulty == 6): # Change Log
        change_log_page = 1
        print("-----------------------------------------------")
        print("Guess the number          Current Version: v1.3")
        print("")
        print("Version 1.3 (3/08/2022)")
        print("- New Difficulty option, Choose between Easy, Medium,\nHard and Impossible.\nAdded Option to use letters/word to choose a difficulty.\nMedium and above have togglable hints (Higher/Lower).\nOptimised code by making it longer :)\nChange log can now be closed.")
        print("")
        print("Version 1.2.1")
        print("- Removed prints used for testing")
        print("")
        print("Version 1.2 (28/08/2022)")
        print("- Updated starting menu")
        print("")
        print("Version 1.1 (27/08/2022)")
        print("- Play again option added")
        print("")
        print("Version 1.0 (25/08/2022)")
        print("- Release")
        print("")
        print("-----------------------------------------------")
        change_log_page = input("Close (y/y)\n-->> ")
        if change_log_page == 'y':
            change_log_page = 0
            difficulty = 0
        else: print("...")