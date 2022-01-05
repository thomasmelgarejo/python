#Create a file and call it lyrics.txt (it does not need to have any content)
file1 = open('lyrics.txt', 'w')

#Create a new file and call it songs.docx and in this file write 3 lines of text to it.
file = open('songs.txt', 'w')
file.write('Hejsa\nHoho\nTep')
file.close

#open and read the content and write it to your terminal window. * 
    #readlines returner fuld fil som list
file1 = open('songs.docx', 'r')
lines1 = file1.readlines() 
file.close

# for l in lines1:
#     print(l)

    #readline return one line from stream
file2 = open('songs.docx', 'r')
lines2 = file2.read()
file2.close
#print(lines2)

    #read return hole file as string??
file3 = open('songs.docx', 'r')
lines3 = file3.readline() 
#file.close

while lines3:
    print(lines3)
    line3 = file3.readline()