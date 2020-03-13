from scipy import misc
f = misc.face()

import matplotlib.pyplot as plt
plt.imshow(f,vmin=30, vmax=200)
plt.show()
