def main():
    # Définition des matrices A et B comme des listes de listes
    A = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    B = [[9, 9, 9], [9, 9, 9], [9, 9, 9]]

    # Affichage des matrices A et B
    print("Matrice A :")
    for row in A:
        print(row)

    print("\nMatrice B :")
    for row in B:
        print(row)

    # Addition des matrices A et B (addition élément par élément)
    C_elementwise = [[A[i][j] + B[i][j] for j in range(len(A[0]))] for i in range(len(A))]
    print("\nAddition élément par élément (A + B) :")
    for row in C_elementwise:
        print(row)

    # Addition des matrices A et B selon les règles du calcul matriciel
    C_matrixwise = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    for i in range(len(A)):
        for j in range(len(A[0])):
            C_matrixwise[i][j] = A[i][j] + B[i][j]
    print("\nAddition selon les règles du calcul matriciel (A + B) :")
    for row in C_matrixwise:
        print(row)

if __name__ == "__main__":
    main()
