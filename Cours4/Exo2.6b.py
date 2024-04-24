from PIL import Image
import numpy as np

def isoler_couleur_seuil(image, seuil):
    # Convertir l'image en tableau numpy
    pixel_array = np.array(image)

    # Récupérer la composante rouge de chaque pixel
    composante_rouge = pixel_array[:,:,0]

    # Créer un masque en fonction du seuil
    masque = np.where(composante_rouge >= seuil, 255, 0)

    # Remplacer la composante rouge par le masque
    couleur_isolee = np.zeros_like(pixel_array)
    couleur_isolee[:,:,0] = masque

    # Créer une nouvelle image à partir du tableau numpy de la couleur isolée
    image_couleur_isolee = Image.fromarray(couleur_isolee.astype('uint8'))

    return image_couleur_isolee

def main():
    # Ouvrir l'image du singe
    image = Image.open("images\\Lenna512.jpg")

    # Isoler les zones dont la composante rouge dépasse le seuil de 220
    image_rouge_isolee = isoler_couleur_seuil(image, 220)
    image_rouge_isolee.show()

if __name__ == "__main__":
    main()
