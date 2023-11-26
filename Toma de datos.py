from gpiozero import LightSensor, Buzzer
import time

ldr = LightSensor(4, threshold=0.000001, charge_time_limit=0.05)

datos = open(f'datos{numerito}.txt', 'w')
tiempos= open(f'tiempos{numerito}.txt','w')
ti= time.time()
while True:
    print(ldr.value)
    datos.write(f'{ldr.value} ')
    tf= time.time()
    tiempo = tf-ti
    tiempos.write(f'{tiempo} ')
    
    

    



    