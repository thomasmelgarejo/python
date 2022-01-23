#henter module private_test som indeholder private access elementer
from private_test import A_Class

class a:

    objA_class = A_Class('priv', 'pub')
    # print(objA_class)

    # print(objA_class.publicAtt)

    # print(objA_class.__privatAtt)   #kan ikke tilgå privat attribute
    
    #print(objA_class._A_Class__privatAtt)   #underscore class, så kan privat tilgåes

    objFunk = A_Class('para1', 'para2')
    
    #kalder private klasse
    print(objFunk._A_Class__funk1())

    # objFunk = A_Class.funk('parm2')
    # print(objFunk)

