from skimage.metrics import structural_similarity as ssim
from skimage.metrics import mean_squared_error as mse
from PIL import Image
import numpy as np
import logging

# Create and configure logger
logging.basicConfig(format='%(asctime)s %(message)s', filemode='w')
logger = logging.getLogger()
logger.setLevel(logging.INFO)

original = np.array(Image.open("ImagenesGen/original.jpg").convert("LA"))
restaurada = np.array(Image.open("ImagenesGen/restaurada.jpg").convert("LA"))

logger.info("------ SIMILAR A BLANCO NEGRO ------")
logger.info("         ------ SSIM ------")
ssim_recuperado = ssim(original, restaurada, multichannel=True)
porcentaje_recuperado_ssim = (ssim_recuperado) * 100
logger.info("Las imagene se parece aproximadamente en un: " + str(porcentaje_recuperado_ssim) + "%")

logger.info("         ------ MSE ------")
mse_recuperado = mse(original, restaurada)
#porcentaje_recuperado_mse = 100 - ((100 * mse_recuperado) / mse_original)
logger.info("Se recuper aproximadamente un: " + str(mse_recuperado))
