import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit

letras = ["A", "B", "C", "D", "E", "F"]

for i in range(0, 6):
    datos = open(f"Resultados/datos{letras[i]}.txt", "r")
    velocidad = open("velocidad.txt", "r")
    V = []
    for dato in velocidad:
        V.append(dato)
    v = float(V[0])

    I = []
    for dato in datos:
        I.append(dato)
    I = I[0].split()
    I = [float(dato) for dato in I]

    tf = len(I)/v
    t = np.linspace(0, tf, len(I))

    S = np.fft.fftshift(np.fft.fft(I))
    k = np.fft.fftshift(np.fft.fftfreq(len(I)))

    plt.subplot(2, 1, 1)
    plt.plot(t, I)
    plt.grid()
    plt.xlabel("Diferencia camino óptico (\u00B5m)")
    plt.ylabel("Intensidad de luz (candelas)")
    plt.title(f"Gráfica Intensidad vs distancia")

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
    plt.savefig(f"Gráfica datos{letras[i]}.png")
    plt.show()

    if i == 4:

        def Ia(h, Io, ka, alfa):
            return 2 * Io * (1 + np.cos(2* ka * h + alfa))


        # Supongamos que tienes tus datos en las variables t e I
        # Realizar el ajuste
        parametros_optimizados, matriz_covarianza = curve_fit(Ia, t, I)

        # Obtener los parámetros ajustados
        Io_optimo, ka_optimo, alfa_optimo = parametros_optimizados

        # Generar la curva ajustada
        I_ajustada = Ia(t, Io_optimo, ka_optimo, alfa_optimo)

        # Graficar los datos y la curva ajustada
        plt.plot(t, I, label='Datos originales', marker='o', linestyle='None')
        plt.plot(t, I_ajustada, label='Curva ajustada', linestyle='-', color='red')
        plt.xlabel('Diferencia camino óptico (µm)')
        plt.ylabel('Intensidad de luz (candelas)')
        plt.legend()
        plt.savefig("ajustico.png")
        plt.grid()
        plt.show()

        print(ka_optimo)







