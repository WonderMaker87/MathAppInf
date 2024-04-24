import numpy as np

# Création de la matrice A et du vecteur B
A = np.array([
    [1, 2, 1, 0, 0],
    [2, 1, 1, 1, 0],
    [1, 0, 2, 2, 1],
    [2, 2, 1, 1, 3],
    [1, 0, 0, 2, 2]
])

B = np.array([55, 65.5, 80, 117.5, 63.5])

# Utiliser numpy pour résoudre le système d'équations linéaires
prices = np.linalg.solve(A, B)

# Afficher les prix des pizzas
pizza_types = ['Margherita', 'Quatre-saisons', 'Végétarienne', 'Hawaïenne', 'Napolitaine']
for pizza, price in zip(pizza_types, prices):
    print(f"Le prix de la pizza {pizza} est de {price:.1f} €")
