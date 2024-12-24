# Demande le montant total de l'achat
total_amount = float(input("Montant total : "))

# Demande le nombre d'articles
num_items = int(input("Nombre d'articles : "))

# Demande le jour de la semaine
day_of_week = input("Jour de la semaine : ").lower()

# Applique une réduction en fonction du jour
if day_of_week in ["monday", "tuesday", "wednesday", "thursday", "friday"]:
    discount = 0.10  # 10% de réduction
elif day_of_week in ["saturday", "sunday"]:
    discount = 0.20  # 20% de réduction
else:
    print("Jour invalide.")
    discount = 0

# Applique une réduction supplémentaire si plus de 5 articles
if num_items > 5:
    discount += 0.05  # 5% de réduction supplémentaire

# Calcule le prix après réduction
final_price = total_amount * (1 - discount)

# Affiche le prix final
print("Prix total après réduction : ", round(final_price, 2), "dinars")
