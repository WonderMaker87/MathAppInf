def input_matrix(rows, cols):
    matrix = []
    for i in range(rows):
        row = []
        for j in range(cols):
            value = float(input(f"Entrez la valeur de la matrice à la position [{i+1}][{j+1}] : "))
            row.append(value)
        matrix.append(row)
    return matrix

def hadamard_product(matrix1, matrix2):
    if len(matrix1) != len(matrix2) or len(matrix1[0]) != len(matrix2[0]):
        return None  # Les matrices n'ont pas la même taille, l'opération n'est pas possible
    
    result = [[matrix1[i][j] * matrix2[i][j] for j in range(len(matrix1[0]))] for i in range(len(matrix1))]
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

    product = hadamard_product(matrix1, matrix2)

    if product:
        print("\nProduit de Hadamard des deux matrices :")
        display_matrix(product)
    else:
        print("\nLes matrices n'ont pas la même taille, le produit de Hadamard n'est pas possible.")

if __name__ == "__main__":
    main()