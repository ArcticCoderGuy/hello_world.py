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
 
 







