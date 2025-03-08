# 1. Compute energy flux (gradient in space) to measure tensions
energy_gradient_x = np.gradient(E_total, axis=1)  # Spatial gradient of energy density
energy_gradient_t = np.gradient(E_total, axis=0)  # Temporal gradient of energy density

# Magnitude of the tension (combined spatial and temporal gradients)
energy_tension = np.sqrt(energy_gradient_x**2 + energy_gradient_t**2)

# 2. Compute phase relationship between node and field
# Extract phases for E_boomerang and E_field
phase_boomerang = np.angle(E_boomerang + 1j * energy_gradient_x)  # Phase of boomerang energy
phase_field = np.angle(E_field + 1j * energy_gradient_x)  # Phase of field energy

# Phase difference (modulo 2π for clarity)
phase_difference = np.mod(phase_boomerang - phase_field, 2 * np.pi)

# 3. Visualizations

# Tension visualization (spatial-temporal gradients)
plt.figure(figsize=(10, 6))
plt.imshow(energy_tension, extent=[0, L, 0, T], aspect='auto', origin='lower', cmap='inferno')
plt.colorbar(label='Energy Tension Magnitude')
plt.title('Energy Tension (Gradient Magnitude)')
plt.xlabel('Space (Amplitude)')
plt.ylabel('Time (Longitude)')
plt.show()

# Phase difference visualization
plt.figure(figsize=(10, 6))
plt.imshow(phase_difference, extent=[0, L, 0, T], aspect='auto', origin='lower', cmap='twilight')
plt.colorbar(label='Phase Difference (rad)')
plt.title('Phase Relationship Between Boomerang Node and Field')
plt.xlabel('Space (Amplitude)')
plt.ylabel('Time (Longitude)')
plt.show()

# Plot tension at the midpoint of space over time
plt.figure(figsize=(10, 4))
plt.plot(t, energy_tension[:, mid_point_idx], label='Energy Tension at Midpoint')
plt.title(f'Energy Tension Over Time at Space Midpoint (x = {x[mid_point_idx]:.2f})')
plt.xlabel('Time (Longitude)')
plt.ylabel('Tension Magnitude')
plt.grid()
plt.legend()
plt.show()

# Plot phase difference at the midpoint of space over time
plt.figure(figsize=(10, 4))
plt.plot(t, phase_difference[:, mid_point_idx], label='Phase Difference at Midpoint', color='orange')
plt.title(f'Phase Difference Over Time at Space Midpoint (x = {x[mid_point_idx]:.2f})')
plt.xlabel('Time (Longitude)')
plt.ylabel('Phase Difference (rad)')
plt.grid()
plt.legend()
plt.show()
