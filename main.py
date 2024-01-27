# import serial.tools.list_ports
import random
import time
import  sys
from  Adafruit_IO import  MQTTClient

AIO_FEED_IDs = ["sensor1","sensor2","sensor3","button1","button2","ai"]
AIO_USERNAME = "leductai"
AIO_KEY = ""

def  connected(client):
    print("Ket noi thanh cong...")
    for topic in AIO_FEED_IDs:
        client.subscribe(topic)

def  subscribe(client , userdata , mid , granted_qos):
    print("Subscribe thanh cong...")

def  disconnected(client):
    print("Ngat ket noi...")
    sys.exit (1)

def  message(client , feed_id , payload):
    print("Nhan du lieu: " + payload + ", Feed ID :" + feed_id )
    # ser.write((str(payload) + "#").encode())


# def getPort():
#     ports = serial.tools.list_ports.comports()
#     N = len(ports)
#     commPort = "None"
#     for i in range(0, N):
#         port = ports[i]
#         strPort = str(port)
#         if "USB Serial Device" in strPort:
#             splitPort = strPort.split(" ")
#             commPort = (splitPort[0])
#     return commPort

# ser = serial.Serial( port=getPort(), baudrate=115200)
# ser = serial.Serial('COM3', 115200)
# if not ser.isOpen():
#     ser.open()
#     print('com3 is open', ser.isOpen())
client = MQTTClient(AIO_USERNAME , AIO_KEY)
client.on_connect = connected
client.on_disconnect = disconnected
client.on_message = message
client.on_subscribe = subscribe
client.connect()
client.loop_background()
counter = 10
while True:
    counter -= 1
    if counter <= 0:
        counter = 10
        temp = random.randint(0, 70)
        print("Cap nhat nhiet do:", temp)
        client.publish("sensor1", temp)
        humi = random.randint(40, 70)
        print("Cap nhat do am:", humi)
        client.publish("sensor2", humi)
        light = random.randint(200, 400)
        print("Cap nhat anh sang:", light)
        client.publish("sensor3", light)
    time.sleep(1)
    pass