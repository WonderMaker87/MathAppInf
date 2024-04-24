import numpy as np

def main():
    # Définition des matrices A et B en utilisant NumPy arrays
    A = np.array([[4.1, 2.0, 0], [4.6, 1, 6], [2, 8, 3]])
    B = np.array([[1, 1, 0], [1.0, 1, 1], [2, 2, 2]])

    # Affichage des arrays A et B
    print("Array A :\n", A)
    print("\nArray B :\n", B)

    # Addition des arrays A et B
    C = A + B
    print("\nAddition des arrays (A + B) :\n", C)

if __name__ == "__main__":
    main()
