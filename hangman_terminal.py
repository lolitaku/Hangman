import random
from hangman_body import draw_hangman_body
from os import system
import logging


# creating logging info file with data
logging.basicConfig(level=logging.INFO, filename="hangman.log", filemode = "w", 
format="%(asctime)s - %(levelname)s - %(message)s")
logging.info("info")

# making list from txt file 
my_file = open("little_prince_word_list.txt", "r")
my_data = my_file.read()
word = my_data.split()


lives = 10

# greeting with a player
name = input("Enter your name: ")
logging.info(f"Hello {name}") 
print("---------")
print("Try to guess the word in less than 10 attempts. Good luck!")

# generate random word list
# creating function to play the game
def get_random_word() -> str:
    return word[random.randint(0, len(word) -1)]

def play_game() ->None:
    word = get_random_word()
    progress = ''
    for i in range(len(word)):
        progress += '_'
    incorrect = 0
    tries = []


    while True:
        _ = system('clear')
        # clear window game
        guessesValue = ''
        
        for i in range(len(tries)):
            if i != len(tries) and i !=0:
                guessesValue += ', '
            guessesValue += tries[i]
        print(f'Your guesses: {guessesValue}')
        print(draw_hangman_body(incorrect))

        if progress == word:
            print(progress)
            print('Congratulation! You win!')
            break
        if incorrect >=10:
            print('You lose! I expected more from you!')
            logging.info(f'Sorry! The word was "{word}". Try again!!! :)')
            print(f'Sorry! The word was "{word}". Try again!!! :)')
            break
        print(progress)
        
        guess = input()
     
        if guess not in tries:
            tries.append(guess)
        if guess in word:
            # print(f'The letter {guess} is in the word.')
            for i in range(len(word)):
                if guess == word[i]:
                    progressStart = progress[0:i]
                    progressEnd = progress[i+1:]
                    progress = progressStart + guess + progressEnd
        else:
            logging.info(f'The letter {guess} is not in the word. Try again.')
            print(f'The letter {guess} is not in the word. Try again.')
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