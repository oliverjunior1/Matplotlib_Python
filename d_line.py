import matplotlib.pyplot as plt
import numpy as np

ypoints = np.array([3,8,1,10])
xpoints = np.array([10,5,4,3])

# plt.plot(ypoints, linestyle = 'dotted')
# plt.plot(ypoints, linestyle = 'dashed')
# plt.plot(ypoints, ls = ':')
# plt.plot(ypoints, color = 'r')
# plt.plot(ypoints, c = '#4CAF50')
plt.plot(ypoints, c = 'hotpink', linewidth = '20.5')
plt.plot(xpoints, c = 'blue', linewidth = '20.5')

plt.show()