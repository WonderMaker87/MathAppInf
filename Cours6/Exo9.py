import numpy as np
from PIL import Image

def apply_gradient_filter(image):
    """Applique un filtre de détection de contour basé sur le gradient à une image."""
    # Convertir l'image en niveaux de gris en tableau numpy
    image_array = np.array(image.convert("L"))

    # Calculer les gradients horizontaux et verticaux avec le gradient de Sobel
    gradient_x = np.abs(np.gradient(image_array, axis=1))  # Gradient horizontal
    gradient_y = np.abs(np.gradient(image_array, axis=0))  # Gradient vertical

    # Combinaison des gradients horizontaux et verticaux pour obtenir le gradient total
    gradient_total = np.sqrt(gradient_x**2 + gradient_y**2)

    # Normalisation des valeurs du gradient total entre 0 et 255
    gradient_total = (gradient_total / np.max(gradient_total)) * 255

    # Création de l'image résultat à partir du gradient total
    resultat = Image.fromarray(gradient_total.astype(np.uint8))

    return resultat

# Charger une image
image = Image.open("images/Lenna512.jpg")

# Appliquer le filtre de détection de contour basé sur le gradient
contour_image = apply_gradient_filter(image)

# Afficher l'image résultat
contour_image.show()
