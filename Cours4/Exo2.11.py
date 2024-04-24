from PIL import Image
import numpy as np

def adjust_contrast(image):
    # Convertir l'image en tableau numpy
    pixel_array = np.array(image)

    # Calculer les intensités pour chaque pixel
    intensities = np.mean(pixel_array, axis=2)

    # Trouver les valeurs minimales et maximales des intensités
    i_min = np.min(intensities)
    i_max = np.max(intensities)

    # Normaliser les intensités entre 0 et 255 de manière linéaire
    normalized_intensities = 255 * (intensities - i_min) / (i_max - i_min)

    # Appliquer la nouvelle intensité à chaque canal de couleur
    adjusted_pixel_array = np.zeros_like(pixel_array)
    for i in range(3):
        adjusted_pixel_array[:,:,i] = np.clip(pixel_array[:,:,i] * (normalized_intensities / 255), 0, 255)

    # Créer une nouvelle image à partir du tableau numpy modifié
    result_image = Image.fromarray(adjusted_pixel_array.astype(np.uint8))

    return result_image

def main():
    # Charger l'image
    image = Image.open("images\\Lenna512.png")

    # Ajuster le contraste de l'image
    result_image = adjust_contrast(image)
    result_image.show()

if __name__ == "__main__":
    main()