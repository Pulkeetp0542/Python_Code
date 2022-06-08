word_list = ["Monkey","Lion","Horse"]
#Randomly choose a word from the list
import random
chosen_word = random.choice(word_list)
#Ask the user to guess a letter and assign
guess = input("Guess a letter:").lower()
#Check the letter user Guess
for letter in chosen_word:
    if letter == guess:
        print("Right!")
    else:
        print("Wrong")