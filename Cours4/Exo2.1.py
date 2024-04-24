from PIL import Image

def main():
    # Ouvrir l'image
    image = Image.open("images\\Lenna512.jpg")

    # Afficher les dimensions de l'image
    width, height = image.size
    print("Dimensions de l'image : {} x {}".format(width, height))

    # Transformer l'image (copie dans cet exemple)
    new_image = image.copy()

    # Sauvegarder la nouvelle image sous un autre nom/format
    new_image.save("images_mod\\new_image.png")

if __name__ == "__main__":
    main()
