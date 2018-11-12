def reverse(a):
    rev=0
    
    while(a!=0):
        r=a%10
        rev=(rev*10)+r
        a=a//10
    return rev
a=int(input("enter a number"))        
result=reverse(a)
print(result)