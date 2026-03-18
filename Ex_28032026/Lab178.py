import os

file_name= os.open('TestData.txt',os.O_RDWR)
os.write(file_name,b'Hello I am writing')
os.close(file_name)