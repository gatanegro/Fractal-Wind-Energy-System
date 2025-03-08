# 1. Analyze Energy Contributions

# Separate plots for boomerang node energy and background field energy
plt.figure(figsize=(10, 6))
plt.imshow(E_boomerang, extent=[0, L, 0, T], aspect='auto', origin='lower', cmap='viridis')
plt.colorbar(label='Boomerang Node Energy Density')
plt.title('Boomerang Node Energy Density')
plt.xlabel('Space (Amplitude)')
plt.ylabel('Time (Longitude)')
plt.show()

plt.figure(figsize=(10, 6))
plt.imshow(E_field, extent=[0, L, 0, T], aspect='auto', origin='lower', cmap='plasma')
plt.colorbar(label='Background Field Energy Density')
plt.title('Background Field Energy Density')
plt.xlabel('Space (Amplitude)')
plt.ylabel('Time (Longitude)')
plt.show()

# 2. Temporal and Spatial Analysis

# Energy density at a fixed spatial point (e.g., midpoint of the domain) over time
mid_point_idx = Nx // 2  # Index for the spatial midpoint
plt.figure(figsize=(10, 4))
plt.plot(t, E_total[:, mid_point_idx], label='Total Energy')
plt.plot(t, E_boomerang[:, mid_point_idx], label='Boomerang Node Energy', linestyle='--')
plt.plot(t, E_field[:, mid_point_idx], label='Background Field Energy', linestyle=':')
plt.title(f'Energy Density Over Time at Space Midpoint (x = {x[mid_point_idx]:.2f})')
plt.xlabel('Time (Longitude)')
plt.ylabel('Energy Density')
plt.legend()
plt.grid()
plt.show()

# Energy density across space at a fixed moment in time (e.g., halfway through the simulation)
mid_time_idx = Nt // 2  # Index for the temporal midpoint
plt.figure(figsize=(10, 4))
plt.plot(x, E_total[mid_time_idx, :], label='Total Energy')
plt.plot(x, E_boomerang[mid_time_idx, :], label='Boomerang Node Energy', linestyle='--')
plt.plot(x, E_field[mid_time_idx, :], label='Background Field Energy', linestyle=':')
plt.title(f'Energy Density Across Space at Time t = {t[mid_time_idx]:.2f}')
plt.xlabel('Space (Amplitude)')
plt.ylabel('Energy Density')
plt.legend()
plt.grid()
plt.show()

# 3. Summary Statistics

# Compute maximum, minimum, and mean energy density over time and space
max_energy_time = E_total.max(axis=1)  # Max energy density for each time step
min_energy_time = E_total.min(axis=1)  # Min energy density for each time step
mean_energy_time = E_total.mean(axis=1)  # Mean energy density for each time step

plt.figure(figsize=(10, 4))
plt.plot(t, max_energy_time, label='Max Energy', linewidth=1.5)
plt.plot(t, min_energy_time, label='Min Energy', linewidth=1.5)
plt.plot(t, mean_energy_time, label='Mean Energy', linewidth=1.5)
plt.title('Energy Density Statistics Over Time')
plt.xlabel('Time (Longitude)')
plt.ylabel('Energy Density')
plt.legend()
plt.grid()
plt.show()