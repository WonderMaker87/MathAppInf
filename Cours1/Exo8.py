import random

def generate_random_matrix(rows, cols):
    matrix = [[random.randint(1, 10) for _ in range(cols)] for _ in range(rows)]
    return matrix

def sum_columns_method1(matrix):
    col_sums = []
    for j in range(len(matrix[0])):
        col_sum = 0
        for i in range(len(matrix)):
            col_sum += matrix[i][j]
        col_sums.append(col_sum)
    return col_sums

def sum_columns_method2(matrix):
    col_sums = [sum(matrix[i][j] for i in range(len(matrix))) for j in range(len(matrix[0]))]
    return col_sums

def display_col_sums(col_sums):
    for i, col_sum in enumerate(col_sums):
        print(f"Somme de la colonne {i+1} :", col_sum)

def main():
    rows = int(input("Entrez le nombre de lignes de la matrice aléatoire : "))
    cols = int(input("Entrez le nombre de colonnes de la matrice aléatoire : "))

    random_matrix = generate_random_matrix(rows, cols)
    print("\nMatrice aléatoire :")
    for row in random_matrix:
        print(row)

    col_sums1 = sum_columns_method1(random_matrix)
    col_sums2 = sum_columns_method2(random_matrix)

    print("\nSomme des colonnes (méthode 1) :")
    display_col_sums(col_sums1)

    print("\nSomme des colonnes (méthode 2) :")
    display_col_sums(col_sums2)

if __name__ == "__main__":
    main()
