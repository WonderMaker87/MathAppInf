from PIL import Image
import numpy as np

def convert_to_grayscale(image):
    # Convertir l'image en tableau numpy
    pixel_array = np.array(image)

    # Extraire les composantes rouge, vert et bleu
    rouge = pixel_array[:,:,0]
    vert = pixel_array[:,:,1]
    bleu = pixel_array[:,:,2]

    # Calculer la luminance pour chaque pixel
    luminance = 0.2126 * rouge + 0.7152 * vert + 0.0722 * bleu

    # Normaliser la luminance pour obtenir des valeurs entre 0 et 255
    luminance_normalisee = (luminance / luminance.max()) * 255

    # Créer un tableau avec les valeurs de luminance pour chaque composante
    image_grayscale = np.stack((luminance_normalisee, luminance_normalisee, luminance_normalisee), axis=-1)

    # Créer une nouvelle image à partir du tableau numpy en nuances de gris
    image_grayscale = Image.fromarray(image_grayscale.astype('uint8'))

    return image_grayscale

def main():
    # Ouvrir l'image Lenna
    image = Image.open("images\\Lenna512.png")

    # Convertir l'image en nuances de gris
    image_grayscale = convert_to_grayscale(image)
    image_grayscale.show()

if __name__ == "__main__":
    main()
