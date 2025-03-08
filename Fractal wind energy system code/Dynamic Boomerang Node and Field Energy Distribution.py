# 1. Define the dynamic boomerang node simulation

# Parameters for the dynamic motion of the boomerang
boomerang_velocity = 2 * L / T  # Velocity of the boomerang node
boomerang_position = L / 2  # Initial position of the boomerang (centered)
boomerang_amplitude = A.copy()  # Base amplitude shape

# Pre-allocate arrays for the dynamic boomerang node and field
E_boomerang_dynamic = np.zeros_like(E_total)  # Dynamic boomerang node
E_field_dynamic = E_field.copy()  # Field remains oscillatory as defined

# Simulate boomerang movement
for i in range(Nt):
    # Compute the current position of the boomerang
    current_position = boomerang_position + boomerang_velocity * (t[i] - T / 2)
    
    # Reflect position when it crosses boundaries to simulate return
    if current_position < 0 or current_position > L:
        boomerang_velocity = -boomerang_velocity  # Reverse direction
    
    # Compute the amplitude envelope based on the current position
    A_dynamic = np.exp(-((x - current_position) ** 2) / (2 * (L / 10) ** 2))
    E_boomerang_dynamic[i, :] = A_dynamic * np.sin(k * x - omega * t[i])  # Update boomerang energy

# Total field energy with dynamic boomerang
E_total_dynamic = E_boomerang_dynamic + E_field_dynamic

# 2. Visualization of energy distribution over time (surface plot)
plt.figure(figsize=(10, 6))
plt.imshow(E_total_dynamic, extent=[0, L, 0, T], aspect='auto', origin='lower', cmap='jet')
plt.colorbar(label='Energy Density')
plt.title('Dynamic Boomerang Node and Field Energy Distribution')
plt.xlabel('Space (Amplitude)')
plt.ylabel('Time (Longitude)')
plt.show()

# 3. Dynamic visualization of energy profiles (boomerang motion and field response)
for i in range(0, Nt, 10):  # Animate every 10th time step for clarity
    plt.figure(figsize=(8, 4))
    plt.plot(x, E_total_dynamic[i, :], label='Total Energy', linewidth=1.5)
    plt.plot(x, E_boomerang_dynamic[i, :], label='Boomerang Node', linestyle='--')
    plt.plot(x, E_field_dynamic[i, :], label='Background Field', linestyle=':')
    plt.ylim([-1.5, 1.5])
    plt.title(f'Energy Profile at Time {t[i]:.2f}')
    plt.xlabel('Space (Amplitude)')
    plt.ylabel('Energy Density')
    plt.legend()
    plt.grid()
    plt.show()