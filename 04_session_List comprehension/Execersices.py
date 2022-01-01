#1) Create a list of capital letters in the english alphabet

#2) Create a list of capital letter from the english aplhabet, but exclude 4 with the Unicode code point of either 70, 75, 80, 85.

#3) Create a list of capital letter from from the english aplhabet, but exclude every second between F & O

#Opgave1
list_uni_letters = [x for x in range(100) if x>=65 and x<=90]
#list_uni_letters = [int(x) for x in list_uni_letters]

# [print(chr(x)) for x in list_uni_letters]
list_uni_letters = [chr(x) for x in list_uni_letters]

# print(chr(list_uni_letters))
print(list_uni_letters)