from PIL import Image
import numpy as np

def resize_image(image, new_width, new_height):
    # Dimensions de l'image d'entrée
    width, height = image.size

    # Calculer les ratios de redimensionnement
    ratio_width = width / new_width
    ratio_height = height / new_height

    # Créer une nouvelle image de la taille spécifiée
    resized_image = Image.new("RGB", (new_width, new_height))

    # Convertir l'image en tableau numpy
    pixel_array = np.array(image)

    # Parcourir chaque pixel de la nouvelle image
    for y in range(new_height):
        for x in range(new_width):
            # Trouver les coordonnées correspondantes dans l'image d'origine
            orig_x = int(x * ratio_width)
            orig_y = int(y * ratio_height)

            # Remplir le pixel de la nouvelle image avec la couleur du pixel correspondant dans l'image d'origine
            resized_image.putpixel((x, y), tuple(pixel_array[orig_y, orig_x]))

    return resized_image

def main():
    # Charger l'image d'origine
    original_image = Image.open("images\\Lenna512.png")

    # Redimensionner l'image
    resized_image = resize_image(original_image, 50, 50)

    # Afficher l'image redimensionnée
    resized_image.show()

if __name__ == "__main__":
    main()
