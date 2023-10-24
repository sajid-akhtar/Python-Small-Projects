import colorgram

rgb_colors = []
colors = colorgram.extract(
    "D:/Python/python/Hirst-Painting-Project-GUI/image1.jpg", 30)

for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b

    rgb_colors.append((r, g, b))

print(rgb_colors)
