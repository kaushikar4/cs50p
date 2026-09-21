# ask user for their name and strip space and capitalize
name = input("what's your name? ").strip().title()

#split user's name into first, middle, and last name
first, middle, last = name.split(" ")

#say hello to user
print(f"hello,{first} {middle} {last}")

