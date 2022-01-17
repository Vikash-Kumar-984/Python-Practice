a=int(input("Enter the number:"))
prime=True

for l in range(2,a):
    if(a%l==0):
        prime=False
        break
if (prime==True):
    print(a," is a prime number")
else:
    print(a, "is not a prime number")