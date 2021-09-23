# this is an object, key value pairs
myLaptop = {
    "name": "Macbook Pro", 
    "size": "large", 
    "color": "space grey", 
    "brandNew": True, 
    "productive year": 2019
}


myMajor = {
    "name": "Interation Design", 
    "School": "SVA", 
    "Location": "NYC", 
    "graduate": True,
    "academic-year": "2023"
}

myApartment = {
    "name": "Journal Square", 
    "Location": "Jersey City", 
    "Roomnumber": 5206, 
    "studio": False,
    "list-of-features": ["1", "2", "3"] 
}



# let the user know what's going on
print ("Welcome to MadLibs!")
print ("Answer the questions below to play.")
print ("-----------------------------------")

# variables containing all of your story info
year = input("Enter a year: ")
name1 = input("What is your name?: ")
length = input("Enter a length: ")
color = input("What is your favourite color?: ")
animal = input("what is your favourite animal?: ")
flavor = input("A flavor that you don't like?: ")
food = input("What's your favourite food?: ")
adjective = input("Enter a lovely adjective: ")
body = input("Enter a body part that comes fist in your mind: ")
word = input("Enter a sentence you would say to your loved one: ")

# this is the story. it is made up of strings and variables.
# the \ at the end of each line let's the computer know our string is a long one
# (a whole paragraph!) and we want to continue more code on the next line. 
# play close attention to the syntax!

story = "In the morning of " + year + ", "  + name1 + " wakes up on his/her " + length + " Simmons. " \
"There are " + color + " clouds floating in the air. " + name1 + "'s " + "AI " +animal + " robot comes to his/her bed," \
" bringing a bowl of " + flavor + " " + food +  ". However, after " + name1 + " earting the " + food + ", " + name1 + " gets diarrheal!" \
" It seems to make sense that the AI " + animal + " messed about with the " + food + ". " \
"When " + name1 + " gets angry and decides to blame the " + animal + ", he/she looks into the " + adjective + " eyes of the " + animal + "." \
" He/She becomes softhearted and tap the " + animal  + "'s " + body + " and says " + "'" + word + "'."

# finally we print the story
print (story)