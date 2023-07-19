import serial


import serial
import time

# Configuración del puerto serial
port = '/dev/ttyACM0'  # Reemplaza '/dev/ttyACM0' con el puerto correspondiente a tu Arduino
baudrate = 9600

# Conexión al puerto serial
ser = serial.Serial(port, baudrate)
time.sleep(2)  # Espera 2 segundos para establecer la conexión

def read_rfid():
    data = ''
    while True:
        if ser.inWaiting() > 0:
            char = ser.read().decode('utf-8')
            if char == '\r':
                return data
            else:
                data += char

# Ciclo principal
while True:
    rfid_data = read_rfid()
    print("RFID leído: ", rfid_data)

ser.close()