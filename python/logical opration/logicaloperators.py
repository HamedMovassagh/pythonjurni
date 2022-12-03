temp =int(input("what is the temperature outside: "))

if not(temp >= 0 and temp <= 30) :
    print("the temp is bad today ! ")
    print("stay inside !")
if not(temp < 0 or temp > 30):
   print("the temperature is good today! ")
   print("go outside! ")
