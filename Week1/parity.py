def main():
    x = int(input("Whats X?"))
    if is_even(x):
        print("Your number is Even")
    else:
        print("Your number is Odd")

def is_even(number):
    return True if number % 2 == 0 else False
main()