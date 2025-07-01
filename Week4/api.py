import requests

def main():
	print("Search the Museum")
	artist = input("Artist: ")

	n = 0
	try:
		response = requests.get(
			"https://api.artic.edu/api/v1/artworks/search",
			{"q": artist}
		)
		response.raise_for_status()
	except requests.HTTPError:
		print("Couldn't complete request")
		return

	content = response.json()
	for artwork in content["data"]:
		n += 1
		print(f"{n} {artwork['title']}")

main()