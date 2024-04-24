import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

def intensity_profile(image, start_point, end_point):
    # Convertir l'image en niveau de gris
    grayscale_image = image.convert("L")

    # Convertir l'image en tableau numpy
    pixel_array = np.array(grayscale_image)

    # Extraire les coordonnées x et y des points de départ et d'arrivée
    x1, y1 = start_point
    x2, y2 = end_point

    # Calculer les coordonnées des pixels le long de la ligne
    x_values = np.linspace(x1, x2, abs(x2 - x1))
    y_values = np.linspace(y1, y2, abs(y2 - y1))

    # Interpoler les valeurs des pixels le long de la ligne
    interpolated_values = pixel_array[np.round(y_values).astype(int), np.round(x_values).astype(int)]

    return interpolated_values

def main():
    # Charger l'image
    image_path = "images\\Lenna512.png"
    image = Image.open(image_path)

    # Définir les points de départ et d'arrivée de la ligne
    start_point = (100, 100)
    end_point = (400, 400)

    # Calculer le profil d'intensité le long de la ligne
    profile = intensity_profile(image, start_point, end_point)

    # Tracer le profil d'intensité
    plt.plot(profile)
    plt.title("Profil d'intensité le long de la ligne")
    plt.xlabel("Position")
    plt.ylabel("Intensité")
    plt.show()

if __name__ == "__main__":
    main()
