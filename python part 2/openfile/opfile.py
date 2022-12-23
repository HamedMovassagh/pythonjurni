try:
    with open('D:\\python part 2\\openfile\\text.tx') as file:
      print(file.read())
except FileNotFoundError :
    print("i could not find that file ")      