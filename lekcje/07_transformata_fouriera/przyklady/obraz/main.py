"""
W tym przykladzie na obrazie mamy dwie linie: jedna pionowa i jedna pozioma. 
Po zastosowaniu FFT i wyswietleniu widma amplitudowego, zauwazysz, ze na 
spektrum pojawiaja sie dwa wyrazne maksima w pionie i poziomie, ktore 
odpowiadaja dwom liniom na obrazie. Jest to przyklad, jak FFT moze byc 
uzywane do analizy kierunkow w obrazach.
"""
import numpy as np
import matplotlib.pyplot as plt

# Utworzenie obrazu
image = np.zeros((128, 128))

# Dodanie dwoch linii o roznej orientacji
image[60:68, 10:120] = 1  # Pozioma linia
image[10:120, 60:68] = 1  # Pionowa linia

# Obliczenie 2D FFT obrazu
fft_image = np.fft.fft2(image)
fft_shift = np.fft.fftshift(fft_image)  # Przesuniecie zerowego punktu do centrum
magnitude_spectrum = np.log(np.abs(fft_shift) + 1)  # Obliczenie widma amplitudowego

# Wizualizacja
plt.figure(figsize=(12, 6))

# Oryginalny obraz
plt.subplot(1, 2, 1)
plt.imshow(image, cmap="gray")
plt.title("Oryginalny obraz")
plt.colorbar()

# Spektrum FFT
plt.subplot(1, 2, 2)
plt.imshow(magnitude_spectrum, cmap="gray")
plt.title("Spektrum FFT")
plt.colorbar()

plt.tight_layout()
plt.show()
