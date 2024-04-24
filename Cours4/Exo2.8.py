from PIL import Image
import numpy as np

def adjust_brightness(image, adjustment):
    # Convertir l'image en tableau numpy
    pixel_array = np.array(image)

    # Extraire les composantes rouge, vert et bleu
    rouge = pixel_array[:,:,0]
    vert = pixel_array[:,:,1]
    bleu = pixel_array[:,:,2]

    # Ajouter la valeur d'ajustement à chaque composante en utilisant np.clip pour s'assurer que les valeurs restent entre 0 et 255
    new_rouge = np.clip(rouge + adjustment, 0, 255)
    new_vert = np.clip(vert + adjustment, 0, 255)
    new_bleu = np.clip(bleu + adjustment, 0, 255)

    # Créer un nouveau tableau avec les valeurs modifiées
    new_pixel_array = np.stack((new_rouge, new_vert, new_bleu), axis=-1)

    # Créer une nouvelle image à partir du tableau numpy modifié
    new_image = Image.fromarray(new_pixel_array.astype('uint8'))

    return new_image

def main():
    # Ouvrir l'image Lenna
    image = Image.open("images\\Lenna512.png")

    # Modifier la luminosité de l'image en augmentant de 50
    new_image = adjust_brightness(image, 50)
    new_image.show()

if __name__ == "__main__":
    main()