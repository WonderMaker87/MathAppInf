def echanger_lignes(matrice, i, j):
    """Échange les lignes i et j dans la matrice."""
    matrice[i], matrice[j] = matrice[j], matrice[i]

# Exemple d'utilisation
A = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print("Avant l'échange :")
for ligne in A:
    print(ligne)

# Échanger les lignes 0 et 2
echanger_lignes(A, 0, 2)

print("\nAprès l'échange :")
for ligne in A:
    print(ligne)
