import numpy as np
from PIL import Image

def convolution(image, masque):
    """Effectue la convolution entre une image et un masque."""
    # Convertir l'image en tableau numpy
    image_array = np.array(image)

    # Taille de l'image et du masque
    hauteur, largeur = image_array.shape
    taille_masque = len(masque)

    # Calcul de la marge pour le masque
    marge = taille_masque // 2

    # Initialisation du tableau résultat
    resultat = np.zeros_like(image_array)

    # Appliquer le masque sur chaque pixel de l'image
    for y in range(marge, hauteur - marge):
        for x in range(marge, largeur - marge):
            somme = 0
            for i in range(taille_masque):
                for j in range(taille_masque):
                    somme += image_array[y + i - marge, x + j - marge] * masque[i][j]
            resultat[y, x] = somme

    return Image.fromarray(resultat)

# Test de la fonction
if __name__ == "__main__":
    # Charger une image
    image = Image.open("images\\Lenna512.jpg").convert("L")  # Convertir en niveaux de gris

    # Définir un masque (filtre)
    masque = [
        [-1, -1, -1],
        [-1,  8, -1],
        [-1, -1, -1]
    ]

    # Appliquer la convolution
    image_conv = convolution(image, masque)

    # Afficher l'image résultat
    image_conv.show()
