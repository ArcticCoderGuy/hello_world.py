# Here are all the programs from Exercises 2-3 through 2-8.

# 2-3: personal_message.py

name = "Eric"
message = f"Hello {name}, would you like to learn some Python today?"

print(message)



# 2-4: name_cases.py

name = "ada lovelace"

print(name.lower())   
print(name.upper())   
print(name.title())   


# 2-5: famous_quote.py

author = "Albert Einstein"
quote = "Anyone who has never made a mistake has never tried anything new."

print(f'{author} once said, "{quote}"')


# 2-6: famous_quote_2.py

famous_person = "Albert Einstein"
quote = "Anyone who has never made a mistake has never tried anything new."

message = f'{famous_person} once said, "{quote}"'

print(message)



# 2-7: stripping_names.py

name = "\t  \n  Markus Kaprio  \t\n" # /t/n from pag page 22

print("Raw name:")
print(name)


print("\nLeft stripped:")
print(name.lstrip())


print("\nRight stripped:")
print(name.rstrip())

print("\nFully stripped:")
print(name.strip())


# 2-8: file_extensions.py

filename = "python_notes.txt"

clean_name = filename.removesuffix(".txt")

print(clean_name)
