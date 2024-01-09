# create a function to get color name based on its RGB format
def get_color_name(rgb):
    match rgb:
        case (255, 0, 0):
            return "Red"
        case (255, 165, 0):
            return "Orange"
        case (255, 255, 0):
            return "Yellow"
        case (0, 128, 0):
            return "Green"
        case (0, 0, 255):
            return "Blue"
        case (255, 255, 255):
            return "White"
        case (128, 128, 128):
            return "Grey"
        case _:
            return "Unknown color / Неизвестный цвет"

# parse input value into tuple
input_color = input("Введите цвет в формате RGB (например, (255, 0, 0)): ")
rgb_values = tuple(map(int, input_color.strip('()').split(',')))

# call the function and print color name
color_name = get_color_name(rgb_values)
print(color_name)



# create a function to check that color is in RGB format
#import re
#def is_color_rgb(color):
    #rgb_pattern = re.compile(r'\(\s*(\d{1,3})\s*,\s*(\d{1,3})\s*,\s*(\d{1,3})\s*\)')
    #bool(rgb_pattern.match(color))

# get a color and check the format
#color = str(input("Введите цвет в формате RGB: "))
#if is_color_rgb(color): #if color match RGB proceed to matching checks