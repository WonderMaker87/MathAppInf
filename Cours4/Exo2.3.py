from PIL import Image
import numpy as np

def main():
    # Ouvrir l'image Lenna512
    image = Image.open("images\\Lenna512.png")

    # Récupérer une partie de l'image (le regard de Lenna)
    regard_lenna = image.crop((240, 240, 360, 290))  # Récupère la zone entre les lignes 240 et 290 et les colonnes 240 et 360

    # Afficher les dimensions du regard de Lenna
    width, height = regard_lenna.size
    print("Dimensions du regard de Lenna : {} x {}".format(width, height))

    # Afficher le regard de Lenna
    regard_lenna.show()

if __name__ == "__main__":
    main()
