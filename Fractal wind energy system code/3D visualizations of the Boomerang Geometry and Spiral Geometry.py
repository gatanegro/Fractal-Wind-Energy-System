import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

# Plotting 3D representations of Boomerang and Spiral geometries

# Boomerang geometry
def plot_boomerang(ax):
    # Parameters for boomerang curve
    x = np.linspace(-1, 1, 200)
    y = -np.abs(x) + 1  # Simple boomerang curve
    z = np.zeros_like(x)

    # Plot base curve
    ax.plot(x, y, z, color='blue', label='Boomerang Curve')

    # Add vertical thickness
    for i in range(-5, 6, 2):
        z_offset = i * 0.05
        ax.plot(x, y, z + z_offset, color='blue', alpha=0.5)

    # Highlight focal point (2/3 from the base)
    focal_point = int(len(x) * 2 / 3)
    ax.scatter(x[focal_point], y[focal_point], 0, color='red', label='Focal Point (2/3 Zone)', s=50)

    # Labels and title
    ax.set_title("Boomerang Geometry")
    ax.set_xlabel("X-axis (width)")
    ax.set_ylabel("Y-axis (height)")
    ax.set_zlabel("Z-axis (thickness)")
    ax.legend()

# Spiral geometry
def plot_spiral(ax):
    # Parameters for spiral curve
    theta = np.linspace(0, 4 * np.pi, 500)  # Spiral angle
    r = np.linspace(0.1, 1, 500)  # Spiral radius
    z = np.linspace(0, 1, 500)  # Spiral height (for 3D effect)

    x = r * np.cos(theta)
    y = r * np.sin(theta)

    # Plot spiral
    ax.plot(x, y, z, color='green', label='Spiral Curve')

    # Add nested layers for fractal scaling
    for scale in [0.8, 0.6, 0.4]:
        ax.plot(scale * x, scale * y, scale * z, color='green', alpha=0.5)

    # Highlight core region
    ax.scatter(0, 0, 0, color='red', label='Core Region', s=50)

    # Labels and title
    ax.set_title("Spiral Geometry")
    ax.set_xlabel("X-axis")
    ax.set_ylabel("Y-axis")
    ax.set_zlabel("Z-axis (height)")
    ax.legend()

# Plot both geometries
fig = plt.figure(figsize=(12, 6))

# Boomerang geometry
ax1 = fig.add_subplot(121, projection='3d')
plot_boomerang(ax1)

# Spiral geometry
ax2 = fig.add_subplot(122, projection='3d')
plot_spiral(ax2)

plt.tight_layout()
plt.show()