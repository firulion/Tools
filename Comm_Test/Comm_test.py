import socket
import csv
import time
from time import sleep
import logging

import socket
import csv
import time
from time import sleep
import logging

# TCP information
host = "[HOST]"
port = "[PORT]"

# Logging config
logging.basicConfig(filename='/files/log.txt', format='%(asctime)s %(levelname)-8s %(message)s', level=logging.NOTSET)
logging.Formatter(fmt='%(asctime)s.%(msecs)03d', datefmt='%Y-%m-%d,%H%M%S')
global flag


def loadCSV()
    global csvreader
    with open('/files/commands.csv', 'r') as file
        csvreader = file.readlines()

def send(aux)
    try
        client_socket.send(bytes.fromhex(aux))
    except socket.error as e
        logging.error(Error during message send process %s % e)

def receive()
    global flag
    flag = 0
    er_count = 0
    try
        er_count = 0
        return client_socket.recv(1024)  # receive response
        flag = 0
    except (ConnectionResetError, socket.timeout) as e
        err = e.args[0]
        if err == 'timed out'
            logging.error("Connection timed out!")
            print("Time out to receive")
            er_count = 0
            closeCONN()
            print("Timed out, restarting connection.")
            openCONN()
        else
            logging.error("Host closed connection!")
            print(e)
            print("Host closed connection")
            flag = 1
            er_count = er_count + 1
            time.sleep(60)
            if er_count = 10
                print("Communication error, restarting connection")
                closeCONN()
                time.sleep(300)
                openCONN()

def closeCONN()
    try
        client_socket.close()  # close the connection
    except socket.error as e
        logging.error("Error during close connection %s" % e.args[0])
    print("...End connection")

def openCONN()
    global client_socket #socket configuration
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # instantiate

    try
        client_socket.connect((host, port))  # connect to the server
    except socket.error as e
        logging.error("Error during open connection %s" % e.args[0])

    logging.info("Communication start sucess!")
    client_socket.setblocking(False)
    client_socket.settimeout(10)
    print(Start connection...)

def DOT()
    send(csvreader[1].split(',')[1]) # send DOT
    print("Sending DOT")
    logging.info("Send command %s" % csvreader[1].split(',')[0])
    time.sleep(2)

# Specific functions for the commands______________________________
def send_command(n)
    global flag
    send(csvreader[n].split(',')[1]) # send Command n
    logging.info("Send command %s" % csvreader[n].split(',')[0])
    aux = receive()
    i = 0
    while aux is None
        i = i + 1
        send(csvreader[n].split(',')[1])
        aux = receive()
        if flag == 1 or i == 2
            i = 0
            flag = 0
            logging.error(f"Reset connection and send command again!!!")
            closeCONN()
            print("Restarting connection in 5 minutes...")
            time.sleep(240)
            print("1 min remaining...")
            time.sleep(60)
            openCONN()
    aux = aux.hex()
    print(f"Sending command {csvreader[n].split(',')[0]}...")
    logging.info("Received response %s" % aux)
    if (aux[03] in csvreader[n+1].split(',')[1]) and (len(aux) == 516) # Compare response to standard ACK response frame
        logging.info(f"Response received is OK!")
        DOT()
    else
        print(aux[03])
        print(csvreader[n+1].split(',')[1])
        logging.critical(f"Response received does not match expectation!!!")


if __name__ == '__main__'
    global flag
    count = 0
    i = 0
    comando = 2
    openCONN()
    # Load commands and send based on commands_V01.csv file 
    loadCSV()
    while True
        count = count + 1
        send_command(comando)
        comando = comando + 2
        if comando  10
            comando = 2
        time.sleep(3)
        print("---  Next cycle   ---")
        if flag == 1 or count == 4
            count = 0
            closeCONN()
            print("Restarting connection for functionality issue!n10 minutes remaining ")
            time.sleep(300)
            print("5 minutes remaining")
            time.sleep(300)
            openCONN()

closeCONN()