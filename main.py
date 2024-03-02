# import serial.tools.list_ports
import random
import time
import  sys
from  Adafruit_IO import  MQTTClient
from simple_ai import *
# from uart import*

AIO_FEED_IDs = ["sensor1","sensor2","sensor3","button1","button2","ai"]
AIO_USERNAME = "leductai"
AIO_KEY = "aio_yfTv42StYhbWDexwpGwmx09bYnAU"

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


client = MQTTClient(AIO_USERNAME , AIO_KEY)
client.on_connect = connected
client.on_disconnect = disconnected
client.on_message = message
client.on_subscribe = subscribe
client.connect()
client.loop_background()
counter = 10
counter_ai = 5
ai_result = ""
previous_ai = ""
while True:
    # counter -= 1
    # if counter <= 0:
    #     counter = 10
    #     temp = random.randint(0, 70)
    #     print("Cap nhat nhiet do:", temp)
    #     client.publish("sensor1", temp)
    #     humi = random.randint(40, 70)
    #     print("Cap nhat do am:", humi)
    #     client.publish("sensor2", humi)
    #     light = random.randint(200, 400)
    #     print("Cap nhat anh sang:", light)
    #     client.publish("sensor3", light)

    counter_ai -= 1
    if counter_ai <= 0:
        counter_ai = 5
        ai_result = image_detector()
        if ai_result != previous_ai :
            client.publish("ai" , ai_result)
            previous_ai = ai_result
        print("AI output : ", ai_result)
    
    # readSerial(client)


    time.sleep(1)
    pass