import minimalmodbus

instrument = minimalmodbus.Instrument("/dev/ttyUSB0", 49, debug=True)
instrument.serial.baudrate = 9600

print(instrument.read_register(7, 1))