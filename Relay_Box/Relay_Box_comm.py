import serial
import errno
import time
import logging

#define COM ports and devices
comRelayBox = 'COM17'
comMeter = 'COM15'
delay = 60
global comportRelayBox, comportMeter

#logging config
logging.basicConfig(filename='log.txt', format='%(asctime)s %(levelname)-8s %(message)s', level=logging.NOTSET)
logging.Formatter(fmt='%(asctime)s.%(msecs)03d', datefmt='%Y-%m-%d,%H:%M:%S')

def openportRelayBox():
    global comportRelayBox
    try:
        comportRelayBox = serial.Serial(port=comRelayBox, baudrate=38400, timeout=2, stopbits=serial.STOPBITS_ONE)
    except serial.SerialException as e:
        comportRelayBox = False
        logging.error("Error during RelayBox port openning: %s" % e)

def openportMeter():
    global comportMeter
    try:
        comportMeter = serial.Serial(port=comMeter, baudrate=9600, timeout=2, stopbits=serial.STOPBITS_ONE)
    except serial.SerialException as e:
        comportMeter = False
        logging.error("Error during Meter port openning: %s" % e)

def closeportRelayBox():
    global comportRelayBox
    comportRelayBox.close()

def closeportMeter():
    global comportMeter
    comportMeter.close()

def openRelayBox_ch1():
    global comportRelayBox
    if comportRelayBox is False:
        print("Relay box is not communicating, closing...")
        exit()
    try:
        comportRelayBox.write(b"\n\rROUTe:OPEN (@ 401)\n\r")
        logging.info("Relay open")
    except serial.SerialException as e:
        logging.error("Error during open cmd RelayBox_ch1: %s" % e)

def closeRelayBox_ch1():
    global comportRelayBox
    try:
        comportRelayBox.write(b"\n\rROUTe:CLOSE (@ 401)\n\r")
        logging.info("Relay close")
    except serial.SerialException as e:
        logging.error("Error during close cmd RelayBox_ch1: %s" % e)

def DataReadMeter():
    global comportMeter
    if comportMeter is False:
        print("Meter is not communicating, closing...")
        exit()
    try:
        data = comportMeter.readline()
        logging.info(data)
        if data:
            return data
    except serial.SerialException as e:
        logging.error("Error during Meter data read: %s" % e)


if __name__ == '__main__':
    Module_start = "[MODULE START STRING]"        # Variable to check if module has started properly
    openportRelayBox()
    openportMeter()
    print('Test Start.....')

    for aux in range(1000):
        pre_time = time.time()
        openRelayBox_ch1()
        print('Relay open')
        Comm_data = DataReadMeter()
        while Module_start not in Comm_data:
            cur_time = time.time()
            print(data)
            Comm_data = DataReadMeter()

        print(cur_time-pre_time)
        logging.info(data)
        closeRelayBox_ch1()
        print('Relay close')
        sleep(delay)

        logging.info("iteration: %d" % aux)
        print("iteration: %d" % aux)

    closeportRelayBox()
    closeportMeter()