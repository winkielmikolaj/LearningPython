
groceryList = {}
x = 0
try:
	while True:
		x += 1
		item = input().upper()
		groceryList[item] = x
		continue
	print(groceryList)
except EOFError:
	for item, count in groceryList.items():
		print(f"{count}. {item}")