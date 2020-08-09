import random, time

#Word lists to randomly choose from
WORDS = ["hello", "donkey", "cat", "pig", "computer", "python", "variable"]
humanNames = ["Zappy", "Spelga", "Jooe", "Joshua", "Andrew", "Pili", "Connie"]
superHeroes = ['ironman', 'robin', 'flash', 'thor', 'spiderman', 'superman', 'deadpool', 'antman']

word = []
word_str = []
game_state = 1
category = ""

name = input(f'Hi, welcome to Hangman. What is your name? ')
print("Hello", name.lower(), "let's start playing Hangman!")
time.sleep(1)


while game_state == 1:
    #Choosing a wordlist from the above defined ones
    while True:
        if category.upper() == 'S':
            secretWord = random.choice(superHeroes)
            break
        elif category.upper() == 'W':
            secretWord = random.choice(WORDS)
            break
        elif category.upper() == 'H':
            secretWord = random.choice(humanNames)
            break
        else:
            category = input("Select a word list: S for Super-Heroes W for random words and H for human names; X to exit: ")

        if category.upper() == 'X':
            print("Bye. See you next time!")
            game_state = 0
            break

    if game_state:
        secretWordList = list(secretWord)
        lives = (len(secretWord) + 2)

        #Adding blank lines to word to create the blank secret word
        for n in secretWordList:
            word.append('_ ')
        print("Your Secret word is: ", (lives -2), " character long " +''.join(word))

        print("The number of allowed guesses for this word is:", lives)


        #starting the game
        while game_state:

            print("Guess a letter:")
            letter = input()

            if letter in word_str:
                print("You already guessed this letter, try something else.")

            else:
                lives -= 1
                word_str.append(letter)
                if letter in secretWordList:
                    print("Nice guess!")
                    if lives > 0:
                        print("You have ", lives, 'guess left!')
                    for i in range(len(secretWordList)):
                        if letter == secretWordList[i]:
                            letterIndex = i
                            word[letterIndex] = letter.lower()
                    print("Your Secret word is: " + ''.join(word))

                else:
                    print("Oops! Try again.")
                    if lives > 0:
                        print("You have ", lives, 'guess left!')
                    print("Your Secret word is: " + ''.join(word))


            #Win/loss logic for the game
            joinedList = ''.join(word)
            if joinedList.lower() == secretWord.lower():
                print("Yay! you won.")
                break
            elif lives == 0:
                print("Too many Guesses!, Sorry better luck next time.")
                print("The secret word was: "+ secretWord.lower())
                break
    break            
print("Bye!")