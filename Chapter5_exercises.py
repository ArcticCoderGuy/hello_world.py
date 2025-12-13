
# Here are the relevant list method examples from Chapter 5 exercises 

# My introduction to if-statements:

cars = ["F1 Mclaren", "Ferrari", "Red Bull", "Mercedes", "Alpine"]

for variable in cars:    
      if variable == "Alpine":
          print(variable.upper())
      else:
          print(variable.title())
          
# Example with if-else 


#Applied page 74 example toppings.py and the != ineqaulity operator 


we_want = 'Linux'

we_do_not_want = 'Windows Vista'
    
if we_want != we_do_not_want:
    print(f"Hold the {we_do_not_want.upper()} !! ")
    
    
    
# Paga 74 magic_number.py x 2 tasks

answer = 17
if answer != 42:
    print(f" If the {answer} is your age, Register to vote next year")
    
answer = 21
if answer != 31:
    print(f" On if you are {answer} old, that is the only age you get the Rhum-Cola in this bar")
    
    
markuksen_kotikaupunki = "Matinkylä"

if markuksen_kotikaupunki == "Matinkylä":
    print(f"Siellä oli kiva asua lapsena, koska {markuksen_kotikaupunki.upper()} oli lapsiperheille kiva paikka asua 1980-luvulla")
         
         
         
    
 # Page 76 and applied banned_users.py 
 
  
banned_users = ['andrew','caroline','Gerenimo']
user = 'marie'

if user not in banned_users:
    print(f"{user.title()}, you can post on Twitter if you wish")

        
       
        
# Task 5-1 conditional tests, page 77 

car = 'subaru'
print("Is car == 'Subaru' ? I predict True.")
print(car == 'subaru')

print ("\nIs car == 'audi' ? I predict False.")
print("car == audi")

# Task 5-1: Conditional tests – at least 10 tests
# We want at least 5 tests == True and at least 5 == False


#10 tests and at least 5 tests == True and at least 5 == False

car = 'subaru'
os = 'linux'
age = 21

print("Test 1: Is car == 'subaru'? I predict True.")
print(car == 'subaru')   # True

print("\nTest 2: Is car == 'audi'? I predict False.")
print(car == 'audi')     # False

print("\nTest 3: Is car != 'bmw'? I predict True.")
print(car != 'bmw')      # True

print("\nTest 4: Is car == 'Subaru'? (case-sensitive) I predict False.")
print(car == 'Subaru')   # False

print("\nTest 5: Is car.lower() == 'subaru'? I predict True.")
print(car.lower() == 'subaru')   # True

print("\nTest 6: Is age == 21? I predict True.")
print(age == 21)         # True

print("\nTest 7: Is age < 18? I predict False.")
print(age < 18)          # False

print("\nTest 8: Is age >= 18? I predict True.")
print(age >= 18)         # True

print("\nTest 9: Is os == 'Windows'? I predict False.")
print(os == 'Windows')   # False

print("\nTest 10: Is os != 'linux'? I predict False.")
print(os != 'linux')     # False


# 5-2 More Conditional tests on page 78 and at least one True/False on every category

car = 'audi'
os = 'linux'
age = 21
height_cm = 185
allowed_oses = ['linux', 'macOS', 'FreeBSD']

# 1) Equality ja inequality merkkijonoilla
print("== ja != stringeillä")
print("car == 'audi'? ->", car == 'audi')      # True
print("car != 'bmw'?  ->", car != 'bmw')       # True
print("car == 'Audi'? ->", car == 'Audi')      # False (case-sensitive)

# 2) lower() metodin käyttö
print("\nlower() tests")
print("car.lower() == 'audi'? ->", car.lower() == 'audi')   # True
print("car.lower() == 'AUDI'? ->", car.lower() == 'AUDI')   # False

# 3) Numeeriset testit: ==, !=, >, <, >=, <=
print("\nNumeric tests")
print("age == 21?   ->", age == 21)            # True
print("age != 30?   ->", age != 30)            # True
print("age > 18?    ->", age > 18)             # True
print("age < 18?    ->", age < 18)             # False
print("height >= 180? ->", height_cm >= 180)   # True
print("height <= 180? ->", height_cm <= 180)   # False

# 4) and / or
print("\nLogical and / or")
print("age > 18 AND height > 180? ->", age > 18 and height_cm > 180)   # True
print("age < 18 AND height > 180? ->", age < 18 and height_cm > 180)   # False
print("age > 18 OR height < 150?  ->", age > 18 or height_cm < 150)    # True
print("age < 18 OR height < 150?  ->", age < 18 or height_cm < 150)    # False

# 5) Onko alkio listassa (in)
print("\nMembership: in")
print("'linux' in allowed_oses?   ->", 'linux' in allowed_oses)    # True
print("'windows' in allowed_oses? ->", 'windows' in allowed_oses)  # False

# 6) Ei ole listassa (not in)
print("\nMembership: not in")
print("'windows' not in allowed_oses? ->", 'windows' not in allowed_oses)  # True
print("'linux' not in allowed_oses?   ->", 'linux' not in allowed_oses)    # False


# Page 78 and voting.py 

age = 19 
if age == 18:
    print("You are old enough to vote")

# The if-elif-else chain page 80 -> amusement park example 

age = 32

if age < 4:
    print("Your admission cost is of 0 EUR.")

elif age < 18:
    print("Your admission cost is 25 EUR")

else:
   print("your admission is 250 EUR, because we can !")

        


 