
        # Le nombre de personnes
total_people = int(input("Combien de personnes ont besoin d'un transport ? "))
        
        # La capacité d'un taxi
taxi_capacity = int(input("Combien de personnes peuvent tenir dans un taxi ? "))
        
if total_people <= 0 or taxi_capacity <= 0:
  print("Les deux nombres doivent être supérieurs à 0.")
else:
        
        # Calculer le nombre de taxis requis
 taxis_needed = total_people // taxi_capacity
 if total_people % taxi_capacity != 0:
            taxis_needed += 1
        
        # Résultat
 print("Nombre de taxis nécessaires : %d" % taxis_needed)
