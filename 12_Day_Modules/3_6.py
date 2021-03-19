from random import randint, choice

# def rgb_color_gen(r = randint(0, 256), g = randint(0, 256), b = randint(0, 256)):
#     return f'rgb({r}, {g}, {b})'
#
# print(rgb_color_gen())
#
# def list_of_hexa_color():
#     hexaArray = list()
#     hexa = 'abcdef' + '0123456789'
#     hexaColor = ''.join(choice(hexa) for i in range(6))
#     hexaArray.append('#' + hexaColor)
#     return hexaArray
#
# print(list_of_hexa_color())
#
# def list_of_rgb_colors():
#     listrgb = list()
#     colors = int(input('Number of colors: '))
#     r, g, b = randint(0, 256), randint(0, 256), randint(0, 256)
#     for i in range(colors):
#         listrgb.append(f'rgb({r}, {g}, {b})')
#     return listrgb
#
# print(list_of_rgb_colors())


def generate_colors(typeColor:str, quant: int):
    if typeColor == 'hexa':
        hexaArray = list()
        hexa = 'abcdef' + '0123456789'
        for i in range(quant):
            hexaColor = ''.join(choice(hexa) for i in range(6))
            hexaArray.append('#' + hexaColor)
        return hexaArray
    elif typeColor == 'rgb':
        listrgb = list()
        r, g, b = randint(0, 256), randint(0, 256), randint(0, 256)
        for i in range(quant):
            listrgb.append(f'rgb({r}, {g}, {b})')
        return listrgb


print(generate_colors('hexa', 3))
print(generate_colors('hexa', 1))
print(generate_colors('rgb', 3))
print(generate_colors('rgb', 1))
