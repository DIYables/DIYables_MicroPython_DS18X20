## MicroPython DS18X20 Library - DIYables_MicroPython_DS18X20
This MicroPython DS18X20 library is designed for any hardware plaform that supports MicroPython such as Raspberry Pi Pico, ESP32, Micro:bit... to make it easy to use with DS18B20 Temperature Sensor. It is easy to use for not only beginners but also experienced users... 

For some devices, the MicroPython firmware does not include support for the `DS18X20` module, so this library was created to provide compatibility for these devices. It is created by DIYables to work with DIYables DS18B20 Temperature Sensor, but also work with DS18X20 products from other brands. Please consider purchasing products from [DIYables Store on Amazon](https://amazon.com/diyables) to support our works.



Features
----------------------------
* Works with any hardware plaform that supports MicroPython such as Raspberry Pi Pico, ESP32, Micro:bit...

Product Link
----------------------------
* [DS18B20 Temperature Sensor](https://diyables.io/products/ds18b20-one-wire-temperature-sensor)
* [DS18B20 Temperature Sensor with adapter](https://diyables.io/products/ds18b20-temperature-sensor)
* [Sensor Kit](https://diyables.io/products/sensor-kit)



Available Functions
----------------------------
* \_\_init\_\_(onewire)
* scan()
* def convert_temp()
* read_temp(address)
* def wait_for_conversion()



Available Examples
----------------------------
* main.py



Tutorials
----------------------------
* [Arduino MicroPython - DS18B20 Temperature Sensor](https://newbiely.com/tutorials/arduino-micropython/arduino-micropython-temperature-sensor)


Note that for some devices, the MicroPython firmware already includes support for the `DS18X20` module, so you may not need to use this custom library. For example:
* [Raspberry Pi Pico - DS18B20 Temperature Sensor](https://newbiely.com/tutorials/raspberry-pico/raspberry-pi-pico-temperature-sensor)
* [ESP32 MicroPython - DS18B20 Temperature Sensor](https://newbiely.com/tutorials/esp32-micropython/esp32-micropython-temperature-sensor)



References
----------------------------
* [MicroPython DS18X20 Library](https://newbiely.com/tutorials/micropython/micropython-ds18x20-library)
