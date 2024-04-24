import random

def generate_random_square_matrix(size):
    matrix = [[random.randint(1, 10) for _ in range(size)] for _ in range(size)]
    return matrix

def matrix_multiply(matrix1, matrix2):
    size = len(matrix1)
    result = [[0] * size for _ in range(size)]
    for i in range(size):
        for j in range(size):
            for k in range(size):
                result[i][j] += matrix1[i][k] * matrix2[k][j]
    return result

def matrix_power(matrix, n):
    size = len(matrix)
    if n == 0:
        return [[int(i == j) for j in range(size)] for i in range(size)]  # Matrice identité
    if n == 1:
        return matrix
    if n % 2 == 0:
        half_power = matrix_power(matrix, n // 2)
        return matrix_multiply(half_power, half_power)
    else:
        return matrix_multiply(matrix, matrix_power(matrix, n - 1))

def display_matrix(matrix):
    for row in matrix:
        print(row)

def main():
    size = int(input("Entrez la taille de la matrice carrée aléatoire : "))
    n = int(input("Entrez la puissance à laquelle élever la matrice : "))

    random_matrix = generate_random_square_matrix(size)
    print("\nMatrice aléatoire :")
    display_matrix(random_matrix)

    result_matrix = matrix_power(random_matrix, n)
    print(f"\nMatrice à la puissance {n} :")
    display_matrix(result_matrix)

if __name__ == "__main__":
    main()