import random

def generate_random_matrix(rows, cols):
    matrix = [[random.randint(-10, 10) for _ in range(cols)] for _ in range(rows)]
    return matrix

def calculate_opposite_matrix(matrix):
    opposite_matrix = [[-element for element in row] for row in matrix]
    return opposite_matrix

def add_matrices(matrix1, matrix2):
    if len(matrix1) != len(matrix2) or len(matrix1[0]) != len(matrix2[0]):
        return None  # Les matrices n'ont pas la même taille, l'opération n'est pas possible
    
    result = []
    for i in range(len(matrix1)):
        row = []
        for j in range(len(matrix1[0])):
            row.append(matrix1[i][j] + matrix2[i][j])
        result.append(row)
    return result

def display_matrix(matrix):
    for row in matrix:
        print(row)

def main():
    rows = int(input("Entrez le nombre de lignes de la matrice : "))
    cols = int(input("Entrez le nombre de colonnes de la matrice : "))

    random_matrix = generate_random_matrix(rows, cols)
    opposite_matrix = calculate_opposite_matrix(random_matrix)

    print("\nMatrice aléatoire :")
    display_matrix(random_matrix)

    print("\nMatrice opposée :")
    display_matrix(opposite_matrix)

    print("\nSomme des deux matrices :")
    sum_matrix = add_matrices(random_matrix, opposite_matrix)
    display_matrix(sum_matrix)

    # Vérification que la somme est une matrice nulle
    is_zero_matrix = all(all(element == 0 for element in row) for row in sum_matrix)
    if is_zero_matrix:
        print("\nLa somme des deux matrices est une matrice nulle.")
    else:
        print("\nLa somme des deux matrices n'est pas une matrice nulle.")

if __name__ == "__main__":
    main()