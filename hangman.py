import random
from this import d
from hangman_words import word_list
from hangman_art import stages
from hangman_art import logo

#1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.
print(logo)
chosen_word = random.choice(word_list)
print(chosen_word)
#-1: - Create a variable called 'lives' to keep track of the number of lives left. 
#Set 'lives' to equal 6.
lives = 6
#- Create an empty List called display.
display = []
for i in range(len(chosen_word)):
    display.append("_")
#print(display)
#-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
#-: - Use a while loop to let the user guess again. The loop should only stop once the user has guessed all the letters in the chosen_word and 'display' has no more blanks ("_"). Then you can tell the user they've won.

while "_" in display and lives != 0:
   guess = input("guess a letter: ").lower()
  #: - If the user has entered a letter they've already guessed, print the letter and let them know.
   if guess in display:
       print(f"you guessed the letter {guess}")


# - Loop through each position in the chosen_word;
#-If the letter at that position matches 'guess' then reveal that letter in the display at that position.
#- Check if the letter the user guessed (guess) is one of the letters in the chosen_word.
   c = 0 
   for e in chosen_word:
    
        if e == guess:

            display[c] = e
        
        c += 1
   if guess not in chosen_word:
       lives -= 1
       print(f"the letter {guess} is not on the word. You lost a life.")
   print(stages[lives])
   
   print(f"{''.join(display)}")
   print(lives)

if lives != 0:
   print("you won")
else:
   print("you lose")

