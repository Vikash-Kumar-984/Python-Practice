comment=input("Please enter the comment ")
print("The comment is: ",comment)
if(comment.__contains__("make a lot of money" or "buy now" or "subscribe this" or "Click this")):
    print("This is the spam comment")
else:
    print("The comment is good")