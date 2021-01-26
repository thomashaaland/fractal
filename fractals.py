import matplotlib.pyplot as plt
import numpy as np

frac = lambda z, c: z**2 + c

#z = np.cos(0.899) + np.sin(0.899)*1j
#c = 0.01 - 0.01j

epsilon = 0
dims = (1200, 800)

z = 1
iz = 3/z
jz = 2/z
ix = -dims[0]/5
iy = 0
canvas = np.zeros(dims)

for i, row in enumerate(canvas):
    for j, num in enumerate(row):
        it = -1
        c = (i - dims[0]/2 + ix)/dims[0] * iz + 1j*(j - dims[1]/2 + iy)/dims[1] * jz
        z = frac(0, c)
        try:
            while abs(z) > epsilon and it < 256:
                z = frac(z, c)
                it += 1
        except:
            it = 0
        canvas[i,j] = 256 - it
        print("Finished: ", round((i*dims[1] + j)/(dims[0]*dims[1])*100, 1), "%", end = '\r')

plt.imshow(canvas.T, cmap = 'Spectral', vmin = 0, vmax = 256)
plt.axis('off')
plt.show()
