# #class-based Context manager

class ContextManager():
    def __init__(self):
        print('init method called')
          
    def __enter__(self):
        print('enter method called')
        return self
      
    def __exit__(self, exc_type, exc_value, exc_traceback):
        print('exit method called')
  
  
with ContextManager() as constManagerObject:
    print('constManagerObject: ', constManagerObject)


#************************************************************************
#et praktisk eksempel med en fil

# class FileManager():
#     def __init__(self, filename, mode):
#         self.filename = filename
#         self.mode = mode
#         self.file = None
          
#     def __enter__(self): #buildup 
#         self.file = open(self.filename, self.mode)
#         return self.file
      
#     def __exit__(self, exc_type, exc_value, exc_traceback): #teardown
#         self.file.close()
  
# # skriver til fil 
# with FileManager('test.txt', 'w') as f: #r=read, a=append, w=write, x=create
#     f.write('Tekst til indsættelse')
  

# with FileManager('test.txt', 'a') as f: #r=read, a=append, w=write, x=create
#     print(f"Er filen lukket1: {f.closed}")
#     f.write('Mere tekst')
#     print(f"Er filen lukket2: {f.closed}")
# print(f"Er filen lukket3: {f.closed}") #har her forladt scope

#**********************************************************************
# #Function-based Context Manager

# from contextlib import contextmanager

# @contextmanager
# def hello_context_manager():
#     print("Entering the context...")
#     yield "Hello, World!"
#     print("Leaving the context...")

# with hello_context_manager() as hello:
#     print(hello)



#****************************************************************************************

# from contextlib import contextmanager #fra python blibiotek

# @contextmanager
# def open_file(filename, mode):
#     f = open(filename, mode)
#     try:
#         yield f
#     finally:
#         f.close()


# with open_file('bohr.txt', 'r') as f:
#     print(f.read())