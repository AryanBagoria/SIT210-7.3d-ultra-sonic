from gpiozero import DistanceSensor
from time import sleep
from gpiozero import PWMLED

led = PWMLED(17)

sensor = DistanceSensor(echo=16, trigger=24)
while True:
    measured_distance = sensor.distance * 100
    print('Distance:',measured_distance)
    sleep(1)
    if measured_distance < 30.0 and measured_distance > 20.0:
    led.value = 0.3
    sleep(1)
    elif measured_distance < 20.0 and measured_distance > 10.0:
    led.value = 0.6
    sleep(1)
    elif measured_distance < 10.0:
    led.value = 0.9
    sleep(1)

else:
    led.value = 0
    sleep(1)