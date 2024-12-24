# Demande le nom de l'utilisateur
name = input("Veuillez entrer votre nom : ")
     # Vérifie si l'utilisateur est un VIP
if name == "VIP":
        print("Profitez du spectacle gratuitement !")
else:
        # Demande le nombre de billets à acheter
        tickets = int(input("Combien de billets souhaitez-vous acheter ? "))
        # Calcul du coût total
        total_cost = tickets * 15.50
        # Affiche le résultat
        print("Le coût total est de ",total_cost)
        print("Profitez de vos billets !")