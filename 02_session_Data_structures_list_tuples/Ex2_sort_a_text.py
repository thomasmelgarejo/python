
def sorter(str):
    str = str.lower().replace('a', '')
    str = str.lower().replace('e', '')
    #ect

    sortedlist = sorted(str,key=None,reverse=False)
    return sortedlist 

strin = "oerglwefa"

print(sorter(strin))

#løsning
def sort_cons(s):
    for i in ['a', 'e', 'i', 'o', 'u', 'y', ' ']:
        s = s.lower().replace(i,'')
    
    return sorted(s)

print(sort_cons('Hello world'))