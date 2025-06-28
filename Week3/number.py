def main():
    x = get_int("What is x")
    print(f"x is {x}")

def get_int(prompt):
    while True:
        try:
            x = int(input(prompt))
        except ValueError:
            print("X is not an integer!!! Try again")
        else:
            return x


main()