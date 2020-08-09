from random import choice

WORDS = ["hello", "donkey", "cat", "pig", "computer", "python", "variable"]

lives = 5
word = choice(WORDS).lower()
word_str = "*" * len(word)
game_state = 1 # 0 you lose, 1 game in play, 2 you win

name = input(f'Hi, welcome to Hangman. What is your name? ')
print(f'The word has {len(word)} letters: {word_str}')


while game_state == 1:
    if lives > 0:        
        if '*' in word_str:
            current_letter = input(f'{name} please choose a letter: ').lower()
            if current_letter not in word:
                lives -= 1
                if lives > 0:
                    print(f"{current_letter} is not in the word. You have {lives} guesses left. Please try again")
                    game_state = 1
                else:
                    game_state = 0
                    print(f"Sorry you have lost as you have no guesses left!!. The word was {word}")
            else:
                letter_indexes = [i for i, letter in enumerate(word) if letter == current_letter]
                if len(letter_indexes) == 1:
                    word_str = word_str[:letter_indexes[0]] + current_letter + word_str[letter_indexes[0] + 1:]
                    print(word_str)
                else:
                    for index in letter_indexes:
                        word_str = word_str[:letter_indexes[0]] + current_letter + word_str[letter_indexes[0] + 1:]
                    print(word_str)
        else:
            print(f"Congratulations you correctly guessed the word was {word}")
            game_state = 2

print("Goodbye...")


