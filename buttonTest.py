from signal import pause
from gpiozero import LED, Button

button = Button(21)
led = LED(7)

while True:
    led.on()
    # led.source = button.values
