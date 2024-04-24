import numpy as np

def main():
    # Création et affichage de la matrice M
    M = np.array([[4.1, 2.0, 0], [4.6, 1, 6], [2, 8, 3]])
    print("Matrice M :\n", M)

    # Affichage de l'élément m23
    m23 = M[1, 2]
    print("\nÉlément m23 de la matrice M :", m23)

    # Affichage de la 3ème ligne de la matrice M
    row3 = M[2, :]
    print("\n3ème ligne de la matrice M :", row3)

    # Affichage de la première colonne de la matrice M
    col1 = M[:, 0]
    print("\nPremière colonne de la matrice M :", col1)

    # Création et affichage d'une matrice 3x3 de type entier contenant que des 1
    ones_matrix = np.ones((3, 3), dtype=int)
    print("\nMatrice 3x3 de type entier contenant que des 1 :\n", ones_matrix)

    # Création et affichage d'une matrice unité diagonale 5x5 de type float
    identity_matrix = np.eye(5, dtype=float)
    print("\nMatrice unité diagonale 5x5 de type float :\n", identity_matrix)

    # Réarrangement et affichage de la liste linéaire en matrice 3x2
    A = np.array([2, 4, 6, 12, 24, 36])
    A_reshaped = A.reshape(3, 2)
    print("\nMatrice 3x2 à partir de la liste linéaire A :\n", A_reshaped)

if __name__ == "__main__":
    main()
