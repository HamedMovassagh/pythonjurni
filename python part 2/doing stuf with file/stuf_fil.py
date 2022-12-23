import os

father=("C:\\Users\\hamed\\Desktop\\text")

if os.path.exists(father):
    print("yes the file it exists")
    if os.path.isfile(father):
        print("yes it is file")
    elif os.path.isdir(father):
        print("its directory")

else:
    print("no its not exists")