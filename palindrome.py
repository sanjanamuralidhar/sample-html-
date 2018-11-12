num = int(input("enter a number  "))
n=num
rev=0
digit=0
while(num!=0):
    digit = num%10
    rev = (rev*10)+digit
    num = int(num/10)
    
print(rev)
if(n==rev):
    print(" palindrom")
else:
    print("not palindrome")