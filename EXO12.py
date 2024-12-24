largeur = int(input("Largeur = "))
hauteur = int(input("Hauteur = "))

i = 0
while i < hauteur:
    j = 0
    while j < largeur:
        print("#", end="")  
        j += 1
    print()  
    i += 1
