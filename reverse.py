a = int(input("enter a number  "))
n = 0
while(a!=0):
    r = a%10
    n = (n*10)+r
    a = int(a/10)
    
print(n)