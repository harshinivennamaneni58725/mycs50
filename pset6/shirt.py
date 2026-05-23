import sys
import os
from PIL import Image, ImageOps

def main():
    # 1. Validate the command-line argument count
    check_arguments()

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    try:
        # 2. Open the overlay shirt image and the input photo
        shirt = Image.open("shirt.png")
        muppet_img = Image.open(input_file)

    except FileNotFoundError:
        sys.exit("Input does not exist")

    # 3. Resize and crop the muppet image to match the precise size of the shirt
    # ImageOps.fit automatically takes care of the aspect ratio cropping
    muppet_img = ImageOps.fit(muppet_img, shirt.size)

    # 4. Overlay the shirt onto the muppet image
    # The 3rd parameter 'mask=shirt' maintains transparency edges correctly
    muppet_img.paste(shirt, (0, 0), mask=shirt)

    # 5. Save the final output image
    muppet_img.save(output_file)


def check_arguments():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")

    # Extract extensions and verify they are valid image types
    valid_ext = [".jpg", ".jpeg", ".png"]
    ext1 = os.path.splitext(sys.argv[1])[1].lower()
    ext2 = os.path.splitext(sys.argv[2])[1].lower()

    if ext1 not in valid_ext or ext2 not in valid_ext:
        sys.exit("Invalid input")

    if ext1 != ext2:
        sys.exit("Input and output have different extensions")


if __name__ == "__main__":
    main()
