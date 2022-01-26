# Three lines to make our compiler able to draw:
import numpy as np
import matplotlib.pyplot as plt
import sys
import matplotlib
matplotlib.use('Agg')


xpoints = np.array([0, 6])
ypoints = np.array([0, 250])

plt.plot(xpoints, ypoints)
plt.show()

# Two  lines to make our compiler able to draw:
plt.savefig(sys.stdout.buffer)
sys.stdout.flush()
