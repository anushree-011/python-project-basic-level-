import random
from replit import clear 
from logo import logo,stages
from words import word_list

chosen_word = random.choice(word_list)
word_length = len(chosen_word)

game = 0
lives = 6


from logo import logo,stages
print(logo)


display = []
for _ in range(word_length):
    display += "_"

while not game:
    guess = input("Guess a letter: ").lower()
    clear()
    if guess in display:
        print(f"You've already guessed {guess}")

    
    for position in range(word_length):
        letter = chosen_word[position]
      
        if letter == guess:
            display[position] = letter

    if guess not in chosen_word:
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        lives -= 1
        if lives == 0:
            game = 1
            print("You lose.")
    
    print(f"{' '.join(display)}")

    if "_" not in display:
        game = 1
        print("You win.")
    print(stages[lives])
