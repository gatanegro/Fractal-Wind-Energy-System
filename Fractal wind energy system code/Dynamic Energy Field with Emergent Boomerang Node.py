# Refined Simulation: Dynamic Energy Field with Emergent Boomerang Node

# Define simulation parameters
L = 10           # Spatial domain length
T = 10           # Temporal domain length
Nx = 200         # Number of spatial points
Nt = 200         # Number of temporal points
dx = L / Nx      # Spatial resolution
dt = T / Nt      # Temporal resolution

# Field parameters
sigma = L / 10   # Width of the boomerang node (spatial scale)
k = 2 * np.pi / 5  # Wave number for oscillations

# Grid setup
x = np.linspace(0, L, Nx)  # Space grid
t = np.linspace(0, T, Nt)  # Time grid
X, T_grid = np.meshgrid(x, t)  # Spatiotemporal grid

# Initial energy field: Boomerang node as a localized energy perturbation
E = np.exp(-((x - L / 2) ** 2) / (2 * sigma ** 2))  # Energy density at t=0
U = np.zeros(Nx)  # Initial velocity (tensions) field

# Storage for field evolution
E_field = np.zeros((Nt, Nx))  # Energy field over time
U_field = np.zeros((Nt, Nx))  # Velocity (tensions) field over time

# Store initial conditions
E_field[0, :] = E
U_field[0, :] = U

# Simulation loop: Update energy and tension fields over time
for n in range(1, Nt):
    # Compute gradients
    dE_dx = np.gradient(E, dx)  # Energy density gradient
    dU_dx = np.gradient(U, dx)  # Velocity gradient

    # Update equations
    U = U - dt * dE_dx  # Update velocity (tensions) using energy gradient
    E = E - dt * np.gradient(U * E, dx)  # Update energy using continuity

    # Store updated fields
    E_field[n, :] = E
    U_field[n, :] = U

# Visualization: Energy field evolution in "slow motion"
plt.figure(figsize=(10, 6))
plt.imshow(E_field, extent=[0, L, 0, T], aspect='auto', origin='lower', cmap='jet')
plt.colorbar(label='Energy Density')
plt.title('Energy Field Evolution in Slow Motion')
plt.xlabel('Space (Amplitude)')
plt.ylabel('Time (Longitude)')
plt.show()

# Visualization: Tension field evolution in "slow motion"
plt.figure(figsize=(10, 6))
plt.imshow(U_field, extent=[0, L, 0, T], aspect='auto', origin='lower', cmap='coolwarm')
plt.colorbar(label='Tension Magnitude')
plt.title('Tension Field Evolution in Slow Motion')
plt.xlabel('Space (Amplitude)')
plt.ylabel('Time (Longitude)')
plt.show()

# Dynamic energy profiles at specific time slices
for n in range(0, Nt, 10):  # Every 10th time step
    plt.figure(figsize=(8, 4))
    plt.plot(x, E_field[n, :], label='Energy Density', linewidth=1.5)
    plt.plot(x, U_field[n, :], label='Tension', linestyle='--')
    plt.ylim([-1.5, 1.5])
    plt.title(f'Field Profiles at Time t = {t[n]:.2f}')
    plt.xlabel('Space (Amplitude)')
    plt.ylabel('Field Magnitude')
    plt.legend()
    plt.grid()
    plt.show()