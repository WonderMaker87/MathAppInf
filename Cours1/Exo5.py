import random

def generate_random_matrix(rows, cols):
    matrix = [[random.randint(0, 10) for _ in range(cols)] for _ in range(rows)]
    return matrix

def scalar_multiply(matrix, scalar):
    result = [[element * scalar for element in row] for row in matrix]
    return result

def display_matrix(matrix):
    for row in matrix:
        print(row)

def main():
    rows = int(input("Entrez le nombre de lignes de la matrice : "))
    cols = int(input("Entrez le nombre de colonnes de la matrice : "))

    random_matrix = generate_random_matrix(rows, cols)
    scalar = float(input("Entrez le scalaire pour la multiplication : "))

    print("\nMatrice de départ :")
    display_matrix(random_matrix)

    print("\nScalaire :", scalar)

    product = scalar_multiply(random_matrix, scalar)

    print("\nProduit de la matrice par le scalaire :")
    display_matrix(product)

if __name__ == "__main__":
    main()