from PIL import Image
import matplotlib.pyplot as plt
import random
import numpy as np
from scipy import sparse as sp
import scipy.sparse.linalg as linalg
import math
import time


def laplace(array, image):
    m = image.width
    n = image.height

    # A
    matrix = np.zeros((m * n, m * n))
    # b
    rhs = np.zeros(m * n)
    # x
    guess = np.zeros(m * n)
    guesstmp = 0
    inner = False
    i1, i2, i3, i4, j1, j2, j3, j4 = None, None, None, None, None, None, None, None
    k = 0
    for i in range(0, m):
        for j in range(0, n):
            # Top
            inner = False
            if i == 0:
                i1 = 0
                j1 = 1
                i2 = 1
                j2 = 0
            else:
                if j == n - 1:
                    i1 = 0
                    j1 = n - 2
                    i2 = 1
                    j2 = n - 1
                else:
                    i1 = i2 = 0
                    j1 = j - 1
                    j2 = j + 1

            # Bottom
            if i == m - 1:
                if j == 0:
                    i1 = m - 1
                    j1 = 1
                    i2 = m - 2
                    j2 = 0
                else:
                    if j == n - 1:
                        i1 = m - 1
                        j1 = n - 2
                        i2 = m - 2
                        j2 = n - 1
                    else:
                        i1 = i2 = m - 1
                        j1 = j - 1
                        j2 = j + 1

            # Left / right
            if i > 0 and i < m - 1:
                if j == 0 or j == n - 1:
                    j1 = j2 = j
                    i1 = i - 1
                    i2 = i + 1
                else:
                    # Inner
                    inner = True
                    i1 = i - 1
                    i2 = i - 1
                    i3 = i + 1
                    i4 = i + 1
                    j1 = j - 1
                    j2 = j + 1
                    j3 = j - 1
                    j4 = j + 1

            matrix[k, i * n + j] = 1
            if math.isnan(array[i, j]):
                if inner:
                    matrix[k, i1 * n + j1] = -0.25
                    matrix[k, i2 * n + j2] = -0.25
                    matrix[k, i3 * n + j3] = -0.25
                    matrix[k, i4 * n + j4] = -0.25
                else:
                    matrix[k, i1 * n + j1] = -0.5
                    matrix[k, i2 * n + j2] = -0.5
                rhs[k] = 0
                guess[k] = guesstmp
            else:
                rhs[k] = array[i, j]
                guess[k] = guesstmp = array[i, j]
            k = k + 1

    solution = linalg.bicgstab(sp.csc_matrix(matrix), rhs, guess)
    for a in range(0, m):
        for b in range(0, n):
            if (math.isnan(array[a, b])):
                array[a, b] = solution[0][a * n + b]
    print("ready")
    return array


start = time.time()
# Leer imagen - Blanco y negro para un solo canal de color.
image = Image.open('../imagenes/cat.jpg').convert('RGB')

# Reducir tamaño de la imagen
value = [int(x / 12) for x in image.size]
image = image.resize(value)

imageArray = np.array(image)
original = imageArray.copy()

canal_R, canal_G, canal_B = np.ndarray((image.height, image.width)), np.ndarray(
    (image.height, image.width)), np.ndarray((image.height, image.width))

for x in range(len(imageArray)):
    for y in range(len(imageArray[0])):
        canal_R[x, y] = imageArray[x, y, 0]
        canal_G[x, y] = imageArray[x, y, 1]
        canal_B[x, y] = imageArray[x, y, 2]
        if random.random() < 0.2:
            # Pixel malo
            imageArray[x, y] = [255, 255, 255]
            canal_R[x, y] = None
            canal_G[x, y] = None
            canal_B[x, y] = None

interpolR = laplace(canal_R, image)
interpolG = laplace(canal_G, image)
interpolB = laplace(canal_B, image)

rgbArray = np.zeros((image.width, image.height, 3), 'uint8')
rgbArray[..., 0] = interpolR
rgbArray[..., 1] = interpolG
rgbArray[..., 2] = interpolB

# Graficar
imgplot, axarr = plt.subplots(3)
axarr[0].imshow(Image.fromarray(original))
axarr[0].set_title("Original")
axarr[1].imshow(Image.fromarray(imageArray))
axarr[1].set_title("Danada")
axarr[2].imshow(Image.fromarray(rgbArray))
axarr[2].set_title("Interpolada con Laplace")

Image.fromarray(original).save("../comparacion/imagenes/original_mejorada.jpg")
Image.fromarray(imageArray).save("../comparacion/imagenes/danada_mejorada.jpg")
Image.fromarray(rgbArray).save("../comparacion/imagenes/restaurada_mejorada.jpg")

plt.show()
print("Se demoró: " + str(round(time.time() - start, 3)))
