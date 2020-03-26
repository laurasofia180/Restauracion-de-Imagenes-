from PIL import Image
import matplotlib.pyplot as plt
import random
import numpy as np


def main():
    # Leer imagen - Blanco y negro para un solo canal de color.
    image = Image.open('./imagenes/cat.jpg').convert('RGB').convert('LA')

    value = [int(x / 2) for x in image.size]
    image = image.resize(value)

    image_array = np.array(image)
    bad_array = image_array.copy()
    # Daño el array
    for i in range(len(bad_array)):
        for j in range(len(bad_array[0])):
            if random.random() < 0.5:
                # Pixel malo
                bad_array[i, j] = [255, 255]
    bad_array_copy = bad_array.copy()
    # Proceso
    cols = len(bad_array)
    rows = len(bad_array[0])
    matriz_operacional = np.empty((cols, rows))

    # Creo una matriz para operaciones
    for i in range(len(bad_array)):
        for j in range(len(bad_array[0])):
            if bad_array[i, j, 0] > 254:
                matriz_operacional[i, j] = int(0)
            else:
                matriz_operacional[i, j] = int(bad_array[i, j, 0])

    # Laplace
    for pixelY in range(len(matriz_operacional)):
        for pixelX in range(len(matriz_operacional[0])):
            if matriz_operacional[pixelY, pixelX] == 0:
                if pixelY == 0 and pixelX == 0:
                    solved = (
                        np.linalg.solve([[1]], [
                            (matriz_operacional[pixelY, pixelX + 1] + matriz_operacional[pixelY + 1, pixelX]) * 0.5]))
                    bad_array[pixelY, pixelX, 0] = int(solved[0])
                    continue
                if pixelY == 0 and pixelX == len(matriz_operacional[0]) - 1:
                    solved = (
                        np.linalg.solve([[1]], [
                            (matriz_operacional[pixelY, pixelX - 1] + matriz_operacional[pixelY + 1, pixelX]) * 0.5]))
                    bad_array[pixelY, pixelX, 0] = int(solved[0])
                    continue
                if pixelY == len(matriz_operacional) - 1 and pixelX == 0:
                    solved = (
                        np.linalg.solve([[1]], [
                            (matriz_operacional[pixelY, pixelX + 1] + matriz_operacional[pixelY - 1, pixelX]) * 0.5]))
                    bad_array[pixelY, pixelX, 0] = int(solved[0])
                    continue
                if pixelY == len(matriz_operacional) - 1 and pixelX == len(matriz_operacional[0]) - 1:
                    solved = (
                        np.linalg.solve([[1]], [
                            (matriz_operacional[pixelY - 1, pixelX] + matriz_operacional[pixelY - 1, pixelX]) * 0.5]))
                    bad_array[pixelY, pixelX, 0] = int(solved[0])
                    continue
                if pixelY == 0 or pixelY == len(matriz_operacional) - 1:
                    solved = (
                        np.linalg.solve([[1]], [
                            (matriz_operacional[pixelY, pixelX - 1] + matriz_operacional[pixelY, pixelX + 1]) * 0.5]))
                    bad_array[pixelY, pixelX, 0] = int(solved[0])
                    continue
                if pixelX == 0 or pixelX == len(matriz_operacional[0]) - 1:
                    solved = (
                        np.linalg.solve([[1]], [
                            (matriz_operacional[pixelY - 1, pixelX] + matriz_operacional[pixelY + 1, pixelX]) * 0.5]))
                    bad_array[pixelY, pixelX, 0] = int(solved[0])
                    continue
                    # Punto normal
                solved = (np.linalg.solve([[1]], [
                    (matriz_operacional[pixelY + 1, pixelX] + matriz_operacional[pixelY - 1, pixelX] +
                     matriz_operacional[pixelY, pixelX + 1] +
                     matriz_operacional[
                         pixelY, pixelX - 1]) * 0.25]))
                bad_array[pixelY, pixelX, 0] = int(solved[0])
            else:
                bad_array[pixelY, pixelX, 0] = matriz_operacional[pixelY, pixelX]

    # Graficar
    imgplot, axarr = plt.subplots(3)
    axarr[0].imshow(Image.fromarray(image_array))
    axarr[0].set_title("Original")
    axarr[1].imshow(Image.fromarray(bad_array_copy))
    axarr[1].set_title("Dañada")
    axarr[2].imshow(Image.fromarray(bad_array))
    axarr[2].set_title("Interpolada con Laplace")
    plt.show()


if __name__ == '__main__':
    main()
