from PIL import Image


def main():
    try:
        # Relative Path
        img = Image.open("lenna.png")

        # Angle given
        rotated_img = img.rotate(180)

        # Saved in the same relative location
        rotated_img.save("rotated_picture.jpg")

    except IOError:
        pass

    try:
        # Relative Path
        img = Image.open("lenna.png")

        # transposing image
        transposed_img = img.transpose(Image.FLIP_LEFT_RIGHT)

        # Save transposed image
        transposed_img.save("transposed.jpg")

    except IOError:
        pass


if __name__ == "__main__":
    main()



# ref= https://www.geeksforgeeks.org/working-images-python/