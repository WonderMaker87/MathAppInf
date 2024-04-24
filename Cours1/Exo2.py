import random

def generate_identity_matrix(size):
    matrix = [[0] * size for _ in range(size)]
    for i in range(size):
        matrix[i][i] = 1
    return matrix

def generate_diagonal_matrix(size):
    matrix = [[0] * size for _ in range(size)]
    for i in range(size):
        matrix[i][i] = i + 1  # Valeurs diagonales
    return matrix

def generate_upper_triangular_matrix(size):
    matrix = [[0 if j > i else i + 1 for j in range(size)] for i in range(size)]
    return matrix

def generate_sparse_matrix(size):
    matrix = [[0] * size for _ in range(size)]
    # Remplir quelques éléments avec des valeurs aléatoires
    for i in range(size):
        for j in range(size):
            if i == j:
                continue
            if random.random() < 0.2:  # Probabilité de remplissage
                matrix[i][j] = random.randint(1, 10)
    return matrix

def generate_zero_matrix(size):
    matrix = [[0] * size for _ in range(size)]
    return matrix

def display_matrix(matrix):
    for row in matrix:
        print(row)

def main():
    size = int(input("Entrez la taille de la matrice : "))
    
    identity_matrix = generate_identity_matrix(size)
    diagonal_matrix = generate_diagonal_matrix(size)
    upper_triangular_matrix = generate_upper_triangular_matrix(size)
    sparse_matrix = generate_sparse_matrix(size)
    zero_matrix = generate_zero_matrix(size)
    
    print("\nMatrice unité :")
    display_matrix(identity_matrix)
    
    print("\nMatrice diagonale :")
    display_matrix(diagonal_matrix)
    
    print("\nMatrice triangulaire supérieure :")
    display_matrix(upper_triangular_matrix)
    
    print("\nMatrice creuse :")
    display_matrix(sparse_matrix)
    
    print("\nMatrice nulle :")
    display_matrix(zero_matrix)

if __name__ == "__main__":
    main()