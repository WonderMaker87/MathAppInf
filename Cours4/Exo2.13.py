from PIL import Image
import numpy as np

def smooth_image(image):
    # Convertir l'image en tableau numpy
    pixel_array = np.array(image)

    # Dimensions de l'image
    height, width = pixel_array.shape[:2]

    # Créer une nouvelle image de la même taille que l'originale
    smoothed_image = Image.new("RGB", (width, height))

    # Parcourir chaque pixel de l'image
    for y in range(height):
        for x in range(width):
            # Calculer la moyenne des valeurs des pixels environnants (noyau 3x3)
            avg_red = np.mean(pixel_array[max(0, y-1):min(height, y+2), max(0, x-1):min(width, x+2), 0])
            avg_green = np.mean(pixel_array[max(0, y-1):min(height, y+2), max(0, x-1):min(width, x+2), 1])
            avg_blue = np.mean(pixel_array[max(0, y-1):min(height, y+2), max(0, x-1):min(width, x+2), 2])

            # Assigner la moyenne calculée au pixel correspondant dans l'image lissée
            smoothed_image.putpixel((x, y), (int(avg_red), int(avg_green), int(avg_blue)))

    return smoothed_image

def main():
    # Charger l'image d'origine
    original_image = Image.open("images\\Lenna512.png")

    # Lissage de l'image
    smoothed_image = smooth_image(original_image)

    # Afficher l'image lissée
    smoothed_image.show()

if __name__ == "__main__":
    main()
