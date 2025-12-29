import numpy as np
import matplotlib.pyplot as plt

# Image size
width, height = 800, 800
max_iter = 100

# Create complex plane
x = np.linspace(-2.5, 1.5, width)
y = np.linspace(-2.0, 2.0, height)
X, Y = np.meshgrid(x, y)
C = X + 1j * Y

# Mandelbrot iteration
Z = np.zeros(C.shape, dtype=complex)
img = np.zeros(C.shape)

for i in range(max_iter):
    mask = np.abs(Z) <= 2
    Z[mask] = Z[mask] ** 2 + C[mask]
    img[mask] = i

# Display
plt.imshow(img, cmap="inferno", extent=[-2.5, 1.5, -2, 2])
plt.colorbar(label="Iterations")
plt.title("Mandelbrot Fractal")
plt.show()
