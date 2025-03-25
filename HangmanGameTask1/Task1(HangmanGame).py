# 1.generate a random word
import random
import Hangman_stages
word_list = ["apple", "beautiful", "potato"]
lives =6
chosen_word = random.choice(word_list)
print(chosen_word)
#print(len(chosen_word))
# 2.replace each letter of random word with dash "-"
display = []
#for letter/i in range(len(chosen_word)): # 0,1,2,3,4,5
for letter in chosen_word:
    display += "_"
print(display)

game_over = False
while not game_over:
  # user guess a letter
  # compare each guess letter with the letter of words that given in the word_list# put the guess letter in right place
  guessed_letter= input("Guess a letter").lower() # x _ _ _ _ _

  #for letter in chosen_word:
  for position in range(len(chosen_word)):# 0 1 2 3 4
      letter = chosen_word[position]
      if letter == guessed_letter: # a ==x
        #print("Match")
        display[position] = guessed_letter
  print(display)
  if guessed_letter not in chosen_word:
     lives -= 1
     if lives == 0:
        game_over = True
        print("You lose")
  print(display)
  if "_" not in display:
        game_over = True
        print("You win")
        print(f"The word is {chosen_word}")
  print(Hangman_stages.stages[lives])
          #display[chosen_word.index(letter)] = guessed_letter
#print(display)
