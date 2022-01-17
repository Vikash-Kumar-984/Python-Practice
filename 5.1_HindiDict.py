Dict={
    "Hindi": "English",
    "Chai": "Tea",
    "Pani": "Water"
}
print("The available words in Dictionary are ", Dict.keys())
a=input('Enter the word in hindi \n')
print("The meaning of the required word is :",Dict.get(a))  #It will not throw an error.