from PIL import Image
import numpy as np

def image_negatif(image):
    # Convertir l'image en tableau numpy
    pixel_array = np.array(image)

    # Calculer le négatif de chaque canal de couleur (rouge, vert, bleu)
    negatif_array = 255 - pixel_array

    # Créer une nouvelle image à partir du tableau numpy en négatif
    image_negatif = Image.fromarray(negatif_array.astype('uint8'))

    return image_negatif

def main():
    # Ouvrir l'image Lenna512
    image = Image.open("images\\Lenna512.png")

    # Créer une image en négatif
    image_negatif_result = image_negatif(image)

    # Afficher l'image en négatif
    image_negatif_result.show()

if __name__ == "__main__":
    main()
