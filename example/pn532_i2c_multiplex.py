# SPDX-FileCopyrightText: 2025 Stefan Krüger s-light.eu
# SPDX-License-Identifier: MIT


# based on
# https://github.com/adafruit/Adafruit_CircuitPython_TCA9548A/blob/main/examples/tca9548a_simpletest.py
# SPDX-FileCopyrightText: 2021 Carter Nelson for Adafruit Industries
# SPDX-License-Identifier: MIT
# https://github.com/adafruit/Adafruit_CircuitPython_TCA9548A/blob/main/examples/tca9548a_multisensor.py
# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT

import time
import board
import busio

import adafruit_tca9548a

# Create I2C bus as normal
# i2c = board.I2C()  # uses board.SCL and board.SDA
# i2c = board.STEMMA_I2C()  # For using the built-in STEMMA QT connector on a microcontroller
i2c = busio.I2C(board.GP1, board.GP0)  # Pi Pico RP2040

from adafruit_pn532.i2c import PN532_I2C

# Create the TCA9548A object and give it the I2C bus
tca = adafruit_tca9548a.TCA9548A(i2c)

for channel in range(8):
    if tca[channel].try_lock():
        print(f"Channel {channel}:", end="")
        addresses = tca[channel].scan()
        print([hex(address) for address in addresses if address != 0x70])
        tca[channel].unlock()

pn532_list = [
    PN532_I2C(tca[0], debug=False),
    PN532_I2C(tca[1], debug=False),
    PN532_I2C(tca[2], debug=False),
    PN532_I2C(tca[3], debug=False)
]


for i, pn532 in enumerate(pn532_list):
    ic, ver, rev, support = pn532.firmware_version
    print(f"{i} Found PN532:")
    print(f"  firmware version: {ver}.{rev}")
    print(f"  ic: {ic}")
    print(f"  support: {support}")
    # Configure PN532 to communicate with MiFare cards
    pn532.SAM_configuration()
    # Start listening for a card
    pn532.listen_for_passive_target()

# After initial setup, can just use sensors as normal.
while True:
    for i, pn532 in enumerate(pn532_list):
        # # Check if a card is available to read
        # if irq_pin.value == 0:
        # uid = pn532.get_passive_target()
        # for now we have no irq pin. therefore we are polling..
        uid = pn532.get_passive_target(timeout=0.001)
        if uid:
            print(f"{i} Found card with UID:", [hex(i) for i in uid])
            # Start listening for a card again
            pn532.listen_for_passive_target()
    # time.sleep(0.01)
