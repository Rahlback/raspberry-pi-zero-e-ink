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

    * get_rgb_text(rgb_value) - Returns the encoded string of a RGB value
    * image_to_ascii(image) - Returns the image as a string
    * save_string(string_to_save, filename, file_format) - Saves a string in a file

Required package:
* PIL

"""

from PIL import Image
from os import listdir

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
        if rgb_value[3] == 0: # White-space
            return "11" # 11
        rgb_value = [rgb_value[0], rgb_value[1], rgb_value[2]]

    for index, value in enumerate(rgb_value):
        if value > 180:
            rgb_value[index] = 255
        else:
            rgb_value[index] = 0

    if rgb_value == [255, 0, 0]: # Red
        return "01" # 01
    elif 255 in rgb_value: # Anything that is not red, will be white
        return "00" # 00
    elif rgb_value == [0, 0, 0]: # Black
        return "10" # 10

def image_to_ascii(image):
    """Converts an image into text.

    Enumerates over all pixels in image and converts each value into
    a character.

    Parameter:
        image - Raw data of a RGBA png file

    Returns:
        String - A string containing a character for each pixel in the image.

    """
    width, height = image.size

    string_builder = ""
    for index, pixel in enumerate(image.getdata(), start=1):
        string_builder += get_rgb_text(pixel)
        if ((index) % width == 0):
            string_builder += '\n' #+ str((index) / width) + " "

    return string_builder

def save_string(string_to_save, filename="default_filename", file_format="txt"):
    """Saves the string image as a file.
    Default filename is 'default_filename.txt'.

    Parameters:
        string_to_save - The string that will be saved in the file.
        filename - Filename. Defaults to 'default_filename'
        file_format - File format of the file. Defaults to txt.
    """
    filename_and_path = filename + "." + file_format
    f = open(filename_and_path, "w")
    f.write(string_to_save)
    f.close()


def main():
    """Creates files with converted data from all images in  './images'.
    Saves all the converted data in './converted_images'.
    """
    image_path = './images/'
    list_of_files = listdir(image_path)

    save_path = './converted_images/'
    for filename in list_of_files:
        if filename.split('.')[1] == 'png':
            with Image.open(image_path + filename) as im:
                print(filename)
                im = im.convert("RGBA")
                save_string(image_to_ascii(im), filename=save_path + filename)
    #
    # file_to_test = "unopened_letter.png"
    # im = Image.open("./images/" + file_to_test)
    # im = im.convert("RGBA")
    # save_string(image_to_ascii(im), file_to_test.split('.')[0])
    # im.close()

if __name__ == '__main__':
    main()
