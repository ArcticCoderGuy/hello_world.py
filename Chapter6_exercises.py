# Here are all the Chapter6 tasks and things



# alien.py task 1

alien_0 = {'color' : 'green' , 'points': 5}

print(alien_0['color'])
print(alien_0['points'])


#My own example on key-values in multiple things

cabin_in_yllas = {'made out of': 'wood', 'Log-type': 'Spruce', 'Location': '342.344.321.112', 'Is in AirBbN': 'Yes' }
print(cabin_in_yllas['made out of'])
print(cabin_in_yllas['Log-type'])
print(cabin_in_yllas['Location'])
print(cabin_in_yllas['Is in AirBbN'])

# The book showed an example where it had just an empty dictionary

cabin_in_yllas = {}

cabin_in_yllas['Is in the parrish of Kittilä'] = 'We are in Kittilä parrish' 
cabin_in_yllas['Has how many kilometers of ski-tracks'] = '432km'

print(cabin_in_yllas)



# Now we make a larger task that is applied to the same manner as in the book, in page 95

# on the book it is coded like this: 

alien_0 = {'x_position' : 0, 'y_position' : 25, 'speed' : 'high' }  
print(f"Original position: {alien_0['x_position']}")

if alien_0['speed'] == 'slow':
    x_increment = 1

elif alien_0['speed'] == 'medium':
    x_increment = 2
    
else:
    # You are out of luck Bro and your ass is toasted !!
    x_increment = 14

#The new position is the old position plus the increment.

alien_0['x_position'] = alien_0['x_position'] + x_increment

print(f"New Position on the alien is: {alien_0['x_position']}")



 # made a task 6-1 on the page 98 to see how I would do this
 
The_wife = {'first_name': 'Heidi', 'Surname':'Kaprio', 'Age': 25, 'domecile': 'Tornio' }
 
print(The_wife['first_name'])
print(The_wife['Surname'])
print(The_wife['Age'])
print(The_wife['domecile'])
 
 
 
 # Loopin on page 99 - 101, user.py
 
user_0 = {
        'username': 'efermi',
        'first name': 'Enrico',
        'surname': 'Fermi'
        }


for key, value in user_0.items():
        print(f"\nkey: {key}")
        print(f"Value: {value}")




#  Page 101 task 

favourite_languages = {
    'Jen': 'Python',
    'John': 'Rust',
    'Edward': 'HTML',
    'Phil': 'Javascript'
            
}

for name, language in favourite_languages.items():
    print(f"{name.title()}´s favourite language is {language.title()}.")
    
    
# Page 101 Task 

favourite_languages = {
    'Jen': 'Python',
    'John': 'Rust',
    'Edward': 'HTML',
    'Phil': 'Javascript'
            
}

for name in favourite_languages.keys():
    print(name.title())
    
# For me to remember: Dict = key -> value, items) antaa (key, value) pareina
    
for pair in favourite_languages.items():
    print("DEBUG:", pair, type(pair))


# Page 103 sorted()-method

favourite_languages = {
    'Jen': 'Python',
    'John': 'Rust',
    'Edward': 'HTML',
    'Phil': 'Javascript'
            
}

for name in sorted (favourite_languages.keys()):
    print(f"{name.title()}, Thank you for taking hte poll.")



# Page 103 Continued values()-method


favourite_languages = {
    'Jen': 'Python',
    'John': 'Rust',
    'Edward': 'HTML',
    'Phil': 'Javascript'
            
}

print("the following languages have been mentioned:")
for language in favourite_languages.values(): 
    print(language.title())
    
    

# PAge 105 tasks 6-5 & 6-6 

world_rivers = { 
    'Amazon': 'Brazil',
    'Tornion joki' : 'Lappi',
    'Donau': 'Hungary'
}

for river, country in world_rivers.items():
    print(f"\n The {river} is running through {country}.")
    
    
    
    
print("\n\tRivers:")
for river in world_rivers.keys():
    print(river)


    
print("\n\tCountries/regions:")
for country in world_rivers.values():
    print(country)
    
favourite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python'
}

people = ['jen', 'markus', 'phil', 'anna', 'edward']

for name in people:
    if name in favourite_languages:
        print(f"{name.title()}, thanks for responding!")
    else:
        print(f"{name.title()}, please take the poll!")
    