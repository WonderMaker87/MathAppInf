import numpy as np

def transvection(matrice, k, i, alpha):
    """Soustrait d'une ligne k un multiple d'une autre ligne i de la matrice."""
    matrice[k] -= alpha * matrice[i]

def pivot_gauss_jordan(matrice):
    """Inverse une matrice par la méthode du pivot de Gauss-Jordan."""
    n, m = matrice.shape
    inverse = np.identity(n)

    r = 0  # Indice de ligne du dernier pivot trouvé

    for j in range(m):
        # Recherche du pivot maximal dans la colonne j
        k = np.argmax(np.abs(matrice[r:, j])) + r

        # Échange des lignes si nécessaire
        if matrice[k, j] != 0:
            if k != r:
                matrice[[r, k]] = matrice[[k, r]]
                inverse[[r, k]] = inverse[[k, r]]

            # Normalisation de la ligne du pivot
            alpha = matrice[r, j]
            matrice[r] /= alpha
            inverse[r] /= alpha

            # Elimination de Gauss-Jordan
            for i in range(n):
                if i != r:
                    alpha = matrice[i, j]
                    transvection(matrice, i, r, alpha)
                    transvection(inverse, i, r, alpha)

            r += 1

    return inverse

# Exemple d'utilisation
A = np.array([
    [2, 5, 8],
    [3, 6, 7],
    [4, 9, 1]
], dtype=np.float64)  # Setting the dtype to float64

inverse_A = pivot_gauss_jordan(A)
print("La matrice inversée est :\n", inverse_A)