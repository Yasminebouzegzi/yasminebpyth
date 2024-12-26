word = input("Veuillez entrer un mot : ")
i = len(word)
total_width = 30
vide = (total_width - i) // 2


frame_line = '*' * total_width
middle_line = '*' + ' ' * vide + word + ' ' * (total_width - i - vide - 2) + '*'

# Affichage du cadre
print(frame_line)
print(middle_line)
print(frame_line)
