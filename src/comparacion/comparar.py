from skimage.metrics import structural_similarity as ssim
from skimage.metrics import mean_squared_error as mse
from PIL import Image
import numpy as np
import logging

# Create and configure logger
logging.basicConfig(format='%(asctime)s %(message)s', filemode='w')
logger = logging.getLogger()
logger.setLevel(logging.INFO)

original_bw = np.array(Image.open("imagenes/original.jpg").convert("LA"))
danada_bw = np.array(Image.open("imagenes/danada.jpg").convert("LA"))
restaurada_bw = np.array(Image.open("imagenes/restaurada.jpg").convert("LA"))

original_color = np.array(Image.open("imagenes/original.jpg"))
danada_color = np.array(Image.open("imagenes/danada.jpg"))
restaurada_color = np.array(Image.open(" vvimagenes/restaurada.jpg"))

logger.info("------ SIMILAR A BLANCO NEGRO ------")
logger.info("         ------ SSIM ------")
ssim_original_bw = ssim(original_bw, danada_bw, multichannel=True)
ssim_recuperado_bw = ssim(original_bw, restaurada_bw, multichannel=True)
porcentaje_recuperado_bw_ssim = (ssim_recuperado_bw - ssim_original_bw) * 100
logger.info("Se recupero aproximadamente un: " + str(porcentaje_recuperado_bw_ssim) + "%")

logger.info("         ------ MSE ------")
mse_original_bw = mse(original_bw, danada_bw)
mse_recuperado_bw = mse(original_bw, restaurada_bw)
porcentaje_recuperado_bw_mse = 100 - ((100 * mse_recuperado_bw) / mse_original_bw)
logger.info("Se recupero aproximadamente un: " + str(porcentaje_recuperado_bw_mse) + "%")

logger.info("------ SIMILAR A COLOR ------")
logger.info("     ------ SSIM ------")
ssim_original_color = ssim(original_color, danada_color, multichannel=True)
ssim_recuperado_color = ssim(original_color, restaurada_color, multichannel=True)
porcentaje_recuperado_bw_ssim = (ssim_recuperado_color - ssim_original_color) * 100
logger.info("Se recupero aproximadamente un: " + str(porcentaje_recuperado_bw_ssim) + "%")

logger.info("      ------ MSE ------")
mse_original_color = mse(original_color, danada_color)
mse_recuperado_color = mse(original_color, restaurada_color)
porcentaje_recuperado_bw_mse = 100 - ((100 * mse_recuperado_color) / mse_original_color)
logger.info("Se recupero aproximadamente un: " + str(porcentaje_recuperado_bw_mse) + "%")
