name = input("Whats your name?").capitalize()

match name:
    case "Harry" | "Hermione":
        print("Gryffindor")
    #case "Hermione":
        #print("Gryffindor")
    case "Draco":
        print("Slytherin")
    case _:
        print("Who?")