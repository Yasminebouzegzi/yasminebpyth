
price = float(input("Please type in a price: "))
dinars = int(price)
centimes = int(round((price - dinars) * 100))#Convertit le résultat arrondi en un entier, car les centimes doivent être un nombre entier
print("Dinars: ",dinars)
print("Centimes: ",centimes)
