#Use python build in modules.
#Find and use 3rd party modules.
#Save and Share your modules installed in a docker container.
#work with markdown documents.
#Work with the module BeautifullSoup for webscrabing.

#Hent specifik funktion fra module
from  my_module import printfunction1
printfunction1()

import my_module
my_module.printfunction2()

p1 = my_module.person1
print('Henter data fra dict', p1['name'])


import my_module as nytnavn
nytnavn.printfunction2()
