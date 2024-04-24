import numpy as np
from PIL import Image

def apply_directional_blur(image, masque):
    """Applique un filtre de flou directionnel à une image."""
    # Convertir l'image en tableau numpy
    image_array = np.array(image)

    # Taille de l'image et du masque
    hauteur, largeur = image_array.shape[:2]  # Handles images with or without channels
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

    # Clipping the result to avoid overflow
    resultat = np.clip(resultat, 0, 255)

    # Ensure the type is uint8
    resultat = resultat.astype(np.uint8)

    return Image.fromarray(resultat)

# Load an image and convert to grayscale
image_path = "images\\Lenna512.jpg"  # Adjust the path to your image
image = Image.open(image_path).convert("L")  # Convert to grayscale

# Define the mask for left-to-right directional blur
masque_directionnel_gauche_droite = [
    [0, 0, 0],
    [1, 1, 1],
    [0, 0, 0]
]

# Apply the directional blur filter
directional_blur_image = apply_directional_blur(image, masque_directionnel_gauche_droite)

# Display the resulting image
directional_blur_image.show()
