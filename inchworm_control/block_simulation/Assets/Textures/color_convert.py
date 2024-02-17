from PIL import Image

def convert_black_to_color(image_path, tolerance=30):
    # Open the image
    img = Image.open(image_path)
    pixels = img.load()

    # Define what we consider as 'almost black'
    def is_almost_black(pixel):
        if len(pixel) == 4:  # If the image has an alpha channel
            r, g, b, a = pixel
            return r < tolerance and g < tolerance and b < tolerance and a == 255
        else:  # No alpha channel
            r, g, b = pixel
            return r < tolerance and g < tolerance and b < tolerance

    # Iterate over the pixels
    for i in range(img.size[0]):
        for j in range(img.size[1]):
            if is_almost_black(pixels[i, j]):
                pixels[i, j] = (0, 0, 255)  # Change to green

    # Save or display the modified image
    img.show()  # This will display the modified image


convert_black_to_color('smart_block.png')
