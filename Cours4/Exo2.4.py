from PIL import Image
import numpy as np

def image_miroir(image):
    # Convertir l'image en tableau numpy
    pixel_array = np.array(image)

    # Récupérer les dimensions de l'image
    nb_lignes, nb_colonnes, _ = pixel_array.shape

    # Créer un tableau pour l'image miroir
    miroir_array = np.zeros_like(pixel_array)

    # Inverser horizontalement l'image
    for ligne in range(nb_lignes):
        for colonne in range(nb_colonnes):
            miroir_array[ligne, colonne] = pixel_array[ligne, nb_colonnes - 1 - colonne]

    # Créer une nouvelle image à partir du tableau numpy
    image_miroir = Image.fromarray(miroir_array)

    return image_miroir

def main():
    # Ouvrir l'image Lenna512
    image = Image.open("images\\Lenna512.png")

    # Créer une image miroir
    image_miroir_result = image_miroir(image)

    # Afficher l'image miroir
    image_miroir_result.show()

if __name__ == "__main__":
    main()
