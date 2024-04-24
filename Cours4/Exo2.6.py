from PIL import Image
import numpy as np

def isoler_couleur(image, couleur):
    # Convertir l'image en tableau numpy
    pixel_array = np.array(image)

    # Créer un masque pour la couleur souhaitée
    if couleur == "rouge":
        masque = np.array([1, 0, 0])
    elif couleur == "vert":
        masque = np.array([0, 1, 0])
    elif couleur == "bleu":
        masque = np.array([0, 0, 1])

    # Appliquer le masque pour isoler la couleur souhaitée
    couleur_isolee = pixel_array * masque

    # Créer une nouvelle image à partir du tableau numpy de la couleur isolée
    image_couleur_isolee = Image.fromarray(couleur_isolee.astype('uint8'))

    return image_couleur_isolee

def main():
    # Ouvrir l'image Lenna512
    image = Image.open("images\\Lenna512.png")

    # Isoler la couleur rouge
    image_rouge_isolee = isoler_couleur(image, "rouge")
    image_rouge_isolee.show()

    # Isoler la couleur verte
    image_vert_isolee = isoler_couleur(image, "vert")
    image_vert_isolee.show()

    # Isoler la couleur bleue
    image_bleu_isolee = isoler_couleur(image, "bleu")
    image_bleu_isolee.show()

if __name__ == "__main__":
    main()
