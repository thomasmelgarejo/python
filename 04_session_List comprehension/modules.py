#Viser hvordan man importere et module
#Viser hvordan man kalder/bruger, en string, en list, en metode, en klasse


import test_module

#print(test_module._string) #printer string fra module 

#print(test_module._list) #printer list fra module

test_module._method(['argument1', 'argument2', 'argument3', 'argument4']) #kalder metode i modulet test_module

x = test_module._class #Bruger klasse

#Man kan hente alternativt hente module direkte ind i py filen
#Syntaks from <module_name> import <name_på_thing_man_vil_importere>

#_string skrives uden module navn foran
#BEMÆRK hvis variable (_string) allerede eksistere overskrives den??
from test_module import _string, _list
print('Dette er direkte import:',_string) 

#Importere alt fra module_name
#from <module> import * 

#Kan give alternativt navn til importeret thing hvis navne konflikt

#Der findes også packages der kan indeholde flere modules