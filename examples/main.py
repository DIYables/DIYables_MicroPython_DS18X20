import machine
import onewire
import time
from machine import I2C, Pin
from DIYables_MicroPython_DS18X20 import DS18X20

ds_pin = machine.Pin('D2') # The Arduino Giga WiFi D2 connected to the DS18B20 sensorsensor
# Create the onewire object
OneWire = onewire.OneWire(ds_pin)
# Create the DS18X20 object
DS18B20 = DS18X20(OneWire)

# Scan for devices on the bus
sensor_addresses = DS18B20.scan()
print('Arduino found DS18B20 devices:', sensor_addresses)

# Main loop to read and print the temperature every second
while True:
    DS18B20.convert_temp()
    time.sleep_ms(750) # waiting for temperature conversion
    for address in sensor_addresses:
        temperature = DS18B20.read_temp(address)
        if temperature is not None:
            print('Temperature: {:.2f} °C'.format(temperature))
        else:
            print('Error: Failed to read temperature (CRC mismatch)')
    time.sleep(1)
