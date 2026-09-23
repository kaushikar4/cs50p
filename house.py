name = input("what's your name? ")

match name:
    case "Harry" | "Hermione" | "Ron":
        print("gryffindor")
    case "Draco":
        print("slytherine")
    case _:
        print("who? ")