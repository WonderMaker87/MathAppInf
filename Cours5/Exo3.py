import numpy as np

def transvection(matrice, k, i, alpha):
    """Soustrait d'une ligne k un multiple d'une autre ligne i de la matrice."""
    matrice[k] -= alpha * matrice[i]

def pivot_gauss_jordan(matrice):
    """Calcule le déterminant d'une matrice par la méthode du pivot de Gauss-Jordan."""
    n = len(matrice)
    det = 1

    for i in range(n):
        # Chercher le pivot
        pivot = i
        for j in range(i + 1, n):
            if abs(matrice[j, i]) > abs(matrice[pivot, i]):
                pivot = j

        # Échanger les lignes si nécessaire
        if pivot != i:
            matrice[[i, pivot]] = matrice[[pivot, i]]
            det *= -1

        # Élimination de Gauss
        for j in range(i + 1, n):
            alpha = matrice[j, i] / matrice[i, i]
            transvection(matrice, j, i, alpha)

    # Calcul du déterminant
    for i in range(n):
        det *= matrice[i, i]

    return det

# Exemple d'utilisation
A = np.array([
    [2, 5, 8],
    [3, 6, 7],
    [4, 9, 1]
], dtype=np.float64)  # Setting the dtype to float64

determinant = pivot_gauss_jordan(A)
print("Le déterminant de la matrice est :", determinant)