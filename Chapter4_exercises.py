
# Here you can find all the exercisese in Chapter 4

# The Magician.py-task on page 50

magicians = ["Peter", "Steve", "Colin"]
for magician in magicians:
    print(f"{magician.title()}, that was an awesome trick you did !")
    
    
    #Page 52
    magicians = ["Peter", "Steve", "Colin"]
for magician in magicians:
    print(f"{magician.title()}, that was an awesome trick you did !")
    print(f"I can't wait to see your next trick, {magician.title()}.\n")    
    
    
print("Thank you, everyone. That was such a great magic show!") # And I did indet this line to be outside the for-loop, as instructuion says.


# Page 56 - 4-1: Pizzas

pizzas = ['Margherita', 'Pepperoni', 'Hawaiian']        
for pizza in pizzas:
    
    print(f"I like {pizza} pizza.")
    
 
print("\nI really love all of these pizzas!")  # Indented outside the for-loop.



#Page 56 - 4-2: Animals

animals = ['dog', 'cat', 'rabbit']
for animal in animals:
    print(f"A {animal} would make a great pet.")        

print("\nAny of these animals would make a great pet!")  # Indented outside the for-loop.

#Page 57 - first numbers.py example

for value in range(1, 6):
    print(value)
    
# Page 58 - second numbers.py example using range() to make a list

numbers = list(range(1, 6))
print(numbers)


# Page 58 - third numbers.py example using range() with different step values       
even_numbers = list(range(2, 11, 2))
print(even_numbers)


# Page 59 - fourth numbers.py example - squares of numbers
squares = []
for value in range(1, 11):
    square = value ** 2
    squares.append(square)   
    
# Page 58 - squares - more concise version

squares = []
for value in range(1, 11):
    square = value ** 3
    squares.append(square)      
    
print(squares)       

#Assingment 4-3: print numbers 1-20
for number in range(1, 21):
    print(number)           
        
# Assingment 4-4: One million and NOTIFY 
# that I have commented the print(number)-line below to avoid flooding the output. Hope that's ok


numbers = list(range(1, 1000001))

for number in numbers:
    #git add .print(number)
    
    


 
