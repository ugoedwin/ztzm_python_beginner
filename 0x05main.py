visited_cities = {"New York", "London", "Tokyo", "Paris", "Sydney"}
visited_cities.add("Tokyo")
visited_cities.add("Berlin")
visited_cities.discard("Sydney")

print("Cities visited:")
for city in visited_cities:
    print(city)

if "Paris" in visited_cities:
    print("\nYou've been to Paris!")
else:
    print("\nYou haven't been to Paris yet.")