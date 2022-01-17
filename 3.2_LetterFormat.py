name=input("Enter your name: ")
date=input("Enter Date: ")
letter=''' Dear <|Name>,
 You are selected!

 Date: <|Date>
'''
letter=letter.replace("<|Name>", name)
letter=letter.replace("<|Date>", date)

print(letter)

# if(letter.find('dear')):
#     print("the letter is found")