
cities = []

while True:
    city = input("Enter a city name (or type 'stop' to finish): ")
    if city.lower() == "stop":
        break
    population = len(city.replace(" ", "")) * 1000000  # sans compter les espaces
    cities.append((city, population))  # Ajouter la ville et sa population à la liste


def get_second_value(x):
    return x[1]

cities.sort(key=get_second_value, reverse=True)
print("\nCities and their populations:")
for city, population in cities:
    print(city,":", population,"citizens")  
