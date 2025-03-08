from scipy.fftpack import fft, fftfreq

# 1. Fourier Transform to Analyze Frequency (along the time axis)
# Compute FFT for the boomerang node and the field
fft_boomerang = fft(E_boomerang, axis=0)  # Along the time axis
fft_field = fft(E_field, axis=0)          # Along the time axis

# Compute the corresponding frequencies
frequencies = fftfreq(Nt, d=(T / Nt))  # Frequencies in the temporal domain

# Magnitudes of the FFT (spectral power)
magnitude_boomerang = np.abs(fft_boomerang)
magnitude_field = np.abs(fft_field)

# 2. Dominant Frequency Components (focusing on positive frequencies)
positive_freqs = frequencies[frequencies >= 0]
spectral_power_boomerang = magnitude_boomerang[frequencies >= 0, :]
spectral_power_field = magnitude_field[frequencies >= 0, :]

# Visualize frequency spectra for the boomerang node and field
plt.figure(figsize=(10, 6))
plt.plot(positive_freqs, spectral_power_boomerang.mean(axis=1), label='Boomerang Node Spectrum')
plt.plot(positive_freqs, spectral_power_field.mean(axis=1), label='Field Spectrum', linestyle='--')
plt.title('Frequency Spectrum of Boomerang Node and Field')
plt.xlabel('Frequency (Time Domain)')
plt.ylabel('Spectral Power')
plt.legend()
plt.grid()
plt.show()

# 3. Spatial Energy Density at a Dominant Frequency (e.g., peak frequency of the boomerang node)
dominant_freq_idx = np.argmax(spectral_power_boomerang.mean(axis=1))  # Index of peak frequency
dominant_freq = positive_freqs[dominant_freq_idx]

# Extract spatial energy density at the dominant frequency
spatial_energy_boomerang = np.abs(fft_boomerang[dominant_freq_idx, :])
spatial_energy_field = np.abs(fft_field[dominant_freq_idx, :])

# Visualize spatial energy density at the dominant frequency
plt.figure(figsize=(10, 4))
plt.plot(x, spatial_energy_boomerang, label=f'Boomerang Node at f={dominant_freq:.2f}')
plt.plot(x, spatial_energy_field, label=f'Field at f={dominant_freq:.2f}', linestyle='--')
plt.title(f'Spatial Energy Density at Dominant Frequency f={dominant_freq:.2f}')
plt.xlabel('Space (Amplitude)')
plt.ylabel('Energy Density')
plt.legend()
plt.grid()
plt.show()