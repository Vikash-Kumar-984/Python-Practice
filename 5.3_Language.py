Lang= {}

a=input("Enter your favorite language Vikash \n")
b=input("Enter your favorite language Ashish \n")
c=input("Enter your favorite language Roshan \n")

Lang['Vikash']=a
Lang['Ashish']=b
Lang['Roshan']=c

print(Lang)

# Keys should be unique but not neccessay for values.
# Set cannot contain List in it as list is mutable but set is immutable.
# Set can contain tuple as both is immutable.