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

def subtract_matrices(matrix1, matrix2):
    if len(matrix1) != len(matrix2) or len(matrix1[0]) != len(matrix2[0]):
        return None  # Les matrices n'ont pas la même taille, l'opération n'est pas possible
    
    result = []
    for i in range(len(matrix1)):
        row = []
        for j in range(len(matrix1[0])):
            row.append(matrix1[i][j] - matrix2[i][j])
        result.append(row)
    return result

def input_matrix(rows, cols):
    matrix = []
    for i in range(rows):
        row = []
        for j in range(cols):
            value = float(input(f"Entrez la valeur de la matrice à la position [{i+1}][{j+1}] : "))
            row.append(value)
        matrix.append(row)
    return matrix

def display_matrix(matrix):
    for row in matrix:
        print(row)

def main():
    rows = int(input("Entrez le nombre de lignes des matrices : "))
    cols = int(input("Entrez le nombre de colonnes des matrices : "))

    print("Entrez la première matrice :")
    matrix1 = input_matrix(rows, cols)

    print("Entrez la deuxième matrice :")
    matrix2 = input_matrix(rows, cols)

    print("\nMatrice 1 :")
    display_matrix(matrix1)
    print("\nMatrice 2 :")
    display_matrix(matrix2)

    sum_result = add_matrices(matrix1, matrix2)
    if sum_result:
        print("\nRésultat de l'addition :")
        display_matrix(sum_result)
    else:
        print("\nLes matrices n'ont pas la même taille, l'addition n'est pas possible.")

    diff_result = subtract_matrices(matrix1, matrix2)
    if diff_result:
        print("\nRésultat de la soustraction :")
        display_matrix(diff_result)
    else:
        print("\nLes matrices n'ont pas la même taille, la soustraction n'est pas possible.")

if __name__ == "__main__":
    main()