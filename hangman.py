#a hangman game that is raletively complete
#the function that I realized there are:
#check "not valid" input/repeat guess check/play again/word_bank/category search/blur search

import random

def draw_rack():
    print "+--------+"
    print "|        |"
    for i in range(0, 7):
        print "|"
    print "H A N G M A N"
    print "----------"

def draw_hangman_1():
    print "+--------+"
    print "|        |"
    print "|        O"
    for i in range(0, 6):
        print "|"
    print "----------"

def draw_hangman_2():
    print "+--------+"
    print "|        |"
    print "|        O"
    print "|        |"
    for i in range(0, 5):
        print "|"
    print "----------"

def draw_hangman_3():
    print "+--------+"
    print "|        |"
    print "|        O"
    print "|       /|"
    for i in range(0, 5):
        print "|"
    print "----------"

def draw_hangman_4():
    print "+--------+"
    print "|        |"
    print "|        O"
    print "|       /|\\"
    for i in range(0, 5):
        print "|"
    print "----------"

def draw_hangman_5():
    print "+--------+"
    print "|        |"
    print "|        O"
    print "|       /|\\"
    print "|       /"
    for i in range(0, 4):
        print "|"
    print "----------"

def draw_hangman_6():
    print "+--------+"
    print "|        |"
    print "|        O"
    print "|       /|\\"
    print "|       / \\"
    for i in range(0, 4):
        print "|"
    print "----------"
    print "Game Over!"

def check_repeat():
    global letter
    global new_list
    for i in range(0, len(new_list)):
        if letter == new_list[i]:
            global repeat_handler
            repeat_handler = True
            letter = raw_input("The letter is guessed before. Guess aother letter?")


def check_right():
    for i in range(0, len(word_to_list)):
        global letter
        global new_list
        if letter == word_to_list[i]:
            new_list[i] = letter
            global right_handler
            right_handler = True


def game():
    draw_rack()

    global word_bank_fruit
    global word_bank_pet
    global word_bank_coding

    while True:
        input_category = raw_input("Choose a category(fruit/pet/coding language)")
        category = input_category.lower()
        if category in "fruit":
            secret_word = random.choice(word_bank_fruit)
            break
        elif category in "pet":
            secret_word = random.choice(word_bank_pet)
            break
        elif category in "coding language":
            secret_word = random.choice(word_bank_coding)
            break
        else:
            continue
        break

    global word_to_list
    word_to_list = list(secret_word)

    global new_list
    new_list = []

    for i in range(0, len(word_to_list)):
        new_list.append("_")

    new_string = " ".join(new_list)
    print new_string

    while True:

        global play_again_handler

        if "".join(new_list) == secret_word:
            print "You win!"
            while True:
                play_again = raw_input("Do you want to play again?(y or n)")
                if play_again == "n":
                    play_again_handler = False
                    break
                elif play_again == "y":
                    break
                else:
                    continue
            break

        global right_handler
        right_handler = False

        global repeat_handler
        repeat_handler = False

        global letter
        alphabet = "abcdefghijklmnopqrstuvwxyz"
        alphabet_to_list = list(alphabet)
        while True:
            input = raw_input("guess a letter?")
            letter = input.lower()
            if letter in alphabet_to_list:
                break
            else:
                continue
            break

        check_repeat()

        check_right()

        new_string = " ".join(new_list)
        print new_string

        if right_handler == False:
            global wrong_counter
            wrong_counter += 1
            if wrong_counter == 1:
                draw_hangman_1()
            elif wrong_counter == 2:
                draw_hangman_2()
            elif wrong_counter == 3:
                draw_hangman_3()
            elif wrong_counter == 4:
                draw_hangman_4()
            elif wrong_counter == 5:
                draw_hangman_5()
            elif wrong_counter == 6:
                draw_hangman_6()
                while True:
                    play_again = raw_input("Do you want to play again?(y or n)")
                    if play_again == "n":
                        play_again_handler = False
                        break
                    elif play_again == "y":
                        break
                    else:
                        continue
                break

wrong_counter = 0
letter = ""
new_list = []
play_again_handler = True
right_handler = False
repeat_handler = False
word_bank_fruit = ["apple", "pear", "grape", "orange", "strawberry", "watermelon", "lemon"]
word_bank_pet = ["dog", "cat", "snake", "bird", "hamster", "rabbit"]
word_bank_coding = ["python", "javascript", "java", "swift", "php", "ruby"]


while True:
    if play_again_handler == True:
        game()
    if play_again_handler == False:
        print "Bye!"
        break
