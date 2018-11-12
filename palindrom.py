a = int(input("enter a number  "))
n = m
while(a!=0):
    r = a%10
    n = (n*10)+r
    a = int(a/10)
if(m==n):
    print("palindrom")
    else:
    print("not")
    
    
print(n)