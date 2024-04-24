def main():
    # Définition de la matrice M comme une liste de listes
    M = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

    # Affichage de la matrice
    print("Matrice M :")
    for row in M:
        print(row)

    # Affichage de l'élément m23
    m23 = M[1][2]
    print("\nÉlément m23 :", m23)

    # Affichage de la 3ème ligne
    row3 = M[2]
    print("\n3ème ligne de la matrice :", row3)

    # Affichage de la première colonne
    first_column = [row[0] for row in M]
    print("\nPremière colonne de la matrice :", first_column)

if __name__ == "__main__":
    main()
