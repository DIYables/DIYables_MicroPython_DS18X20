"""
This MicroPython library is designed for any hardware plaform that supports MicroPython such as Raspberry Pi Pico, ESP32, Micro:bit... to make it easy to use with DS18B20 Temperature Sensor

It is created by DIYables to work with DIYables products, but also work with products from other brands. Please consider purchasing products from [DIYables Store on Amazon](https://amazon.com/diyables) from to support our work.

Product Link:
- DS18B20 Temperature Sensor: https://diyables.io/products/ds18b20-temperature-sensor
- DS18B20 Temperature Sensor (without adapter): https://diyables.io/products/ds18b20-one-wire-temperature-sensor
- Sensor Kit: https://diyables.io/products/sensor-kit


Copyright (c) 2024, DIYables.io. All rights reserved.

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions
are met:

- Redistributions of source code must retain the above copyright
  notice, this list of conditions and the following disclaimer.

- Redistributions in binary form must reproduce the above copyright
  notice, this list of conditions and the following disclaimer in the
  documentation and/or other materials provided with the distribution.

- Neither the name of the DIYables.io nor the names of its
  contributors may be used to endorse or promote products derived from
  this software without specific prior written permission.

THIS SOFTWARE IS PROVIDED BY DIYABLES.IO "AS IS" AND ANY EXPRESS OR
IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
DISCLAIMED. IN NO EVENT SHALL DIYABLES.IO BE LIABLE FOR ANY DIRECT,
INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
(INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION)
HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT,
STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING
IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
POSSIBILITY OF SUCH DAMAGE.
"""

from machine import Pin
import time
import onewire

class DS18X20:
    def __init__(self, ow):
        """
        Initialize the DS18X20 class with a OneWire bus object.
        
        :param ow: OneWire bus object
        """
        self.ow = ow
        self.roms = []

    def scan(self):
        """
        Scan for DS18B20 devices on the OneWire bus.

        :return: List of ROM addresses of the DS18B20 devices found
        """
        self.roms = self.ow.scan()
        return self.roms

    def convert_temp(self):
        """
        Start temperature conversion on all DS18B20 devices on the bus.
        """
        for rom in self.roms:
            self.ow.reset()
            self.ow.select_rom(rom)
            self.ow.writebyte(0x44)  # Start temperature conversion

    def read_temp(self, rom):
        """
        Read the temperature from a specific DS18B20 device.

        :param rom: ROM address of the DS18B20 device
        :return: Temperature in Celsius
        """
        self.ow.reset()
        self.ow.select_rom(rom)
        self.ow.writebyte(0xBE)  # Read scratchpad command
        
        # Read 9 bytes of scratchpad data
        data = bytearray(9)
        for i in range(9):
            data[i] = self.ow.readbyte()
        
        # Check CRC (Cyclic Redundancy Check) to ensure data integrity
        if self.crc8(data[:8]) != data[8]:
            return None  # Return None if CRC check fails
        
        # Calculate temperature from scratchpad data
        temp_lsb = data[0]
        temp_msb = data[1]
        temp = (temp_msb << 8 | temp_lsb) / 16.0
        
        return temp

    def wait_for_conversion(self):
        """
        Wait for the conversion to complete.
        """
        # Wait 750 ms (maximum conversion time for 12-bit resolution)
        time.sleep_ms(750)

    def crc8(self, data):
        """
        Compute the CRC-8 of the given data using the polynomial 0x31 (x^8 + x^5 + x^4 + 1).
        
        :param data: Data to compute CRC on
        :return: CRC-8 value
        """
        crc = 0
        for byte in data:
            crc ^= byte
            for _ in range(8):
                if crc & 0x01:
                    crc = (crc >> 1) ^ 0x8C
                else:
                    crc >>= 1
        return crc

