from PIL import Image
import matplotlib.pyplot as plt
import random
import numpy as np


def interpolarLaplace(oprarray, imagearray):
    for pixelY in range(len(oprarray)):
        for pixelX in range(len(oprarray[0])):
            if oprarray[i, j] == 99999:
                if pixelY == 0 and pixelX == 0:
                    solved = (
                        np.linalg.solve([[1]], [(oprarray[pixelY, pixelX + 1] + oprarray[pixelY + 1, pixelX]) * 0.5]))
                    imagearray[i, j, 0] = int(solved[0])
                    continue
                if pixelY == 0 and pixelX == len(oprarray[0]) - 1:
                    solved = (
                        np.linalg.solve([[1]], [(oprarray[pixelY, pixelX - 1] + oprarray[pixelY + 1, pixelX]) * 0.5]))
                    imagearray[i, j, 0] = int(solved[0])
                    continue
                if pixelY == len(oprarray) - 1 and pixelX == 0:
                    solved = (
                        np.linalg.solve([[1]], [(oprarray[pixelY, pixelX + 1] + oprarray[pixelY - 1, pixelX]) * 0.5]))
                    imagearray[i, j, 0] = int(solved[0])
                    continue
                if pixelY == len(oprarray) - 1 and pixelX == len(oprarray[0]) - 1:
                    solved = (
                        np.linalg.solve([[1]], [(oprarray[pixelY - 1, pixelX] + oprarray[pixelY - 1, pixelX]) * 0.5]))
                    imagearray[i, j, 0] = int(solved[0])
                    continue
                if pixelY == 0 or pixelY == len(oprarray) - 1:
                    solved = (
                        np.linalg.solve([[1]], [(oprarray[pixelY, pixelX - 1] + oprarray[pixelY, pixelX + 1]) * 0.5]))
                    imagearray[i, j, 0] = int(solved[0])
                    continue
                if pixelX == 0 or pixelX == len(oprarray[0]) - 1:
                    solved = (
                        np.linalg.solve([[1]], [(oprarray[pixelY - 1, pixelX] + oprarray[pixelY + 1, pixelX]) * 0.5]))
                    imagearray[i, j, 0] = int(solved[0])
                    continue
                    # Punto normal
                solved = (np.linalg.solve([[1]], [
                    (oprarray[pixelY + 1, pixelX] + oprarray[pixelY - 1, pixelX] + oprarray[pixelY, pixelX + 1] +
                     oprarray[
                         pixelY, pixelX - 1]) * 0.25]))
                imagearray[i, j, 0] = int(solved[0])
            else:
                imagearray[i, j, 0] = oprarray[i, j]
    return imagearray


# Cargar imagen
f = Image.open('./imagenes/cat.jpg').convert('RGB').convert('LA')
value = [int(x / 2) for x in f.size]
f = f.resize(value)
x, y = f.size
# Convertir en array
arrayoriginal = np.array(f)
arraycopia = arrayoriginal.copy()
array2 = np.full((y, x), 0)

for i in range(len(arrayoriginal)):
    for j in range(len(arrayoriginal[0])):
        if random.random() < 0.5:
            newValue = arrayoriginal[i, j]
            newValue[0] = 255
            arrayoriginal[i, j] = newValue

for i in range(len(array2)):
    for j in range(len(array2[0])):
        if arrayoriginal[i, j, 0] == 255:
            array2[i, j] = 99999
        else:
            array2[i, j] = arrayoriginal[i, j, 0]

interpolado = interpolarLaplace(array2, arrayoriginal)

imagenoriginal = Image.fromarray(arraycopia)
imagendanada = Image.fromarray(arrayoriginal)
imageninterpolada = Image.fromarray(interpolado)

f, axarr = plt.subplots(3)
axarr[0].imshow(imagenoriginal)
axarr[1].imshow(imagendanada)
axarr[2].imshow(imageninterpolada)

plt.show()
