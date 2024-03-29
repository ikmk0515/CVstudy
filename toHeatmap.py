import numpy as np
import pandas as pd

import matplotlib.pyplot as plt

data = [[976, 0, 0, 0, 6, 18, 0],
      [0, 977, 0, 0, 3, 0, 0],
      [1, 0, 982, 0, 0, 6, 11],
      [1, 2, 2, 995, 0, 0, 0],
      [14, 0, 0, 0, 975, 11, 0],
      [17, 0, 0, 0, 5, 978, 0],
      [0, 0, 3, 0, 0, 0, 997]]

# data = np.random.rand(10,10)
plt.title("Heatmap", fontsize=20)
plt.xlabel("Estimated Label")
plt.ylabel("True label")
plt.imshow(data, cmap='Blues')
plt.colorbar()
plt.show()
