import random
from hangmanstages import stages

word_list = ["python","sharks","compensation"]
end_of_game = False
lives = 6

chosen_word=random.choice(word_list)

display = ['_' for _ in chosen_word]

while not end_of_game and lives!=0:
    guess = input("Enter a letter:").lower()
    for pos in range(len(chosen_word)):
        if guess == chosen_word[pos]:
            display[pos] = guess
    
    if guess not in chosen_word:
        lives -= 1
        print(stages[lives])
        if lives == 0:
            end_of_game = True
            print(f"The chosen word was: {chosen_word}")
            print("You lost!")
    
    if '_' not in display:
        end_of_game = True
        print("You win!")
    print(display)