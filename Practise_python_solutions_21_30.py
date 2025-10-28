# from practisepython.org

# Problem 21 Solutions

# with open("test_text_file.txt", 'w') as open_file:
#     open_file.write("Booleans are okay")

# Problem 22 Solutions 

# with open('C:/Users/Simon/My Drive/Python_practise_scripts/nameslist.txt', 'r') as open_file:
#     text = open_file.read()

# text = text.splitlines()

# dictionary = {
#     "Darth" : 0,
#     "Lea" : 0 
# }

# for x in text:
#     if x == "Darth":
#         dictionary["Darth"] += 1
#     elif x == "Lea":
#         dictionary["Lea"] += 1

# print(dictionary["Darth"])
# print(dictionary["Lea"])

# with open('C:/Users/Simon/My Drive/Python_practise_scripts/Training_01.txt', 'r') as open_file:
#     texts = open_file.read()

# texts = texts.splitlines()

# new_text = []
# for x in texts:
#     x = x[3:]
#     x = x[:-25]
#     new_text.append(x)


# new_dict = {}

# for x in new_text:
#     if x not in new_dict:
#         new_dict[x] = 1
#     elif x in new_dict:
#         new_dict[x] += 1

# print(new_dict)

# Problem 23 Solutions 

# with open('C:/Users/Simon/My Drive/Python_practise_scripts/primenumbers.txt', 'r') as open_file:
#      primes = open_file.read()

# with open('C:/Users/Simon/My Drive/Python_practise_scripts/happynumbers.txt', 'r') as open_file:
#      happys = open_file.read()

# primes = primes.split("\n")

# happys = happys.split("\n")

# duplicates = []

# for x in primes:
#     if x in happys:
#         duplicates.append(x)

# Problem 24 Solutions

# def grid(number = int(input("How big is your grid : "))):
#     a = " ---"
#     b = "   |"
#     c = number
#     d = (a*c + "\n" + "|" + b*c + "\n" + a*c)
#     e = ("\n" + "|" + b*c + "\n" + a*c)
#     return ( d + (e*(c-1)))

# print(grid())

# Problem 25 Solution 

# a = 50
# max = 100
# min = 0  

# Search, simple method
# while True:
#     b = input("Is " + str(a) + " the number in your head? (Yes/Higher/Lower) : ")
#     if b == "Yes":
#         print("Yay! We found your number, it's " + str(a))
#         break
#     elif b == "Lower":
#         print("Aw we haven't found it yet")
#         a -= 1
#     elif b == "Higher":
#         print("Aw we haven't found it yet")
#         a += 1

# Search, binary search method 
# while True:
#     b = input("Is " + str(a) + " the number in your head? (Yes/Higher/Lower) : ")
#     if b == "Yes":
#         print("Yay! We found the number it's : " + str(a))
#         break
#     elif b == "Lower":
#         print("Aw we haven't found it yet")
#         max = a
#         a = (a+min)//2
#         print(a)
#     elif b == "Higher":
#         print("Aw we haven't found it yet")
#         min = a
#         a = (a+max)//2
#     else:
#         print("Invalid reponse given, good day")

# Problem 26 Solution 

# import math

# a = [[2, 2, 1],[1, 2, 1],[2, 1, 1]]

# a1 = a[0][0]
# a2 = a[0][1]
# a3 = a[0][2]

# b1 = a[1][0]
# b2 = a[1][1]
# b3 = a[1][2]

# c1 = a[2][0]
# c2 = a[2][1]
# c3 = a[2][2]

# outcomes = [ 
#     math.prod(a[0]),
#     math.prod(a[1]),
#     math.prod(a[2]),
#     math.prod([a1,b1,c1]),
#     math.prod([a2,b2,c2]),
#     math.prod([a3,b3,c3]),
#     math.prod([a1,b2,c3]),
#     math.prod([a3,b2,c1])
# ]

# for x in outcomes:
#     if x == 8:
#         print("Player 2 wins")
#         break
#     elif x == 1: 
#         print("Player 1 wins")
#         break

# Problem 27 Solution

# game = [[0, 0, 0],
# 	    [0, 0, 0],
# 	    [0, 0, 0]]

