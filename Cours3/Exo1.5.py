import numpy as np

def main():
    # Définition des arrays A, B et C en utilisant NumPy
    A = np.array([[4.1, 2.0, 0], [4.6, 1, 6], [2, 8, 3]])
    B = np.array([[1, 1, 0], [1.0, 1, 1], [2, 2, 2]])
    C = np.array([[1, 2], [0, 1], [3, 1]])

    # Affichage des arrays A, B et C
    print("Array A :\n", A)
    print("\nArray B :\n", B)
    print("\nArray C :\n", C)

    # Calcul du produit d'Hadamard entre A et B
    hadamard_product = A * B
    print("\nProduit d'Hadamard entre A et B :\n", hadamard_product)

    # Calcul du produit matriciel entre A et B
    matrix_product = np.dot(A, B)
    print("\nProduit matriciel entre A et B :\n", matrix_product)

    # Calcul du produit matriciel de A par C
    try:
        product_AC = np.dot(A, C)
        print("\nProduit matriciel entre A et C :\n", product_AC)
    except ValueError as e:
        print("\nImpossible de calculer le produit matriciel entre A et C :", e)

    # Calcul du produit matriciel de C par A
    try:
        product_CA = np.dot(C, A)
        print("\nProduit matriciel entre C et A :\n", product_CA)
    except ValueError as e:
        print("\nImpossible de calculer le produit matriciel entre C et A :", e)

if __name__ == "__main__":
    main()