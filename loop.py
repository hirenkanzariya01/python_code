# ? Print Even Number from 1 to 50
# for i in range(1, 51, 2):
#   print(i+1)

# for i in range(1, 51):
#     if i % 2 == 0:
#         print(i, end=" ")


# Sum of Number from 1 to N
# N = int(input("Enter Number :- "))
# total = 0
# for i in range(1, N+1):
#   total = total + i
# print('Total', total)


# ? Find The Factorial Of A Number using loop
# num = 5
# fact = 1
# #  fact of 5 = 1*2*3*4*5
# for i in range(1, num + 1 ):
#   fact = fact * i

# print(fact)

# ? print a table of any number

# table = int(input('Enter A Number to Print A Table :- '))
# for i in range(1 , 11):
#   print(table , 'X', i , '=', i * table)

# ? Count a Digits in a number using loop
# number = 10002300
# str_number = str(number)
# count = 0
# for i in str_number:
#     count = count + 1

# print('Total Digits :- ', count)


# Pattern Print (Triangle)
# *
# **
# ***
# ****
# *****
# ******

# for i in range(1, 6):
#   print("* " * i)

# for i in range(1, 6):
#     for j in range(1, i + 1):
#         print("* ", end=" ")
#     print()

# ? break in python

# for i in range(1, 21):
#   if i == 10:
#     continue
#   print(i)

# name = "vivek badra"
# for i in name:
#   if i == 'a':
#     break
#   print(i)