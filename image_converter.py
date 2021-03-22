from PIL import Image

# Load test image

def get_rgb_text(rgb_value):

    if len(rgb_value) == 4:
        if rgb_value[3] == 0:
            return " "
        rgb_value = [rgb_value[0], rgb_value[1], rgb_value[2]]

    for index, value in enumerate(rgb_value):
        if value > 180:
            rgb_value[index] = 255
        else:
            rgb_value[index] = 0

    if rgb_value == [255, 0, 0]: # Red
        return "R"
    elif 255 in rgb_value: # Anything that is not red, will be white
        return " "
    elif rgb_value == [0, 0, 0]: # Black
        return "B"

def image_to_ascii(image):
    width, height = image.size

    string_builder = ""
    for index, pixel in enumerate(image.getdata(), start=0):
        if ((index) % width == 0):
            string_builder += '\n' #+ str((index) / width) + " "
        print(pixel)
        string_builder += get_rgb_text(pixel)


    print(string_builder)


im = Image.open("./fonts/hejemma.png")
print(im)


image_to_ascii(im)
