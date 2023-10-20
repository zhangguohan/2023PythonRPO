import random
import hangman_art
import hangman_words
#word_list = ["tank","zhang","pao"]
chose_word = random.choice(hangman_words.word_list)
print(f"{chose_word}")
display = []
word_length = len(chose_word)
for _ in range(word_length):
    display += "_"
print(display)

end_of_game = False
lives =6

print(hangman_art.logo3)
print("\nTo win, guess the word before the person is hung.\n")

while not end_of_game:
    guess = input("Guess a letter:").lower()
    for positon in range(word_length):
        letter = chose_word[positon]
        if letter == guess:
            display[positon] = letter
    if guess not in chose_word:
        lives -= 1
        print(hangman_art.stages[lives])
        if lives ==0:
            end_of_game = True
            print("your lose!")
    print(f"{''.join(display)}")

    if "_" not in display:
        end_of_game =True
        print("Your win ")
