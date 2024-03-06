#Step 5

import random
from hangman_words import word_list
from hang_art import logo ,stages

#TODO-1: - Update the word list to use the 'word_list' from hangman_words.py

chosen_word = random.choice(word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6

#TODO-3: - Import the logo from hangman_art.py and print it at the start of the game.
print(logo)

#Testing code
print(f'Pssst, the solution is {chosen_word}.')

#Create blanks
display = []
for _ in range(word_length):
    display += "_"

print(f"{' '.join(display)}")

print(f"\n***YOUR WORD HAVE {len(chosen_word)} LETTERS***")

guessed_letters=[]

while not end_of_game:
    guess = input("\nGuess a letter: ").lower()
    
    if guess in guessed_letters:
        print(f"\nThe letter {guess} is already guessed.please input another letter\n")
        guess = input("Guess a letter: ").lower()
    guessed_letters.append(guess)

    #TODO-4: - If the user has entered a letter they've already guessed, print the letter and let them know.
    count=0
    #Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        #print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
        if letter == guess:
            display[position] = letter
            count+=1
            
    if count>0:
        print("\nYOU GUESSED A CORRECT LETTER\n")
    #Check if user is wrong.
    if guess not in chosen_word:
        #TODO-5: - If the letter is not in the chosen_word, print out the letter and let them know it's not in the word.
        print(f"\nThe letter {guess} not in the word\n")
        lives -= 1
        print(stages[lives])
        if lives == 0:
            end_of_game = True
            print("You lose.retry")

    #Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")
    
       

    #Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("congratulations!! You win.")

    #TODO-2: - Import the stages from hangman_art.py and make this error go away.
    