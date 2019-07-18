#Alanza Blake
#7/16/2019
import random

#list of words for the computer to generate

#list 1 is professions
#list 2 is sports
#list 3 is clothing
#list 4 is holidays 
#list 5 is furniture
#list 6 is historically black colleges and universities
#list 7 is ivy league schools
#list 8 is caribbean countries/islands 
#list 9 is movie/TV genres 
#list 10 is colors
words=[
    ['doctor', 'lawyer', 'cashier', 'engineer', 'manager', 'entrepreneur', 'surgeon', 'dentist', 'pharmacist', 'nurse', 'architect', 'therapist', 'actress', 'pilot', 'accountant', 'technician', 'firefighter', 'teacher', 'veterinarian', 'mechanic', 'judge', 'waiter'],#professions
    ['basketball', 'softball', 'baseball', 'cheerleading', 'tennis', 'lacrosse', 'soccer', 'track', 'dance', 'football', 'rugby', 'swimming', 'gymnastics', 'wrestling', 'kickboxing', 'karate', 'archery', 'bowling', 'hockey', 'volleyball'],#sports
    ['shirt', 'pants', 'dress', 'bra', 'underwear', 'hat', 'scarf', 'jacket', 'shoes', 'boots', 'sneakers', 'skirt', 'jumpsuit', 'romper', 'jeans'],#clothing
    ['juneteenth', 'christmas', 'thanksgiving', 'easter', 'passover', 'halloween', 'hanukkah', 'kwanzaa'],#holidays
    ['table', 'couch', 'oven', 'microwave', 'television', 'bed', 'dresser', 'refrigerator', 'chairs', 'bookcase', 'painting', 'lamp', 'carpet'],#furniture
    ['spelman', 'howard', 'hampton', 'morehouse', 'lincoln', 'ncat', 'famu', 'southern', 'tuskegee', 'xavier', 'dillard', 'bennett', 'fisk', 'claflin', 'morgan'],#hbcus
    ['upenn', 'harvard', 'yale', 'princeton', 'brown', 'columbia', 'cornell', 'dartmouth'],#ivy leagues
    ['cuba', 'haiti', 'jamaica', 'guyana', 'bahamas', 'martinique', 'belize', 'dominica', 'grenada', 'barbados', 'aruba', 'antigua', 'guadeloupe'],#caribbean countries/islands
    ['comedy', 'horror', 'action', 'adventure', 'romance', 'crime', 'drama', 'documentary', 'musical', 'western', 'mystery', 'fantasy'],#movie genres
    ['pink', 'red', 'brown', 'yellow', 'orange', 'black', 'white', 'purple', 'blue', 'gray', 'gold', 'silver', 'green', 'turquoise']#colors
       ]

def used_let(used):#function to make the used letters list a string instead of a set
    used_list=""#empty string
    for i in used:#elements in used
        used_list+=i#add to empty string
        used_list+=", "#add comma so it's still a list
    used_list=used_list.strip(", ")#strip the comma at the end
    return used_list#value when the function is set to a variable
def screen(h, c, a, l, u, d):#function to print the screen(hint, counter, answer, letter, used, dashes)
    for i in range(len(a)):#going through answer string 
        if a[i] == l:#if the element in answer is equal to the letter the user guessed 
            d[i]=l#change the dash to the letter
    
    print("Hint:", h)
    if c >= 0:#if counter is still 0
        print(' |')#starting pole
    if c >= 1:#if the user got 1 wrong
        print(' 0')#head
    if c == 2:#if the user got 2 wrong
        print(' |')#body
        print(' |')
    if c == 3:#if the user got 3 wrong
        print('\|')#first arm
        print(' |')
    if c >= 4:#if the user got 4 wrong 
        print('\|/')#second arm 
        print(' |')
    if c ==5:#if the user got 5 wrong 
        print(' | ')#lower body
    if c ==6:#if the user got 6 wrong
        print('/| ')#first leg
    if c >= 7:#if the user got 7 wrong 
        print('/|\ ')#second leg
    word_string=""#empty string
    for let in d:#go through the list
        word_string+=let#add each dash to the empty string
    print()#space
    print(word_string)#print out string of dashes
    print()#space
    
