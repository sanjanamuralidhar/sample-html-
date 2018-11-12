num=int(input("enter a year"))
print(num)
if (num%4==0):
    if(num%100==0):
        if(num%400==0):
            print("year is a leap year")
        else:
            print("year is not a leap year")
    else:
        print(num," is a leap year")
else:
    print(num,"is not a leap year")
