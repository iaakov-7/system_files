import os
print(os.getcwd())
print(os.listdir())
os.chdir("../") 
print(os.listdir())
os.chdir("system_files")
print(os.getcwd())