import random

def generate_random_matrix(rows, cols):
    matrix = [[random.randint(1, 10) for _ in range(cols)] for _ in range(rows)]
    return matrix

def sum_rows_method1(matrix):
    row_sums = []
    for row in matrix:
        row_sum = 0
        for element in row:
            row_sum += element
        row_sums.append(row_sum)
    return row_sums

def sum_rows_method2(matrix):
    row_sums = [sum(row) for row in matrix]
    return row_sums

def display_row_sums(row_sums):
    for i, row_sum in enumerate(row_sums):
        print(f"Somme de la ligne {i+1} :", row_sum)

def main():
    rows = int(input("Entrez le nombre de lignes de la matrice aléatoire : "))
    cols = int(input("Entrez le nombre de colonnes de la matrice aléatoire : "))

    random_matrix = generate_random_matrix(rows, cols)
    print("\nMatrice aléatoire :")
    for row in random_matrix:
        print(row)

    row_sums1 = sum_rows_method1(random_matrix)
    row_sums2 = sum_rows_method2(random_matrix)

    print("\nSomme des lignes (méthode 1) :")
    display_row_sums(row_sums1)

    print("\nSomme des lignes (méthode 2) :")
    display_row_sums(row_sums2)

if __name__ == "__main__":
    main()