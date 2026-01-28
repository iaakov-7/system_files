import os
print(os.getcwd())
print(os.listdir())
os.chdir("../") 
print(os.listdir())
os.chdir("system_files")
print(os.getcwd())
def print_files(path_to_dir):
    list = os.listdir(path_to_dir)
    for value in list:
        if os.path.isfile(f"{path_to_dir}/{value}"):
            print(value)
        else:
            print_files(f"{path_to_dir}/{value}")
print_files("../")           
