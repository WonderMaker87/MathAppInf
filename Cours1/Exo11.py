import random

def generate_random_matrix(rows, cols):
    matrix = [[random.randint(1, 10) for _ in range(cols)] for _ in range(rows)]
    return matrix

def transpose_matrix(matrix):
    transposed_matrix = [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]
    return transposed_matrix

def display_matrix(matrix):
    for row in matrix:
        print(row)

def main():
    rows = int(input("Entrez le nombre de lignes de la matrice aléatoire : "))
    cols = int(input("Entrez le nombre de colonnes de la matrice aléatoire : "))

    random_matrix = generate_random_matrix(rows, cols)
    print("\nMatrice aléatoire :")
    display_matrix(random_matrix)

    transposed_matrix = transpose_matrix(random_matrix)
    print("\nTransposée de la matrice :")
    display_matrix(transposed_matrix)

if __name__ == "__main__":
    main()
