# from practisepython.org

# Problem 31 solutions

# unknown_word = "DISCUS" 
# word_list = []
# for x in unknown_word:
#     word_list += x 
 
# board = ("_ "*int(len(unknown_word)))
# board_list = board.split()

# guess_box = []

# while True: 
#     print("Welcome to Hangman! \n")
#     guess = input("Guess your letter : ")
#     if guess in guess_box:
#         print("Already guessed try again \n")
#         continue
#     guess_box += guess
#     number_index = 0 
#     for x in word_list:
#         number_index += 1 
#         if x == guess:
#             position = number_index - 1 
#             board_list[position] = guess
#     print("\n" + " ".join(board_list) + "\n")
#     if "_" not in board_list:
#         print("Hangman solved! Game ends")
#         break

# Problem 32 solutions

#Make a function that generates a random word from the SOWPODS database first 

# import random

# #generate a random word from SOWPODS text file
# def random_word(): 
#     with open("c:/Users/Simon/My Drive/Python_practise_scripts/sowpods.txt", 'r') as f:
#         lines = f.readlines()
#         random_word = lines[random.randint(0,len(lines)-1)]
#         return random_word


# unknown_word = random_word() 
# print(unknown_word)

# # turn unknown word into a list, each letter is an element in the list
# word_list = []
# for x in unknown_word:
#     word_list += x 
 
# # make a string based game board of "_" indicating number of letters to be guessed
# board = ("_ "*(int(len(unknown_word))-1))

# #turn game board into a list
# board_list = board.split()

# # where letters guessed show up, if already guessed we tell the player, but don't penalize them 
# guess_box = set()

# #Number of incorrect guesses allowed 
# incorrect_guess_times = 6  

# while True: 
#     print("Welcome to Hangman! \n")
#     guess = input("Guess your letter : ")
#     if guess in guess_box:
#         print("Already guessed try again \n _____________________")
#         continue
#     else:
#         guess_box.add(guess)

#     number_index = 0 
#     for x in word_list:
#         number_index += 1 
#         if x == guess:
#             position = number_index - 1 
#             board_list[position] = guess

#     if guess in word_list:
#         print("\nCorrect guess!")
#     elif guess not in word_list:
#         print("\nIncorrect guess!")
#         incorrect_guess_times -= 1

#     print("You have " + str(incorrect_guess_times) + " lives left")

#     if incorrect_guess_times == 0:
#         print("Sorry, you lost! Game ends.")
#         break


#     print("\n" + " ".join(board_list) + "\n" + "____________________")
#     if "_" not in board_list:
#         print("Hangman solved! Game ends.")
#         break
        
# Problem 33 Solutions 

# dictionary = {

#     "Simon" : r"1994/04/11",
#     "Remy" : r"1993/03/10",
#     "Kevin" : r"1992/02/09"

# }
# print("Welcome to the birthday dictionary. We know the birthdays of : \n")

# lists = list(dictionary.keys())

# for x in lists:
#     print(x + "\n")

# prompts = input("Which birthday do you want to look up? ")

# print("The birthday of {} is {}.".format(prompts,dictionary[prompts]))

# Problem 34 Solutions 
# Json intro

# import json

# dictionary = {

#     "Simon" : r"1994/04/11",
#     "Remy" : r"1993/03/10",
#     "Kevin" : r"1992/02/09"

# }

# with open("c:/Users/Simon/My Drive/Python_practise_scripts/info.json", "r") as g:
#     info = json.load(g)

# dict_add_name = input("Input new scientist name : ")
# dict_add_bday = input("Input birthday : ")
# info[str(dict_add_name)] = dict_add_bday

# with open("c:/Users/Simon/My Drive/Python_practise_scripts/info.json", "w") as f:
#     json.dump(info,f)

# with open("c:/Users/Simon/My Drive/Python_practise_scripts/info.json", "r") as h:
#     info_new = json.load(h)

# print(info_new)

# Problem 35 Solutions

# import json
# from collections import Counter
# import re

# with open("c:/Users/Simon/My Drive/Python_practise_scripts/info.json", "r") as h:
#      info_new = json.load(h)

# values = list(info_new.values())

# months = {
#     "01" : "January",
#     "02" : "February",
#     "03" : "March", 
#     "04" : "April",
#     "05" : "May", 
#     "06" : "June", 
#     "07" : "July",
#     "08" : "August",
#     "09" : "September",
#     "10" : "October", 
#     "11" : "November",
#     "12" : "December"
# }

# empty_list = []

# for x in values:
#     y = re.sub(r"\d{4}/","", x)
#     y = re.sub(r"/\d{2}", "", y)
#     empty_list.append(months[y])

# c = dict(Counter(empty_list))
# print(c)

# Problem 36 Solutions
# from bokeh.plotting import figure, show, output_file
# import json
# from collections import Counter
# import re

# with open("c:/Users/Simon/My Drive/Python_practise_scripts/scientist_birthdays.json", "r") as h:
#      info_new = json.load(h)

# values = list(info_new.values())

# months = {
#     "01" : "January",
#     "02" : "February",
#     "03" : "March", 
#     "04" : "April",
#     "05" : "May", 
#     "06" : "June", 
#     "07" : "July",
#     "08" : "August",
#     "09" : "September",
#     "10" : "October", 
#     "11" : "November",
#     "12" : "December"
# }

# empty_list = []

# for x in values:
#     y = re.sub(r"/.*", "", x)
#     empty_list.append(months[y])

# c = dict(Counter(empty_list))

# x_categories = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

# x = list(c.keys())

# y = list(c.values())

# p = figure(x_range = x_categories)
# p.vbar(x=x, top = y, width = 0.5)
# show(p)

# Problem 37 solutions 

# def horz(num):
#     a = " --- --- ---"   
#     b = "|   |   |   |"
#     for x in range(num):
#         print(a)
#         print(b)
#     print(a)

# horz(3)

# Problem 38 Solutions 

# a = "Simon"
# b = 20
# current_yr = 2025
# print(f"This person's name is {a}, and their age be {b} they will be 100 in the year {(100-b)+current_yr}")

# Problem 39 Solutions

# import datetime

# name = "Simon"

# age = 31

# current = datetime.datetime.now()

# print(f"This person's name is {name}, and their age be {age} they will be 100 in the year {(100-age)+current.year}")

# Problem 40 Solutions 

# import random

# number = random.randint(1, 9)
# number_of_guesses = 0
# while True:
# 	guess = int(input("Guess a number between 1 and 9: "))
# 	if guess not in list(range(1,10)):
# 		print("Invalid number input")
# 		continue
# 	number_of_guesses += 1
# 	if guess == number:
# 		break
# print(f"You needed {number_of_guesses} guesses to guess the number {number}")