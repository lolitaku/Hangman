import random
from hangman_body import hangmanBody
from os import system


my_file = open("little_prince_word_list.txt", "r")
my_data = my_file.read()
words = my_data.split()
print(words)

lives = 10
# entry_valid - set('abcdefghijklmnoprtsuvwxyz')

name = input("Enter your name: ")
print(f"Hello {name}") 
print("---------")
print("Try to guess the word in less than 10 attempts")

def randomWord():
    return words[random.randint(0, len(words) -1)]

def playGame():
    word = randomWord()
    progress = ''
    for i in range(len(word)):
        progress += '_'
    incorrect = 0
    guesses = []
    while True:
        _ = system('clear')
        # print(word)
        guessesString = ''
        for i in range(len(guesses)):
            if i != len(guesses) and i !=0:
                guessesString += ', '
            guessesString += guesses[i]
        print(f'Past guesses: {guessesString}')
        print(hangmanBody(incorrect))

        if progress == word:
            print(progress)
            print('You win!')
            break
        if incorrect >=10:
            print('You lose! I expected more from you!')
            print(f'Sorry! The word was "{word}". Try again!!! :)')
            break
        print(progress)
        print('Guess a letter!')

        guess = input()
     
        if guess not in guesses:
            guesses.append(guess)
        if guess in word:
            # print(f'The letter {guess} is in the word.')
            for i in range(len(word)):
                if guess == word[i]:
                    progressStart = progress[0:i]
                    progressEnd = progress[i+1:]
                    progress = progressStart + guess + progressEnd
        else:
            print(f'The letter {guess} is not in the word. Try again.')
            incorrect +=1

if __name__ == '__main__':
    while True:
        print('Hi! Want to play hangman? (yes / no)')
        answer = input()
        if answer.lower() == 'yes':
           playGame()
        if answer.lower() == 'no':
            print('Bye bye! Have a good day!')
            break

input("Press Enter to Leave! ")