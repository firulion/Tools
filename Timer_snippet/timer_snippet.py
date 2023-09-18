import serial
import time

# Replace 'COMx' with your actual serial port (e.g., 'COM1' on Windows or '/dev/ttyUSB0' on Linux)
ser = serial.Serial('COM15', baudrate=38400, timeout=1)

previous_time = time.time()

print("_____START APPLICATION_____")
try:
    while True:
        data = ser.readline().decode('utf-8')  # Read and decode serial data
        current_time = time.time()
        time_interval = (current_time - previous_time)*1000
        
        if data:
            print(f"Received data: {data}")
            print(f"Time interval: {time_interval} ms")
            print("----------------\n______________")
            previous_time = current_time

except KeyboardInterrupt:
    ser.close()
    print("Serial communication terminated.")