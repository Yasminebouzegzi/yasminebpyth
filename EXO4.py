
age1 = int(input("Veuillez entrer l'âge de la première personne : "))
age2 = int(input("Veuillez entrer l'âge de la deuxième personne : "))
if age1 > age2:
    print("L'âge le plus grand est :", age1)
elif age2 > age1:
    print("L'âge le plus grand est :", age2)
else:
    print("Les deux personnes ont le même âge !")
