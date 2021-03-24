"""Image converter

This script takes an image and encodes it into a binary image
specifically for an E-ink screen with 3 pixel color (Red, black, white).
Also supports transparent pixels.

Currently only accepts PNG files in the RGBA and RGB formats. All other
formats are untested.

Encoding table:
White = 00
Red = 01
Black = 10
Transparent = 11

This script can also be imported as a module and contains the following
functions:

    * get_rgb_text - Returns the encoded string of a RGB value
    * image_to_ascii - Returns the image fully encoded

"""
#
#
#
#





from PIL import Image

def get_rgb_text(rgb_value):
    """Gets the two bit representation of a RGB value.

    Parameters
    ----------
    rgb_value : tuple, array
        RGB or RGBA value of a pixel

    Returns
    -------
    string
        dependent on RGB value.
        White = "00"
        Red = "01"
        Black = "10"
        Transparent = "11"
    """

    if len(rgb_value) == 4:
        if rgb_value[3] == 0:
            return "11"
        rgb_value = [rgb_value[0], rgb_value[1], rgb_value[2]]

    for index, value in enumerate(rgb_value):
        if value > 180:
            rgb_value[index] = 255
        else:
            rgb_value[index] = 0

    if rgb_value == [255, 0, 0]: # Red
        return "01"
    elif 255 in rgb_value: # Anything that is not red, will be white
        return "00"
    elif rgb_value == [0, 0, 0]: # Black
        return "10"

def image_to_ascii(image):
    width, height = image.size

    string_builder = ""
    for index, pixel in enumerate(image.getdata(), start=0):
        if ((index) % width == 0):
            string_builder += '\n' #+ str((index) / width) + " "
        print(pixel)
        string_builder += get_rgb_text(pixel)


    print(string_builder)


def main():
    im = Image.open("./fonts/hejemma.png")
    print(im)


    image_to_ascii(im)

if __name__ == '__main__':
    main()
