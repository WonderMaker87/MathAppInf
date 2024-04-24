import numpy as np
from PIL import Image

def apply_median_filter(image, taille_fenetre):
    """Applique un filtre médian à une image."""
    # Convertir l'image en tableau numpy
    image_array = np.array(image)

    # Taille de l'image
    hauteur, largeur = image_array.shape

    # Initialisation du tableau résultat
    resultat = np.zeros_like(image_array)

    # Appliquer le filtre médian sur chaque pixel de l'image
    for y in range(hauteur):
        for x in range(largeur):
            # Calculer les limites de la fenêtre autour du pixel courant
            y_min = max(0, y - taille_fenetre // 2)
            y_max = min(hauteur, y + taille_fenetre // 2 + 1)
            x_min = max(0, x - taille_fenetre // 2)
            x_max = min(largeur, x + taille_fenetre // 2 + 1)

            # Extraire les valeurs des pixels dans la fenêtre
            valeurs_pixels = image_array[y_min:y_max, x_min:x_max].flatten()

            # Calculer la médiane des valeurs des pixels
            valeur_mediane = np.median(valeurs_pixels)

            # Assigner la médiane comme valeur du pixel courant dans le résultat
            resultat[y, x] = valeur_mediane

    return Image.fromarray(resultat)

# Charger une image
image = Image.open("images/Lenna512.jpg").convert("L")  # Convertir en niveaux de gris

# Appliquer le filtre médian avec une fenêtre de taille 3x3
median_filtered_image = apply_median_filter(image, taille_fenetre=3)

# Afficher l'image résultat
median_filtered_image.show()
