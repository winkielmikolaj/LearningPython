greeting = input().title()

print(f"Greeting: {greeting}")

if  greeting.__contains__("Hello"):
    print("$0")
elif greeting.startswith("H"):
    print("$20")
else:
    print("$100")