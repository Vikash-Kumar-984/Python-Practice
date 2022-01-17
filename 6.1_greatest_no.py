a=int(input("Enter the first number \n"))
b=int(input("Enter the second number \n"))
c=int(input("Enter the third number \n"))
d=int(input("Enter the fourth number \n"))

if(a>b):
    if(a>c):
        if(a>d):
            print("a is greater number")
        else:
            print("d is greater number")
    elif(c>d):
        print("c is greater number")
    else:
        print("d is greater number")
elif(b>c):
    if(b>d):        
       print("b is greater number")
    else:
        print("d is greater number")
else:
    print("C is greater number")