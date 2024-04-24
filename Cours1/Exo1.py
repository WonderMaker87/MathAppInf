import random

def generate_integer_matrix(rows, cols):
    matrix = [[random.randint(0, 100) for _ in range(cols)] for _ in range(rows)]
    return matrix

def generate_float_matrix(rows, cols):
    matrix = [[random.uniform(0, 100) for _ in range(cols)] for _ in range(rows)]
    return matrix

def display_matrix(matrix):
    for row in matrix:
        print(row)

def main():
    rows = int(input("Entrez le nombre de lignes de la matrice : "))
    cols = int(input("Entrez le nombre de colonnes de la matrice : "))
    
    integer_matrix = generate_integer_matrix(rows, cols)
    float_matrix = generate_float_matrix(rows, cols)
    
    print("\nMatrice d'entiers :")
    display_matrix(integer_matrix)
    
    print("\nMatrice de réels :")
    display_matrix(float_matrix)

if __name__ == "__main__":
    main()
