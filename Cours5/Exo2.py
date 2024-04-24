import numpy as np

def transvection(matrice, k, i, alpha):
    """Soustrait d'une ligne k un multiple d'une autre ligne i de la matrice."""
    matrice[k] -= alpha * matrice[i]

# Exemple d'utilisation
A = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

print("Avant la transvection :")
print(A)

# Soustraire 2 fois la première ligne de la troisième ligne
transvection(A, 2, 0, 2)

print("\nAprès la transvection :")
print(A)
