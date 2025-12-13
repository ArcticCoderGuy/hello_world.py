
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