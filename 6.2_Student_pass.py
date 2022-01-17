a=int(input("Enter the maths marks: "))
b=int(input("Enter the physics marks: "))
c=int(input("Enter the chemistry marks: "))

# print("The value of a is: ",a)
sum=a+b+c
# print("The sum is: ",sum)
total_perctg=(sum/300)*100
# print("The total percentage is: ",total_perctg)

if(total_perctg>40 and a>33 and b>33 and c>33):
    print("Student has passed the exam with ",total_perctg, "percentage")
else:
    print("Student didn't passed the exam")