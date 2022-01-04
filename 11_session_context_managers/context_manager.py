# class ContextManager():
#     def __init__(self):
#         print('init method called')
          
#     def __enter__(self):
#         print('enter method called')
#         return self
      
#     def __exit__(self, exc_type, exc_value, exc_traceback):
#         print('exit method called')
  
  
# with ContextManager() as manager:
#     print('with statement block')

#**********************************************************************
#et praktisk eksempel med en fil

# class FileManager():
#     def __init__(self, filename, mode):
#         self.filename = filename
#         self.mode = mode
#         self.file = None
          
#     def __enter__(self): #metode kaldes
#         self.file = open(self.filename, self.mode)
#         return self.file
      
#     def __exit__(self, exc_type, exc_value, exc_traceback): #
#         self.file.close()
  
# # skriver til fil 
# with FileManager('test.txt', 'w') as f: #r=read, a=append, w=write, x=create
#     f.write('Tekst til indsættelse')
  

# with FileManager('test.txt', 'a') as f: #r=read, a=append, w=write, x=create
#     print(f"Er filen lukket1: {f.closed}")
#     f.write('Mere tekst')
#     f.write('cccc')
#     print(f"Er filen lukket2: {f.closed}")
# print(f"Er filen lukket3: {f.closed}") #har her forladt scope

#****************************************************************************************

from contextlib import contextmanager #fra python blibiotek

@contextmanager
def open_file(filename, mode):
    f = open(filename, mode)
    try:
        yield f
    finally:
        f.close()


with open_file('bohr.txt', 'r') as f:
    print(f.read())