import numpy as np
from PIL import Image
from scipy.signal import convolve2d

def apply_blur_filter(image_path, filter_size):
    # Charger l'image
    image = Image.open(image_path)

    # Convertir l'image en niveaux de gris
    image_gray = image.convert("L")

    # Convertir l'image en tableau numpy
    image_array = np.array(image_gray)

    # Définir le masque de flou
    blur_filter = np.ones((filter_size, filter_size)) / (filter_size ** 2)

    # Appliquer le filtre de flou avec convolve2d
    blurred_image = convolve2d(image_array, blur_filter, mode="same", boundary="symm")

    # Convertir le tableau numpy en image PIL
    blurred_image_pil = Image.fromarray(blurred_image.astype(np.uint8))

    return blurred_image_pil

# Appliquer un filtre de flou linéaire avec un masque de 3x3
blurred_image_3x3 = apply_blur_filter("images/Lenna512.jpg", 3)
blurred_image_3x3.show()

# Appliquer un filtre de flou linéaire avec un masque de 10x10
blurred_image_10x10 = apply_blur_filter("images/Lenna512.jpg", 10)
blurred_image_10x10.show()
