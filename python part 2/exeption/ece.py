#exception = event deceted during execution that intrrupt the flow of  a program
try:
    m=float(input("take a number"))
    n=float(input("take another number"))
    result=m/n
except ZeroDivisionError as e:
    print(e)
    print("you can dvide somthing by zero")    
except ValueError as e:
    print(e)
    print("you can use letter lady")
except Exception as e:
    print(e)
    print("somthing went")
else:
    print(result)
finally:
    print("this will happend no mather what")    