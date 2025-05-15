from machine import Pin
import time

# Pin setup
reed_switch = Pin(16, Pin.IN, Pin.PULL_UP)
alarm_led = Pin(17, Pin.OUT)        # Blinking LED during alarm
buzzer = Pin(18, Pin.OUT)           # Active buzzer
button = Pin(14, Pin.IN)            # Button input (external pull-down)
armed_led = Pin(19, Pin.OUT)        # NEW: Armed status LED

alarm_on = False
button_was_pressed = False

print("Security system ready. Press button to toggle alarm ON/OFF.")

while True:
    # Button handling
    if button.value() == 1 and not button_was_pressed:
        alarm_on = not alarm_on
        print("Alarm is now:", "ON" if alarm_on else "OFF")
        button_was_pressed = True
        time.sleep(0.2)  # Debounce delay

    if button.value() == 0:
        button_was_pressed = False

    # Set armed LED
    if alarm_on:
        armed_led.on()
    else:
        armed_led.off()

    # Alarm condition: armed + reed switch open
    if alarm_on and reed_switch.value() == 1:
        alarm_led.on()
        buzzer.on()
    else:
        alarm_led.off()
        buzzer.off()

    time.sleep(0.05)
