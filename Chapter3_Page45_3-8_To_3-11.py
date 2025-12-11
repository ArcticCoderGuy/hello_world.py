# Here you can find the assigments from Exercises 3-8 through 3-11.

#Example code to just try out 

bicycles = ['car', 'building', 'boat', 'this stuff is just too easy...']
print(bicycles)


#From pages 22,34-35 Just for fun stuff


gifts = ["Playstation 2", "Trip to Hawai", "Lobster dinner", "New Laptop", "New iPhone 10"]

message = f"My Nr.1 wish is to get a {gifts[-1].title()}"
print(message)

print(f"\ngifts[-1] is the last item in the list:\n\t{gifts[-1]}")




#Extended version of the above code

gifts = ["Playstation 2", "Trip to Hawai", "Lobster dinner", "New Laptop", "New Phone"]

message = f"\nMy Nr.1 wish is to get a {gifts[-1].title()}."
print(message)

print("\nMy full wishlist:")
print(f"\t1. {gifts[0]}")
print(f"\t2. {gifts[1]}")
print(f"\t3. {gifts[2]}")
print(f"\t4. {gifts[3]}")
print(f"\t5. {gifts[4]}")

# Question for the teacher from Markus: What is the best "Python-way" to indent multiple lines like above ? 1 space under each line or what ? I want to become a devs-guy that does the most Robust code possible.



# Just wanted to experiment with list methods a bit more, as a function

def build_wishlist_messages (gifts: list[str]) ->  tuple[str, str]:
    
    """ Builds two messages of wishlists 
    - main message 
    - explanatory message Gifts[-1]-index
    - Also learn the difference where one uses Print as a script or as a function return value. """

    main_message = f"\nMy Nr.1 wish is to get a {gifts[-1].title()}."
    info_message = f"\nGifts[-1] is the last item in the list:\n\t{gifts[-1]}"
    return main_message, info_message

gifts = ["Playstation 2", "Trip to Hawai", "Lobster dinner", "New Laptop", "New iPhone10"]

message, debug_info = build_wishlist_messages(gifts)

print(message)
print(debug_info)




#Page 37-40 short example of list modification with .append()-command + some print formatting and a for-loop + .pop()-command.

Great_Buildings = []

Great_Buildings.append('Burj Khalifa')
Great_Buildings.append('Shanghai Tower')
Great_Buildings.append('Raadenhammas in Espoo')

print(f"\t- \nThe list of Great Buildings:")

print(f"\t ")

for building in Great_Buildings:
    print(f"\t {building}")
    

first_visited = Great_Buildings.pop(2)   
print(f"\t \n- The first building I visited was {first_visited.title()} when I was 8 years old.")   

    
 #Assignment  3-8 
 
   # 3-8: Seeing the World

places = [
    "Tokyo",
    "Ylläs",
    "Dubai",
    "New York",
    "Reykjavik",
]

#  
print("Original list:")
print(places)

#
print("\nSorted (alphabetical, does NOT change the original):")
print(sorted(places))


print("\nStill original list:")
print(places)


print("\nSorted (reverse alphabetical, does NOT change the original):")
print(sorted(places, reverse=True))

print("\nStill original list again:")
print(places)


places.reverse()
print("\nAfter reverse():")
print(places)


places.reverse()
print("\nAfter reverse() again (back to original order):")
print(places)


places.sort()
print("\nAfter sort() (alphabetical, CHANGES the list):")
print(places)


places.sort(reverse=True)
print("\nAfter sort(reverse=True) (reverse alphabetical, CHANGES the list):")
print(places)

    
    
    # 3-9: Dinner Guests
    
    

guests = ["Albert Einstein", "Nikola Tesla", "Marie Curie", "Ada Lovelace"]

print("Guest list:")
for guest in guests:
    print(f"\t- {guest}")


print(f"\nI am inviting {len(guests)} people to dinner.")




# 3-10: Every Function


languages = ["Python", "Rust", "C", "JavaScript"]

print("Alkuperäinen lista:")
print(languages)


print("\nappend(): lisätään Go listan loppuun")
languages.append("Go")
print(languages)

#
print("\ninsert(): lisätään TypeScript indeksin 1 kohdalle")
languages.insert(1, "TypeScript")
print(languages)


print("\ndel: poistetaan indeksin 2 alkio pysyvästi")
del languages[2]
print(languages)


print("\npop(): poistetaan ja talletetaan listan viimeinen alkio")
popped_language = languages.pop()
print(f"Poistettu kieli: {popped_language}")
print("Lista nyt:")
print(languages)


print("\nremove(): poistetaan 'TypeScript' nimen perusteella")
languages.remove("TypeScript")
print(languages)


print("\nsorted(): väliaikainen lajittelu aakkosjärjestykseen")
print(sorted(languages))
print("Alkuperäinen lista ei muuttunut:")
print(languages)


print("\nsorted(..., reverse=True): väliaikainen lajittelu käänteiseen aakkosjärjestykseen")
print(sorted(languages, reverse=True))
print("Alkuperäinen lista edelleen samassa järjestyksessä:")
print(languages)


print("\nsort(): pysyvä lajittelu aakkosjärjestykseen")
languages.sort()
print(languages)


print("\nsort(reverse=True): pysyvä lajittelu käänteiseen aakkosjärjestykseen")
languages.sort(reverse=True)
print(languages)


print("\nreverse(): käännetään nykyinen järjestys ympäri")
languages.reverse()
print(languages)


print(f"\nLopuksi listassa on {len(languages)} ohjelmointikieltä.")


# 3-11: Intentional Errors

