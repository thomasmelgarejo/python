#Create a list of strings with names in it. (l = [‘Claus’, ‘Ib’, ‘Per’])
listNames = ['Andersd','Thomaassc', 'Petere', 'Sørenb', 'Hansf', 'Ludviga']
# print(listNames)

#Sort this list by using the sorted() build in function.
listNames1 = sorted(listNames)
# print(listNames1)

#Sort the list in reversed order.
listNames2 = sorted(listNames, reverse=True)
# print(listNames2)

#Sort the list on the lenght of the name.
def sortByLength(listNames3):
    listNames3 = sorted(listNames3, key=len, reverse=True)
    #print(listNames3)

#sortByLength(listNames)

#Sort the list based on the last letter in the name.
def lastLetterFunc(str):
    return str[-1]

def sortByLastLetter(list):
    return sorted(list, key=lastLetterFunc)

#print(sortByLastLetter(listNames))

#Sort the list with the names where the letter ‘a’ is in the name first.
def is_containsLetter(letter, string):
    if letter in string:
        return True
    else:
        return False

def choosenListSort(list):
    choosenList = []
    for i in range(len(list)):
        if(is_containsLetter('a', list[i])):
            choosenList.append(list[i])
    return sorted(choosenList)

print(choosenListSort(listNames))

#Claus løsning
def a_in(s):
    if 'a' in s.lower():
        return True
    return False

sorted(names, key=a_in)
