# 1. Track the size and shape of the boomerang node (energy density over time)
# Define a threshold to identify the boomerang's "size" in space at each time step
threshold = 0.2 * E_boomerang.max()  # A fraction of the maximum energy density

# Compute the size of the boomerang at each time step
boomerang_size_over_time = []
for i in range(Nt):
    active_region = np.abs(E_boomerang[i, :]) > threshold  # Regions above the threshold
    boomerang_size = x[active_region].ptp() if active_region.any() else 0  # Size in spatial domain
    boomerang_size_over_time.append(boomerang_size)

# 2. Compute and visualize energy flux (gradient)
energy_flux_x = -np.gradient(E_total, axis=1)  # Spatial flux (negative gradient)
energy_flux_t = -np.gradient(E_total, axis=0)  # Temporal flux (negative gradient)

# Magnitude of flux (for visualization)
flux_magnitude = np.sqrt(energy_flux_x**2 + energy_flux_t**2)

# 3. Visualize the restoring forces (tensions) as a vector field
# Downsample for clarity in vector field visualization
downsample_factor = 10
X_down, T_down = X[::downsample_factor, ::downsample_factor], T_grid[::downsample_factor, ::downsample_factor]
flux_x_down, flux_t_down = energy_flux_x[::downsample_factor, ::downsample_factor], energy_flux_t[::downsample_factor, ::downsample_factor]

# Plotting the energy flux vector field overlay
plt.figure(figsize=(10, 6))
plt.imshow(E_total, extent=[0, L, 0, T], aspect='auto', origin='lower', cmap='coolwarm', alpha=0.7)
plt.colorbar(label='Total Energy Density')
plt.quiver(X_down, T_down, flux_x_down, flux_t_down, color='black', scale=50, alpha=0.8)
plt.title('Restoring Forces (Energy Flux) and Energy Distribution')
plt.xlabel('Space (Amplitude)')
plt.ylabel('Time (Longitude)')
plt.show()

# 4. Visualize the boomerang size evolution over time
plt.figure(figsize=(10, 4))
plt.plot(t, boomerang_size_over_time, label='Boomerang Size', color='purple')
plt.title('Boomerang Node Size Over Time')
plt.xlabel('Time (Longitude)')
plt.ylabel('Boomerang Size (Spatial Extent)')
plt.grid()
plt.legend()
plt.show()