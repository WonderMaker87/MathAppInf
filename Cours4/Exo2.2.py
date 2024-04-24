from PIL import Image
import numpy as np

def main():
    # Ouvrir l'image du damier de couleur rouge, vert et bleu de 3x2 pixels
    image = Image.open("images\\6x2.png")

    # Afficher les dimensions de l'image
    width, height = image.size
    print("Dimensions de l'image : {} x {}".format(width, height))

    # Convertir l'image en tableau numpy
    pixel_array = np.array(image)

    # Afficher le tableau des valeurs des pixels
    print("Tableau des valeurs des pixels :")
    print(pixel_array)

    # Sauvegarder l'image d'entrée
    image.save("image_entree.png")

    # Effectuer une manipulation sur l'image (dans cet exemple, aucune manipulation n'est effectuée)

    # Sauvegarder l'image de sortie après manipulation
    image.save("image_sortie.png")

if __name__ == "__main__":
    main()
