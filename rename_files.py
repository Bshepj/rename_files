import os

def rename_files():
    #(1) Get files name from a given folder
    file_list = os.listdir(r"S:\Udacity\Programming Foundations with Python\Lesson 1\prank")
    #print (file_list)
    saved_path = os.getcwd()
    print("Current Working Directory is "+saved_path)
    os.chdir(r"S:\Udacity\Programming Foundations with Python\Lesson 1\prank")
    #(2) For each file rename filename
    for file_name in file_list:
        print("Old Name - "+file_name)
        print("New Name - "+file_name.translate(None, "0123456789"))
        os.rename(file_name, file_name.translate(None, "0123456789"))
    os.chdir(saved_path)
    
rename_files()
