import numpy as np

def input_matrix(n):
    """ Demande à l'utilisateur d'entrer les coefficients pour chaque équation. """
    matrix = []
    for i in range(n):
        row = list(map(float, input(f"Entrez les coefficients et le terme constant pour l'équation {i+1} (séparés par des espaces): ").split()))
        if len(row) != n + 1:
            raise ValueError("Nombre incorrect de coefficients et de terme constant.")
        matrix.append(row)
    return np.array(matrix, dtype=float)

def gauss_jordan(matrix):
    """ Applique l'élimination de Gauss-Jordan pour trouver la solution du système. """
    n = len(matrix)
    for i in range(n):
        # Trouver le pivot maximal dans la colonne i dans les lignes i ou après
        max_row = max(range(i, n), key=lambda r: abs(matrix[r, i]))
        if abs(matrix[max_row, i]) < 1e-10:
            continue  # Cette colonne est zéro, passer à la prochaine

        # Échanger la ligne actuelle avec la ligne du pivot maximal
        matrix[[i, max_row]] = matrix[[max_row, i]]

        # Normaliser la ligne pivot
        matrix[i] = matrix[i] / matrix[i, i]

        # Éliminer toutes les autres entrées dans cette colonne
        for j in range(n):
            if i != j:
                matrix[j] = matrix[j] - matrix[j, i] * matrix[i]

    return matrix[:, -1]

def main():
    while True:
        try:
            n = int(input("Combien y a-t-il de variables (et donc d'équations) ? "))
            break
        except ValueError:
            print("Veuillez entrer un nombre valide.")

    matrix = input_matrix(n)
    try:
        result = gauss_jordan(matrix)
        if any(np.isnan(result)):
            print("Le système n'a pas de solution unique.")
        else:
            print("La solution du système est:")
            for i, res in enumerate(result):
                print(f"x{i+1} = {res}")
    except Exception as e:
        print(str(e))

if __name__ == "__main__":
    main()
