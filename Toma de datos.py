# Esta libreria se usa para detectar los niveles de luz recibidos y automatizar la carga y descarga del capacitor
from gpiozero import LightSensor, Buzzer
import time

ldr = LightSensor(4, threshold=0.000001, charge_time_limit=0.05)

# Se abren los archivos donde se escribiran los datos
datos = open(f'datos.txt', 'w')
tiempos= open(f'tiempos.txt','w')

#Se toma el tiempo inicial
ti= time.time()

while True:
    # Mostrar el valor de intensidad
    print(ldr.value)
    # Escribir dicho dato en el archivo para intensidades
    datos.write(f'{ldr.value} ')
    # Se toma el tiempo final y se halla el intervalo de tiempo desde que se empezzó a correr el código
    tf= time.time()
    tiempo = tf-ti
    # Escribir este intervalo de tiempo en el archivo para tiempos
    tiempos.write(f'{tiempo} ')
    
    

    



    