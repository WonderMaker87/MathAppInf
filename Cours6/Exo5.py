import numpy as np
from PIL import Image
from scipy.ndimage import gaussian_filter

def apply_gaussian_blur(image_path, sigma):
    # Charger l'image
    image = Image.open(image_path)

    # Convertir l'image en niveaux de gris
    image_gray = image.convert("L")

    # Convertir l'image en tableau numpy
    image_array = np.array(image_gray)

    # Appliquer le filtre de flou gaussien avec gaussian_filter
    blurred_image = gaussian_filter(image_array, sigma=sigma)

    # Convertir le tableau numpy en image PIL
    blurred_image_pil = Image.fromarray(blurred_image.astype(np.uint8))

    return blurred_image_pil

# Appliquer un filtre de flou gaussien avec un sigma de 2
blurred_image_sigma_2 = apply_gaussian_blur("images/Lenna512.jpg", 2)
blurred_image_sigma_2.show()

# Appliquer un filtre de flou gaussien avec un sigma de 5
blurred_image_sigma_5 = apply_gaussian_blur("images/Lenna512.jpg", 5)
blurred_image_sigma_5.show()
