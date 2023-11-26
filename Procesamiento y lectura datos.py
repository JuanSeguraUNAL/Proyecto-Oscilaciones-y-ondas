import matplotlib.pyplot as plt
import numpy as np

# Bucle para la lectura y procesamiento de todos los datos tomados
for i in range(1, 7):
    # Se abren los archivos con los valores de intensidades y tiempos
    intensidades = open(f"Resultados/datos{i}.txt", "r")
    tiempo = open(f"Resultados/tiempos{i}.txt", "r")

    # Se extraen a un arreglo los valores del archivo de intensidades
    I = []
    for dato in intensidades:
        I.append(dato)
    I = I[0].split()
    I = [float(dato) for dato in I]

    # Se extraen a un arreglo los valores del archivo de tiempos
    t = []
    for ti in tiempo:
        t.append(ti)
    t = t[0].split()
    t = [float(ti) for ti in t]

    # Se realiza la transformada rápida de Fourier sobre los datos de intensidad (Se trabaja ahora sobre la variable k de número de onda)
    S = np.fft.fftshift(np.fft.fft(I))
    k = np.fft.fftshift(np.fft.fftfreq(len(I)))

    # Se grafica la intensidad de luz en función de la diferencia de camino óptico
    # Cabe recalcar que la diferencia de camino óptico en micrometros coincide con el tiempo en segundos dada la velocidad del espejo movible (1 micrometro por segundo)
    plt.subplot(2, 1, 1)
    plt.plot(t, I)
    plt.grid()
    plt.xlabel("Diferencia camino óptico (\u00B5m)")
    plt.ylabel("Intensidad de luz (candelas)")
    plt.title(f"Gráfica Intensidad vs distancia")

    # Se grafica la tranformada de Fourier en función del número de onda k
    plt.subplot(2, 1, 2)
    plt.plot(k, abs(S), label= "Norma", color= "purple")
    plt.plot(k, S.real, label="Parte real", color="blue")
    plt.plot(k, S.imag, label="Parte imaginaria", color="red")
    plt.grid()
    plt.xlabel("Número de onda k (1/\u00B5m)")
    plt.ylabel("Magnitud")
    plt.legend()
    plt.title(f"Gráfica transformada de Fourier")

    plt.tight_layout()
    plt.savefig(f"Gráfica intensidades{i}.png")
    plt.show()

