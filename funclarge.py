def large(a,b,c):
    if(a>b):
        if(a>c):
            return a 
        else:
            return b 
    else:
        if(b>c):
            return b 
        else:
            return c 
x = int(input("enter num1"))
y = int(input("enter num2"))
z = int(input("enter num3"))
result=large(x,y,z)
print(result)