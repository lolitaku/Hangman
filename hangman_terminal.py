import random
from hangman_body import draw_hangman_body
from os import system
import logging
import time


# creating logging info file with data
logging.basicConfig(level=logging.INFO, filename="hangman.log", filemode = "w", 
format="%(asctime)s - %(levelname)s - %(message)s")

# making list from txt file 
my_file = open("little_prince_word_list.txt", "r")
my_data = my_file.read()
all_words = my_data.split()


lives = 10

# greeting with a player
name = input("Enter your name: ")
print(f"Hello {name}")
print("---------")
print("Try to guess the word in less than 10 attempts. Good luck!")

# generate random word list
# creating function to play the game
def get_random_word(word_list: list) -> str:
    return word_list[random.randint(0, len(word_list) -1)]



def play_game() -> None:
    incorrect = 0
    tries = []
    word = get_random_word(all_words)
    progress = ''
    for letter in range(len(word)):
        progress += '_'
    
    while True:
        _ = system('clear')
        # clear window game
        guessesValue = ''
        
        for letter in range(len(tries)):
            if letter != len(tries) and letter !=0:
                guessesValue += ', '
            guessesValue += tries[letter]
        print(f'Your guesses: {guessesValue}')
        print(draw_hangman_body(incorrect))

        if progress == word:
            print(progress)
            logging.info('Congratulation! You win! The word was "{word}" ')
            print('Congratulation! You win! The word was "{word}" ')
            break
        if incorrect >=10:
            print('You lose! I expected more from you!')
            logging.info(f'Sorry! The word was "{word}". Try again!!! :)')
            print(f'Sorry! The word was "{word}". Try again!!! :)')
            break
        print(progress)
        
        
        guess = input()
        guess = guess.lower()

        while len(guess) == 1 and guess.isalpha():
            print(guess)
            break

        else:
            print('Enter a single letter to continue!')
            time.sleep(1.0)
            continue
     
        if guess not in tries:
            tries.append(guess)
        if guess in word:
            # print(f'The letter {guess} is in the word.')
            for letter in range(len(word)):
                if guess == word[letter]:
                    progressStart = progress[0:letter]
                    progressEnd = progress[letter+1:]
                    progress = progressStart + guess + progressEnd

        elif guess in guessesValue:
            print('You have already guessed that letter. Try again!')
            time.sleep(1.0)
        
        else:
            logging.info(f'The letter {guess} is not in the word. Try again.')
            print(f'The letter {guess} is not in the word. Try again.')
            time.sleep(1.0)
            incorrect +=1

if __name__ == '__main__':
    while True:
        print('Hi! Want to play hangman? (yes / no)')
        answer = input()
        if answer.lower() == 'yes':
           play_game()
        if answer.lower() == 'no':
            print('Bye bye! Have a good day!')
            break

input("Press Enter to Leave! ")