# while True:
#     player_input = input("What Player are you? Player (1/2) : ")
#     zero_count = 0
#     if player_input == "1":
#         print("You are Player 1")
#         input1 = input("What is your move : ")
#         input1 = input1.strip("()")
#         input1 = input1.split(",")
#         if game[int(input1[0])-1][int(input1[1])-1] == 0:
#             game[int(input1[0])-1][int(input1[1])-1] = "X"
#         else:
#             print("Coordinate already entered")
#         print(game)
#     elif player_input == "2":
#         print("You are Player 2")
#         input2 = input("What is your move : ")
#         input2 = input2.strip("()")
#         input2 = input2.split(",")
#         if game[int(input2[0])-1][int(input2[1])-1] == 0:
#             game[int(input2[0])-1][int(input2[1])-1] = "O"
#         else:
#             print("Coordinate already entered")
#         print(game)
#     for x in game:
#         y = x.count(0)
#         zero_count += y
#     print("Available moves left: " + str(zero_count)) 
#     if zero_count == 0:
#         print("No more moves available")
#         break
#     game_end = input("Continue? (Y/N) : ")
#     if game_end == "Y":
#         continue
#     else:
#         break

# Problem 28 solutions 

# def bignum(x,y,z):
#     a = max(x,y,z)
#     return ("The maximum number is : " + str(a))
    
# print(bignum(4,2,3))

# Problem 29 solutions

# import math

# game = [[0, 0, 0],
# 	     [0, 0, 0],
# 	     [0, 0, 0]]

# game1 = [[0, 0, 0],
# 	      [0, 0, 0],
# 	      [0, 0, 0]]
 

# def grid(number):
#     a = " ---"
#     b = " | "
#     c = "| "
#     d = " |"
#     e = number
#     f = (str(a*e) + "\n" + 
#          c + str(game[0][0]) + b + str(game[0][1]) + b + str(game[0][2]) + d + "\n"  + 
#          str(a*e) + "\n" + 
#          c + str(game[1][0]) + b + str(game[1][1]) + b + str(game[1][2]) + d + "\n" + 
#          str(a*e) + "\n" + 
#          c + str(game[2][0]) + b + str(game[2][1]) + b + str(game[2][2]) + d + "\n" + 
#          str(a*e) )
#     return (f)


# # drawing on the grid 

# while True:
#     player_input = input("What Player are you? Player (1/2) : ")
#     zero_count = 0
#     if player_input == "1":
#         print("You are Player 1")
#         input1 = input("What is your move : ")
#         input1 = input1.strip("()")
#         input1 = input1.split(",")
#         if game[int(input1[0])-1][int(input1[1])-1] == 0:
#             game[int(input1[0])-1][int(input1[1])-1] = "X"
#             game1[int(input1[0])-1][int(input1[1])-1] = 1
#         else:
#             print("Coordinate already entered")
#         print(game)
#         print(grid(3))
#     elif player_input == "2":
#         print("You are Player 2")
#         input2 = input("What is your move : ")
#         input2 = input2.strip("()")
#         input2 = input2.split(",")
#         if game[int(input2[0])-1][int(input2[1])-1] == 0:
#             game[int(input2[0])-1][int(input2[1])-1] = "O"
#             game1[int(input2[0])-1][int(input2[1])-1] = 2
#         else:
#             print("Coordinate already entered")
#         print(game)
#         print(grid(3))
#     for x in game:
#         y = x.count(0)
#         zero_count += y
#     print("Available moves left: " + str(zero_count)) 
#     if zero_count == 0:
#         print("No more moves available")
#         break
#     outcomes = [ 
#         math.prod(game1[0]),
#         math.prod(game1[1]),
#         math.prod(game1[2]),
#         math.prod([game1[0][0],game1[1][0],game1[2][0]]),
#         math.prod([game1[0][1],game1[1][1],game1[2][1]]),
#         math.prod([game1[0][2],game1[1][2],game1[2][2]]),
#         math.prod([game1[0][0],game1[1][1],game1[2][2]]),
#         math.prod([game1[0][2],game1[1][1],game1[2][0]])
#     ]    

#     if 8 in outcomes:
#         print("Player 2 wins")
#         break
#     elif 1 in outcomes: 
#         print("Player 1 wins")
#         break
#     else:
#         print("No winner yet")
#     print(outcomes)
#     game_end = input("Continue? (Y/N) : ")
#     if game_end == "Y":
#         continue
#     else:
#         break

# Problem 30 solutions

# import random

# with open("c:/Users/Simon/My Drive/Python_practise_scripts/sowpods.txt", 'r') as f:
#     lines = f.readlines()


# random_word = lines[random.randint(0,len(lines)-1)]

# print(random_word)