import serial
import time

def superLectura():
    def read_rfid():
        ser = serial.Serial('COM8', 9600)
        time.sleep(2)  # Espera 2 segundos para establecer la conexión

        data = b''  # Usa un objeto de bytes en lugar de un string
        while True:
            try:
                if ser.inWaiting() > 0:
                    char = ser.read()  # Lee un byte (objeto bytes)
                    if char == b'\r':
                        rfid_data = data.decode('utf-8')  # Decodifica data para obtener el ID de la tarjeta
                        ser.close()  # Cierre de la conexión serial
                        return rfid_data
                    else:
                        data += char  # Concatena char directamente (objeto bytes)

            except serial.SerialException as e:
                print("Error de comunicación serial:", e)
                break

        ser.close()
        return None  # Retorna None si no se ha leído ninguna tarjeta RFID

    # Uso de la función para obtener el ID de la tarjeta RFID
    try:
        while True:
            rfid_id = read_rfid()
            if rfid_id:
                print("RFID leído:", rfid_id)
                return rfid_id
    except KeyboardInterrupt:
        pass

# Llamada al método superLectura
superLectura()