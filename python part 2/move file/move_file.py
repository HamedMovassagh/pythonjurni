import os

sorce= "text.txt"
distion="D:\\text.txt"

try:
   if  os.path.exists(distion):
     print("the file already exsist ")
   os.replace(sorce,distion) 
   print("file replace")    

except FileNotFoundError :
    print("file dosent find")

