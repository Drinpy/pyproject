from PIL import Image
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

def isometric_to_perspective(pixel_art_isometric):
    img = Image.open(pixel_art_isometric)
    width, height = img.size

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.set_proj_type('persp')

    cube_size = 1  # Tamanho do cubo

    for y in range(height):
        for x in range(width):
            # Cores dos cubos baseadas nos pixels da imagem
            color = img.getpixel((x, y))

            # Coordenadas para desenhar o cubo
            x_coords = [x, x + cube_size, x + cube_size, x, x]
            y_coords = [y, y, y + cube_size, y + cube_size, y]
            z_coords = [0, 0, 0, 0, 0]  # Posição Z no plano

            ax.scatter(x_coords, y_coords, z_coords, color=color, marker='s')

    ax.set_xlim([0, width])
    ax.set_ylim([0, height])
    ax.set_zlim([0, cube_size])

    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')

    plt.gca().invert_yaxis()
    plt.gca().invert_zaxis()

    plt.savefig("pixel_art_perspectiva_3d.png")
    plt.show()
