from PIL import Image
import numpy as np

def blend_images(image1, image2, proportion):
    # Convertir les images en tableaux numpy
    pixel_array1 = np.array(image1)
    pixel_array2 = np.array(image2)

    # Mélanger les deux images en utilisant la proportion donnée
    blended_pixel_array = (proportion * pixel_array1 + (1 - proportion) * pixel_array2).astype(np.uint8)

    # Créer une nouvelle image à partir du tableau numpy mélangé
    blended_image = Image.fromarray(blended_pixel_array)

    return blended_image

def main():
    # Charger les deux images
    image1 = Image.open("images\\Lenna512.png")
    image2 = Image.open("images\\4-2-03.png")

    # Définir la proportion de mélange (60% de la première image, 40% de la seconde)
    proportion = 0.6

    # Mélanger les deux images
    blended_image = blend_images(image1, image2, proportion)
    blended_image.show()

if __name__ == "__main__":
    main()
