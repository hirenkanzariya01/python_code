# ? how to reverce a string in a python
# str = "this"
# strLen = len(str)
# rev_str = ""

# for i in range(strLen - 1, -1, -1):
#     print(str[i], end='')


# for i in str:
#     rev_str = i + rev_str
# print(rev_str)


# ? how to cheack if a string contain only digits ?
# str = "123abcd23"
# if str.isdigit():
#   print('Yes String contain only digits')
# else:
#   print('No String can not contain digits')


# ? how do you cheack a string is a pelindrome
# str = "RAR"
# rev_str = ""
# for i in str:
#   rev_str = i + rev_str

# if str == rev_str:
#   print('This str is Pelendrome String ')
# else:
#   print('not Pelendrome')


# ? count vowels and consonnants
# str = "This is my dummy String "
# vovels = "aeiouAEIOU"
# vovels_count = 0
# consonants_count = 0

# for i in str:
#     if i == " ":
#         pass
#     else:
#         if i in vovels:
#             vovels_count = vovels_count + 1
#         else:
#             consonants_count = consonants_count + 1

# print("Vovels:- ", vovels_count)
# print("consonants :- ", consonants_count)


# ? find a longest word in a sentence
# str = "This is my dummmmmmmmmy String"
# arr = str.split()
# largest_word = ''
# largest_word_len = 0

# for i in arr:
#     if len(i) >= largest_word_len:
#       largest_word = i
#       largest_word_len = len(i)
# print(largest_word)

# ? convert a string into a list 
# str = 'im learn python'
# print(str.split(' '))


# ? replace all spaces with specific charactor ? 
str = 'im learn python'
print(str.replace(' ', ' - '))
