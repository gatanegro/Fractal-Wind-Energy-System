# 1. Compute the phase angle of the boomerang node
boomerang_angle = np.mod(k * X - omega * T_grid, 2 * np.pi)  # Modulo 2π for clarity

# 2. Visualization of the phase angle across space and time
plt.figure(figsize=(10, 6))
plt.imshow(boomerang_angle, extent=[0, L, 0, T], aspect='auto', origin='lower', cmap='hsv')
plt.colorbar(label='Boomerang Angle (radians)')
plt.title('Boomerang Node Phase Angle Across Space and Time')
plt.xlabel('Space (Amplitude)')
plt.ylabel('Time (Longitude)')
plt.show()

# 3. Temporal trend of the boomerang angle at the spatial midpoint
plt.figure(figsize=(10, 4))
plt.plot(t, boomerang_angle[:, mid_point_idx], label='Boomerang Angle at Midpoint', color='blue')
plt.title(f'Boomerang Angle Over Time at Space Midpoint (x = {x[mid_point_idx]:.2f})')
plt.xlabel('Time (Longitude)')
plt.ylabel('Phase Angle (radians)')
plt.grid()
plt.legend()
plt.show()