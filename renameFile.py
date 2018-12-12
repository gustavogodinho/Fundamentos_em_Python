import os

def rename_files():
    #1 get files names
    file_list = os.listdir(r"C:\Phyton\prank")
    print(file_list)

    #2 for each file, rename it
    saved_path = os.getcwd()
    print ("Current Working Directory is "+saved_path)
    os.chdir(r"C:\Phyton\prank")
    for file_name in file_list:
        print("Old Name - "+file_name)
        tiraNumero = str.maketrans(dict.fromkeys("0123456789"))
        print("New Name - "+file_name.translate( tiraNumero))
        os.rename(file_name, file_name.translate(tiraNumero))



    os.chdir(saved_path)

rename_files()
