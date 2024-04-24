def input_matrix(rows, cols):
    matrix = []
    for i in range(rows):
        row = []
        for j in range(cols):
            value = float(input(f"Entrez la valeur de la matrice à la position [{i+1}][{j+1}] : "))
            row.append(value)
        matrix.append(row)
    return matrix

def multiply_matrices(matrix1, matrix2):
    if len(matrix1[0]) != len(matrix2):
        return None  # Les matrices ne sont pas compatibles pour la multiplication
    
    result = []
    for i in range(len(matrix1)):
        row = []
        for j in range(len(matrix2[0])):
            element = sum(matrix1[i][k] * matrix2[k][j] for k in range(len(matrix1[0])))
            row.append(element)
        result.append(row)
    return result

def display_matrix(matrix):
    for row in matrix:
        print(row)

def main():
    rows1 = int(input("Entrez le nombre de lignes de la première matrice : "))
    cols1 = int(input("Entrez le nombre de colonnes de la première matrice : "))

    print("Entrez les éléments de la première matrice :")
    matrix1 = input_matrix(rows1, cols1)

    rows2 = int(input("Entrez le nombre de lignes de la deuxième matrice : "))
    cols2 = int(input("Entrez le nombre de colonnes de la deuxième matrice : "))

    print("Entrez les éléments de la deuxième matrice :")
    matrix2 = input_matrix(rows2, cols2)

    print("\nMatrice de départ 1 :")
    display_matrix(matrix1)

    print("\nMatrice de départ 2 :")
    display_matrix(matrix2)

    product = multiply_matrices(matrix1, matrix2)

    if product:
        print("\nProduit des deux matrices :")
        display_matrix(product)
    else:
        print("\nLes matrices ne sont pas compatibles pour la multiplication.")

if __name__ == "__main__":
    main()