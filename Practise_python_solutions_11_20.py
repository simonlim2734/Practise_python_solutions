# from practisepython.org, my own solutions 

# Problem 11 answers 

# input_number = int(input("Give me a number: "))

# divisors = list(range(1, input_number))

# good_divisors = []

# for x in divisors: 
#     if input_number % x == 0:
#         good_divisors.append(x)

# print(good_divisors)

# if len(good_divisors) > 1:
#     print("Value " + str(input_number) + " is not a prime number")
# else: 
#     print("Value " + str(input_number) + " is a prime number")

# def prime_function(number):
#     input_number = int(number)
#     divisors = list(range(1, input_number))
#     good_divisors = []
#     for x in divisors:
#         if input_number % x == 0:
#             good_divisors.append(x)
#     print(good_divisors)
#     if len(good_divisors) > 1:
#         print("Value " + str(input_number) + " is not a prime number")
#     else: 
#         print("Value " + str(input_number) + " is a prime number")

# prime_function(101) # This will return a prime number 

# Problem 12 Solutions

# a = [5, 10, 15, 20, 30] 

# def list_terminal(list_input):
#     b = []
#     b.append(list_input[0])
#     b.append(list_input[-1])
#     return b

# print(list_terminal(a))

# Problem 13 Solutions

# def fibo(num):
#     fibo1 = [1]
#     fibo2 = [1,1]    
#     if num == 1:
#         return fibo1
#     elif num == 2:
#         return fibo2
#     else:
#         for x in range(1,int(num)-1):
#             fibo2.append(fibo2[-1] + fibo2[-2])
#         return fibo2

# Problem 14 Solutions

# a = [1,1,1,2,4,6,7,8,9,9,9,9]
# b = []

# function version of solution

# def list_cleaner(lists):
#     empty_list = []
#     for x in lists:
#         if x not in empty_list:
#             empty_list.append(x)
#     return empty_list

# print(list_cleaner(a))

# set version of solution

# c = a 
# c = set(c)
# c = list(c)
# print(c)

# # Problem 15 solution

# def string_reverse(string):
#     splitstring = string.split(" ")
#     c = list(range(0, len(splitstring)))
#     c = c[::-1]
#     d = [splitstring[x] for x in c]
#     return " ".join(d)
    
# print(string_reverse("What is my purpose"))
# print(string_reverse("Who are you?"))

# Problem 16 Solutions 
# import random
# import string

# a = input("Do you want a password? (Yes/No) : ")
# if a == "Yes":
#     ab = input("Do you want a strong or weak password (Strong/Weak) : ")
#     if ab == "Strong":
#         a = string.ascii_letters + "1234567890"
#         b = ""
#         for x in list(range(0,random.randrange(10,20))):
#             b = b + a[int(random.randint(0,61))]
#         print(b)
#         print("Password generated")
#     else:
#         a = ["one", "two" , "three" , "four" , "five", "six"]
#         print(a[random.randint(0,5)]+a[random.randint(0,5)])
#         print("Password generated")
# else: 
#     print("Password not generated")

# Problem 17 Solutions
# 
# Problem 18 Solutions
# 
# Problem 19 Solutions

#Problem 20 Solutions (Still need to do binary searches)

# def list_search(list, int):
#     if int in list:
#         print("Value is inside list")
#     else:
#         print("Value not inside list")