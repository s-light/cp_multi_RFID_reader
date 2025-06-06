# SPDX-FileCopyrightText: 2021 Carter Nelson for Adafruit Industries
# SPDX-License-Identifier: MIT

# https://github.com/adafruit/Adafruit_CircuitPython_TCA9548A/blob/main/examples/tca9548a_simpletest.py

# This example shows using TCA9548A to perform a simple scan for connected devices
import board
import busio

import adafruit_tca9548a

# Create I2C bus as normal
# i2c = board.I2C()  # uses board.SCL and board.SDA
# i2c = board.STEMMA_I2C()  # For using the built-in STEMMA QT connector on a microcontroller
i2c = busio.I2C(board.GP1, board.GP0)  # Pi Pico RP2040


# Create the TCA9548A object and give it the I2C bus
tca = adafruit_tca9548a.TCA9548A(i2c)

for channel in range(8):
    if tca[channel].try_lock():
        print(f"Channel {channel}:", end="")
        addresses = tca[channel].scan()
        print([hex(address) for address in addresses if address != 0x70])
        tca[channel].unlock()
