from PIL import Image
import numpy as np

def green_screen(image_fg, image_bg):
    # Convertir les images en tableaux numpy
    pixel_array_fg = np.array(image_fg)
    pixel_array_bg = np.array(image_bg)

    # Créer un masque pour les pixels verts, en utilisant un seuil pour prendre en compte différentes nuances de vert
    green_threshold = 200 # Cette valeur peut être ajustée en fonction de l'image spécifique
    green_mask = (pixel_array_fg[:, :, 1] > green_threshold) & (pixel_array_fg[:, :, 0] < green_threshold) & (pixel_array_fg[:, :, 2] < green_threshold)

    # Appliquer le masque pour remplacer les pixels verts par les pixels de l'image de fond
    pixel_array_fg[green_mask] = pixel_array_bg[green_mask]

    # Créer une nouvelle image à partir du tableau numpy modifié
    result_image = Image.fromarray(pixel_array_fg)

    return result_image

def main():
    # Charger les images avant-plan et arrière-plan
    image_fg = Image.open("images\\Lenna512v.png")
    image_bg = Image.open("images\\4-2-03.png")

    # Appliquer la technique de fond vert
    result_image = green_screen(image_fg, image_bg)
    result_image.show()

if __name__ == "__main__":
    main()
