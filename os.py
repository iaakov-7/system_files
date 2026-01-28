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
           
def return_py_files(path_to_file):
    all_files = os.listdir(path_to_file)
    py_files = []
    for file in all_files:
        if file.endswith(".py"):
            py_files.append(file)
    print(all_files)        
    return py_files
print(return_py_files("../../"))

def dict_ends(path_to_dir):
    all_files = os.listdir(path_to_dir)
    list_ends = []
    dict_num_ends = {}
    for file in all_files:
        if os.path.isfile(f"{path_to_dir}/{file}"):
            f = file.split(".")
            list_ends.append(f".{f[1]}")
    for end in list_ends:
        if end not in dict_num_ends:
            dict_num_ends[end] = 1
        else:
            dict_num_ends[end] += 1            
    return dict_num_ends
print(dict_ends("../../"))
        
        