#DICTIONARY

#Dictionary element are pairs key/valye
#Key must be immutable
#Key is unique

#create dict
    #first way
dictionary1 = {'key1': 'value1', 'key2': 'value2' }
print('dictionary1', dictionary1['key1'])  #dictionary1 value2
print('dictionary1: ', dictionary1) #{'key1': 'value1', 'key2': 'value2'}


    #second way
dictionary2 = dict([('key1','value1'),('key2','value2')])
print('dictionary2: ', dictionary2)

#add new entry
dictionary1['key3'] ='value3'
print('dictionary1 after add: ', dictionary1)

#delete key/value
del dictionary1['key3']
print('dictionary1 after delete: ', dictionary1)

#adding value to existing key
dictionary1['key3'] ='value4'
print('dictionary1 existing key ', dictionary1)