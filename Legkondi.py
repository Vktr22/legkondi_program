from ev3dev.ev3 import *
import time


from time import sleep
from machine import ADC
# https://bhave.sh/micropython-measure-temperature/
""" #setup
thermistor_pin = ADC(26)

#loop
while True:
    thermistor_value = thermistor_pin.read_u16()
    print(thermistor_value)
    sleep(0.1) """

# Initialize the temperature sensor
temperature_sensor = Sensor(address=INPUT_1, driver_name='ht-nxt-temp')

# Initialize the motor
motor = LargeMotor(OUTPUT_A)


# Main loop
while True:
    # Read the temperature value in Celsius
    temperature = temperature_sensor.value() / 10.0  # Sensor returns value in tenths of degrees

    # Check if the temperature is equal to or greater than 26 degrees Celsius
    if temperature >= 26:
        # Turn on the motor
        motor.run_forever(speed_sp=500)
    else:
        # Turn off the motor
        motor.stop(stop_action='brake')
    
    # Wait for a short time before checking again
    time.sleep(1)


from ev3dev.ev3 import *
import time

# Initialize the temperature sensor
temperature_sensor = Sensor(address=INPUT_1, driver_name='ht-nxt-temp')

# Initialize the motor
motor = LargeMotor(OUTPUT_A)

# Main loop
while True:
    # Read the temperature value in Celsius
    temperature = temperature_sensor.value() / 10.0  # Sensor returns value in tenths of degrees

    # Print the temperature for debugging
    print("Temperature:", temperature)
    
    # Check if the temperature is equal to or greater than 26 degrees Celsius
    if temperature >= 26:
        # Turn on the motor
        motor.run_forever(speed_sp=500)
    else:
        # Turn off the motor
        motor.stop(stop_action='brake')
    
    # Wait for a short time before checking again
    time.sleep(1)

