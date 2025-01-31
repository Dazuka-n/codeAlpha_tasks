import random
# STEP 0 : Create HangMan Stages
Stages = [
   ''' +---=+
      |    |
      O    | DEAD !!
     /|\   |
     / \   |
           |
     =========''',
   '''+----+
      |    |
      O    |
     /|\   |
     /     |
           |
     =========''',
   '''+----+
      |    |
      O    |
     /|\   |
           |
           |
     =========''',
   ''' +----+
      |    |
      O    |
     /|    |
           |
           |
     =========''',
   ''' +----+
      |    |
      O    |
      |    |
           |
           |
     =========''',
   '''+----+
      |    |
      O    |
           |
           |
           |
     =========''',
   '''+----+
      |    |
           | 
           |
           |
           |
     =========''']

print("GAME START")
# STEP 1 : GENERATE A RANDOM WORD 
words = ["apple","banana","mclaren","asylum","katseye","bronze","dragon","dishwasher","bridge","magma","brush","golden","arabian","chinese","britsh"]
chosen_word = random.choice(words)

# STEP 2 : GENERATE BLANK SPACES
display = []
for i in range(len(chosen_word)):
    display += '_'
print(display,"\n") 

lives = 6
game_over = False
while not game_over  :

    # STEP 3 : GUESS A LETTER
    guessed_letter = input("guess the letter : ").lower()

    # STEP 4 : CHECK IF LETTER IS PRESESNT OR NOT
    for position in range(len(chosen_word)) :
      letter = chosen_word[position]
      if letter == guessed_letter:
        display[position] = guessed_letter
        # Display at screen
    print(display)

    # STEP 5 : if no lose a life if yes game continues
    if guessed_letter not in chosen_word :
      lives -= 1

      # STEP 6 : checks if life remains or not if no you lose
      print("lives left : " , lives)
      if lives == 0 :
        game_over = True
        print("you lose, the word was : ", chosen_word)

     # STEP 7 : YOU WINN if no letter remain
    if '_' not in display :
       game_over = True
       print("you win!!")
    
    print(Stages[lives])
        
        
  