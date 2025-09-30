# My own solutions for the practice problems from practicepython.org

# Practise problem 1 answer

# name = input("Input your name: ")
# age = int(input("Input your age: "))
# repeats = int(input("Input a number: "))

# this_year = 2025
# year_100 = this_year + ( 100 - age)

# message = f"Your name is {name}. You will turn 100 in year {year_100}."
# print((message + "\n" ) * repeats) 

# Practise problem 2 answer

# number = int(input("Input number: "))
# if number % 2 == 0: 
#     print("Number is even")
#     if number % 4 == 0:
#         print("Number is multiple of 4")
# else: 
#     print("Number is odd")

# num = int(input("Input first number: "))
# check = int(input("Input second number here: "))

# if num % check == 0: 
#     print("first number divides into second")
# else: 
#     print("first number does not divide into second")

# Problem 3 answer 
# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

# b = []

# for x in a: 
#     if x < 5 :
#         print(x)
#         b.append(x)

# print(b)

# # List comprehension example 
# # "for iterable x in list a, if x is less than 13 then return x if x does not equal 3, else if x equals 3 then return 4"
# b = [ x if x != 3 else 4 for x in a if x < 13]

# print(b)

# Problem 4 answers 

# number = int(input("Number that you want: "))
# y = list(range(1, number))

# divides_into_number = [x for x in y if (number % x == 0)]
# print(divides_into_number)

# Problem 5 answers

# import random    
# a = random.sample(range(1, 50), random.randrange(1,50))
# b = random.sample(range(1, 50), random.randrange(1,50))

# c = []
# for x in a:
#   if x in b:
#     if x not in c:
#         c.append(x)

# c = [x for x in a if x in b]

# print(sorted(a))
# print(sorted(b))
# print(sorted(c))

# Set solution

# c = a + b 
# c = set(c)
# c = sorted(list(c))

# Problem 6 answers 

# string = list(input("Input a string: "))
# a = string
# b = string[::-1]

# if a == b:
#     print("Palindrome")
# else:
#     print("No Palindrome")

# Problem 7 answers (list comphrehension)

# a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
# b = [x for x in a if x % 2 == 0 ]
# print(b)

# Problem 8 answers

#rock = 1
#paper = 2 
#scissors = 3

#main takeaways
#make sure your variables are clear 
#reflect on what makes the spaghetti code worse than the cleaner code
    # takes logic away from a lot of == and if statements, condense into a code of two numbers
    # using a dictionary to convert from user input into win/lose code
    # use the function to generate the win/lose code from the user input
    # This method is much better than using the spaghetti code as it's much easier to troubleshoot errors or add a new win/lose condition 

# cleaner code
# gamedict = {
#     "rock"      : "1",
#     "paper"     : "2",
#     "scissors"  : "3"
# }

# PlayerOneWins = ["13","21","32"]
# PlayerTwoWins = ["12","23","31"]

# def ProcessInputs(input1, input2):
#     first_num = gamedict[input1]
#     second_num = gamedict[input2]
#     return str(first_num + second_num)

# while True: 
#     game_start = input("Do you want to play a game? (Yes/No) ")
#     if game_start != "Yes":
#         print("You didn't say Yes!")
#         break
#     else:
#         player1 = input("Give me first player input: ")
#         player2 = input("Give me second player input: ")
#         print(f"First player input: {player1}")
#         print(f"Second player input: {player2}")
#         combined_input = ProcessInputs(player1, player2)
#         if combined_input in PlayerOneWins:
#             print("First player wins")
#         elif combined_input in PlayerTwoWins:
#             print("Second player wins")
#         else:
#             print("Draw")

#Spaghetti code version 

        # if second_input == "rock" or "paper" or "scissors":
        #     if third_input == "rock" or "paper" or "scissors":
        #         if second_input == "rock" and third_input == "scissors" or \
        #         second_input == "paper" and third_input == "rock" or \
        #         second_input == "scissors" and third_input == "paper":
        #             print("First player wins")
        #         elif second_input == "rock" and third_input == "rock" or \
        #         second_input == "paper" and third_input == "paper" or \
        #         second_input == "scissors" and third_input == "scissors":
        #             print("Draw")
        #         elif second_input == "rock" and third_input == "paper" or \
        #         second_input == "paper" and third_input == "scissors" or \
        #         second_input == "scissors" and third_input == "rock":
        #             print("Second player wins")
        #         else:
        #             print("Invalid response detected from player 2")
        #     else:
        #         print("Invalid response detected from player 1")

# Problem 9 answers 

# import random
# random_number = random.randint(1,9)
# guesses = 0

# while True:
#     game_start = input("Input either \"start\" or \"exit\" ")
#     if game_start == "exit":
#         print("Game exited")
#         print("User guessed " + str(guesses) + " number of times")
#         break
#     elif game_start == "start": 
#         user_input = int(input("Give me a random number between 1 and 9: "))
#         guesses = guesses + 1
#         if user_input < random_number:
#             print("Guessed too low")
#         elif user_input > random_number:
#             print("Guessed too high")
#         else:
#             print("Guessed right")
#     else:
#         print("Invalid input detected")

# Problem 10 answers 

import random 

listing = []

# make list numbers ranging from 0 to 100, with 1 to 100 elements in the list, do it twice 
a = sorted(random.sample(range(100), random.randint(1,100)))
b = sorted(random.sample(range(100), random.randint(1,100)))

# iterate through list a, if element in list b return element in this newlist
newlist = [x for x in a if x in b ]

# for loop for removing duplicates
for x in newlist: 
    if x not in listing:
        listing.append(x)
print((listing))

lists = list(set(newlist))
print(sorted(lists))
