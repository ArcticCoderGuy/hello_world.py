# Here you can find the assigments from Exercises 3-8 through 3-11.

#Example code to just try out 

bicycles = ['car', 'building', 'boat', 'this stuff is just too easy...']
print(bicycles)


#From pages 22,34- 35 Just for fun stuff


gifts = ["Playstation 2", "Trip to Hawai", "Lobster dinner", "New Laptop", "New iPhone 10"]

message = f"My Nr.1 wish is to get a {gifts[-1].title()}"
print(message)

print(f"Gifts[-1] is the last item in the list:\n\t{gifts[-1]}")




#Extended version of the above code

gifts = ["Playstation 2", "Trip to Hawai", "Lobster dinner", "New Laptop", "New Phone"]

message = f"My Nr1 wish is to get a {gifts[-1].title()}."
print(message)

print("\nMy full wishlist:")
print(f"\t1. {gifts[0]}")
print(f"\t2. {gifts[1]}")
print(f"\t3. {gifts[2]}")
print(f"\t4. {gifts[3]}")
print(f"\t5. {gifts[4]}")

# Question for the teacher from Markus: What is the best "Python-way" to indent multiple lines like above? 1 space under each line ?



