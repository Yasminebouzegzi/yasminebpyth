
numbers = [1, 2, 3, 4, 5]
while True:
  
    index = int(input("Entrez l'index (-1 pour quitter) : "))
    if index == -1:
        break
    new_value = int(input("Entrez la nouvelle valeur : "))
    
    numbers[index] = new_value
    
   
    print(numbers)