def play():
    a=random.randint(0, 9)#elements of words list
    num=len(words[a])-1#range from 0 to the last index
    b=random.randint(0, num)#elements of each list in word list
    answer=words[a][b]#randomly generated element
    if a == 0:#if it's the 1st list
        hint="Professions"#name the category
    elif a == 1:#if it's the 2nd list
        hint="Sports"#name the category
    elif a == 2:#if it's the 3rd list
        hint="Clothing"#name the category 
    elif a == 3:#if it's the 4th list
        hint="Holidays"#name the category 
    elif a == 4:#if it's the 5th list
        hint="Furniture"#name the category
    elif a == 5:#if it's the 6th list
        hint="HBCUS"#name the category
    elif a == 6:#if it's the 7th list
        hint="Ivy Leagues"#name the category
    elif a == 7:#if it's the 8th list
        hint="Caribbean Countries/Islands"
    elif a == 8:#if it's the 9th list
        hint="Movie Genres"#name the category
    elif a == 9:#if it's the 10th list
        hint="Colors"#name the category
    counter=0#create counter
    game_counter=0#create counter to determine whether user wins
    #create a used already list
    used=set()#empty set
    letter=""#user input#initializing letter to use in loop
    answer_length=len(answer)*'-'#replicating the dashes
    dashes=list(answer_length) #list of the dashes 
    invalid_char="`~!@#$%^&*()-_+=/*-+<,.>?:;'\"{}[]\|"#string of invalid inputs
    
    print("Hint:", hint)#print hint for the first try
    print()#space
    print(answer_length)#print the dashes for the first try
    
    #use separate if statements not elif
    while counter != 8 and game_counter!=len(set(answer)):#until counter reaches 8 or until the user guesses all the letters
        print()#space
        letter=input("Guess a letter: ")#user guess
        
        #use multiple nested conditional statements to determine whether the user's input is valid
        if len(letter) != 1 or letter in invalid_char:#if the users input is more than one letter or they didn't enter a letter
            letter=input("This is an invalid character. Please enter a letter: ")#guess again
            if len(letter) != 1 or letter in invalid_char:#if the users input is more than one letter or they didn't enter a letter
                letter=input("This is an invalid character. Please enter a letter: ")#guess again 
                if len(letter) != 1 or letter in invalid_char:#if the users input is more than one letter or they didn't enter a letter
                    letter=input("This is an invalid character. Please enter a letter: ")#guess again
                    if len(letter) != 1 or letter in invalid_char:#if the users input is more than one letter or they didn't enter a letter
                        letter=input("This is an invalid character. Please enter a letter: ")#guess again
                        if len(letter) != 1 or letter in invalid_char:#if the users input is more than one letter or they didn't enter a letter
                            letter=input("This is an invalid character. Please enter a letter: ")#guess again
                            if len(letter) != 1 or letter in invalid_char:#if the users input is more than one letter or they didn't enter a letter
                                letter=input("This is an invalid character. Please enter a letter: ")#guess again
                                if len(letter) != 1 or letter in invalid_char:#if the users input is more than one letter or they didn't enter a letter
                                    letter=input("This is an invalid character. Please enter a letter: ")#guess again
                                    if len(letter) != 1 or letter in invalid_char:#if the users input is more than one letter or they didn't enter a letter
                                        letter=input("This is an invalid character. Please enter a letter: ")#guess again
                                        if len(letter) != 1 or letter in invalid_char:#if the users input is more than one letter or they didn't enter a letter
                                            letter=input("This is an invalid character. Please enter a letter: ")#guess again
                                            if len(letter) != 1 or letter in invalid_char:#if the users input is more than one letter or they didn't enter a letter
                                                letter=input("This is an invalid character. Please enter a letter: ")#guess again
                                                if len(letter) != 1 or letter in invalid_char:#if the users input is more than one letter or they didn't enter a letter
                                                    letter=input("This is an invalid character. Please enter a letter: ")#guess again
                                                    if len(letter) != 1 or letter in invalid_char:#if the users input is more than one letter or they didn't enter a letter
                                                        letter=input("This is an invalid character. Please enter a letter: ")#guess again
                                                        if len(letter) != 1 or letter in invalid_char:#if the users input is more than one letter or they didn't enter a letter
                                                            letter=input("This is an invalid character. Please enter a letter: ")#guess again
                                                            if len(letter) != 1 or letter in invalid_char:#if the users input is more than one letter or they didn't enter a letter
                                                                letter=input("This is an invalid character. Please enter a letter: ")#guess again         
        #let the user know when they've used the word before
        if letter in used:#multiple nested if statements to keep on letting the user guess
            letter=input("You've already used that letter. Guess another one: ")#guess again
            if letter in used:#if previous guess was in the already used letters
                letter=input("You've already used that letter. Guess another one: ")#guess again
                if letter in used:#if previous guess was in the already used letters
                    letter=input("You've already used that letter. Guess another one: ")#guess again
                    if letter in used:#if previous guess was in the already used letters
                        letter=input("You've already used that letter. Guess another one: ")#guess again
                        if letter in used:#if previous guess was in the already used letters
                            letter=input("You've already used that letter. Guess another one: ")#guess again
                            if letter in used:#if previous guess was in the already used letters
                                letter=input("You've already used that letter. Guess another one: ")#guess again
                                if letter in used:#if previous guess was in the already used letters
                                    letter=input("You've already used that letter. Guess another one: ")#guess again
                                    if letter in used:#if previous guess was in the already used letters
                                        letter=input("You've already used that letter. Guess another one: ")#guess again
                                        if letter in used:#if previous guess was in the already used letters
                                            letter=input("You've already used that letter. Guess another one: ") #guess again   
                                            if letter in used:#if previous guess was in the already used letters
                                                letter=input("You've already used that letter. Guess another one: ") #guess again
                                                if letter in used:#if previous guess was in the already used letters
                                                    letter=input("You've already used that letter. Guess another one: ") #guess again
                                                    if letter in used:#if previous guess was in the already used letters
                                                        letter=input("You've already used that letter. Guess another one: ") #guess again
                                                        if letter in used:#if previous guess was in the already used letters
                                                            letter=input("You've already used that letter. Guess another one: ") #guess again
                                                            if letter in used:#if previous guess was in the already used letters
                                                                letter=input("You've already used that letter. Guess another one: ") #guess again                                                            
        print()#space
        if letter not in answer:#if the letter isn't in the word
            counter += 1#add a counter to it
        if letter in answer:#if letter is in the word
            game_counter+=1#add a counter to it
        screen(hint, counter, answer, letter, used, dashes)#call screen with 6 parameters
        used.add(letter)#add letter to the already used list
        prevLet=used_let(used)#value is the returned string
        print("Used letters = "+ prevLet)#string that shows previous guest
    if counter == 8:#if counter reaches 8
        print()#space
        print("Game over! Sorry, you lose! The answer was %s." % (answer))
    if game_counter==len(set(sorted(answer))):#if the counter is the same number as the elements of the set
        print()#space
        print("You win! Congratulations!")
    
def main():   
    #print instructions to game 
    print("Welcome to hangman! You will guess the word \nletter by letter. If you guess an incorrect letter,\na body part will appear. If the whole body appears \nthen you lose. If you guess the word before the whole \nbody appears then you win! Ready? Let's get started!")
    print()#space
    play()#call play function
    print()#space
    ask=input("Would you like to play again(Y/N)? ")#ask user to repeat game
    
    while ask.upper() == 'Y' or ask.upper() == "YES":#until the user says no
        play()#call play function in loop
        print()#space
        ask=input("Would you like to play again(Y/N)? ")#ask user to repeat game
        print()#space

main()#call main loop


