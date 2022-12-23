#
#
#def alphabet_position(text):
#   alphabet=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]            
#   textCode=[]
#   for i in text.lower() :
#     if i.isalpha():
#        textCode.append(str((alphabet.index(i)+1)))
#   return ' '.join(str(e) for e in textCode)     
#
##text="The sunset sets at twelve o' clock."
##alphabet=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]            
##textCode=[]
##for i in text.lower() :
##  if i.isalpha():
##     textCode.append(str((alphabet.index(i)+1)))
##print(" ".join(str(e) for e in textCode)) 
#print(alphabet_position("The sunset sets at twelve o' clock."))
#
#
#
#a="iwae"


#more simpeler
def alphabet_position(text):
    return ' '.join(str(ord(c) - 96) for c in text.lower() if c.isalpha())

#text="o  k"
#alphabet=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]            
#textCode=[]
#for i in text :
#   if i.isalpha():
#      textCode.append(str((alphabet.index(i)+1)))
      

#print(' '.join(str(e) for e in textCode))

#print(alphabet.index("t")+1)



