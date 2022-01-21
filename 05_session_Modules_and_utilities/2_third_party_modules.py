#BRUG af fremmede moduler  ->https://www.crummy.com/software/BeautifulSoup/bs4/doc/

#step1 - Er de korrekte tools installere? pip?
# py --version                  --> Python 3.9.6
# py py -m pip --version        --> pip 21.1.3 from C:\Users\

#step2 - find package - https://pypi.org/

#Step3 - installere fremmede packages
# pip install beautifulsoup4
# pip install htmlparser           ->vælger parser, lxml, htm5lib, htmlparser eller ??

print("================")

html_doc = """<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""
print(html_doc)

from bs4 import BeautifulSoup
soup = BeautifulSoup(html_doc, 'html.parser')

print('Pring title: ', soup.title)
print('Pring title string: ', soup.title.string)
print('Pring all text: ', soup.get_text)



#PIP COMMANDS
# Uninstall a package--------------------------------------------->pip uninstall package_name
#List installed packages ----------------------------------------->pip list  
#Upgrade a package ----------------------------------------------->pip install package_name --upgrade
#Check that installed packages are compatible--------------------->pip check
#Get information about a specific package------------------------->pip show package_name