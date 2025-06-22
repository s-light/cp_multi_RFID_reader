# cp_multi_RFID_reader
simple test for multiple PN532 RFID-readers via I2C multiplexer

## hw
- [PN532 RFID reader](https://funduinoshop.com/elektronische-module/wireless-iot/rfid-nfc/pn532-nfc-rfid-v3-modul-fuer-arduino-und-co)
    - contains 
        . `RFID Card` 
        . `RFID keyfob` 
- [8mm mini RFID tag (NTAG213](https://funduinoshop.com/elektronische-module/wireless-iot/rfid-nfc/nfc-rfid-tag-mini-ntag213-oe-8mm)
- [RFID Coin Tag weiß NXP MIFARE Classic 1K 4-byte-UID 35mm x 0,9 Anti metal (13,56MHz)](https://www.zutrittsshop.de/de/rfid-tags-sonstige/rifd-tags-sonstige-lager/RFID-coin-tag-mifare-1k-anti-metal.html)
- [RFID Chip Platine weiß NXP MIFARE Classic 1K 4b (13,56MHz) 18mm x 12mm x 1mm](https://www.zutrittsshop.de/de/rfid-tags-sonstige/rifd-tags-sonstige-lager/RFID-chip-Platine-mifare-classic-1k.html)
- [RFID Token Ring / Scheibe schwarz TK4100 30mm x 4mm (125KHz)](https://www.zutrittsshop.de/de/rfid-tags-sonstige/rifd-tags-sonstige-lager/RFID-Token-scheibe-Tk4100-125KHz.html)
- [RFID KeyFob Evolution NXP MIFARE Classic 1K 4 byte (13,56MHz)](https://www.zutrittsshop.de/de/rfid-transponder/karten-und-tags/keyfob-evolution-mifare-classic-1k.html)
- [I2C multiplexer (TCA9548A)](https://funduinoshop.com/elektronische-module/schnittstellen-konverter/signalwandler/tca9548a-i2c-multiplexer)

![simple test-setup](<20250604_084520 small.jpg>)

### PN532 module
Size:
- width 41 mm
- length 43 mm
- height 5 mm

### reading range tests

| material            | 8mm NTAG213 | 35mm Coin | Chip PCB | Token 30mm | keyfob evolution | Card | keyfob |
| ------------------- | ----------- | --------- | -------- | ---------- | ---------------- | ---- | ------ |
| cardboard 1mm       |             |           |          |            |                  |      |        |
| plywood birch 0.8mm |             |           |          |            |                  |      |        |
| plywood birch 2mm   |             |           |          |            |                  |      |        |
| plywood birch 4bmm  |             |           |          |            |                  |      |        |