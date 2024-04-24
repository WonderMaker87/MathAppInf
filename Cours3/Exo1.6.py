import numpy as np

def main():
    # Demande à l'utilisateur d'entrer les dimensions des matrices A et B
    rows_A = int(input("Entrez le nombre de lignes de la matrice A : "))
    cols_A = int(input("Entrez le nombre de colonnes de la matrice A : "))
    rows_B = int(input("Entrez le nombre de lignes de la matrice B : "))
    cols_B = int(input("Entrez le nombre de colonnes de la matrice B : "))

    # Demande à l'utilisateur d'entrer les éléments des matrices A et B
    print("\nEntrez les éléments de la matrice A :")
    A = np.array([[float(input(f"Element [{i+1}][{j+1}] de A : ")) for j in range(cols_A)] for i in range(rows_A)])
    print("\nEntrez les éléments de la matrice B :")
    B = np.array([[float(input(f"Element [{i+1}][{j+1}] de B : ")) for j in range(cols_B)] for i in range(rows_B)])

    # Calcul et affichage du produit matriciel de A par B
    try:
        product_AB = np.dot(A, B)
        print("\nProduit matriciel de A par B :\n", product_AB)
    except ValueError as e:
        print("\nImpossible de calculer le produit matriciel de A par B :", e)

    # Calcul et affichage du produit matriciel de B par A
    try:
        product_BA = np.dot(B, A)
        print("\nProduit matriciel de B par A :\n", product_BA)
    except ValueError as e:
        print("\nImpossible de calculer le produit matriciel de B par A :", e)

    # Calcul et affichage de la somme de A+B
    try:
        sum_AB = A + B
        print("\nSomme de A et B :\n", sum_AB)
    except ValueError as e:
        print("\nImpossible de calculer la somme de A et B :", e)

    # Calcul et affichage de la transposée de A
    A_transpose = np.transpose(A)
    print("\nTransposée de A :\n", A_transpose)
    print("Nombre de lignes de la transposée de A :", A_transpose.shape[0])
    print("Nombre de colonnes de la transposée de A :", A_transpose.shape[1])

if __name__ == "__main__":
    main()
