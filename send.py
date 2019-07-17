import paho.mqtt.client as mqtt

def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    client.subscribe("#")

def on_message(client, userdata, msg):
    print(" msg.topic+" +str(msg.payload))

client = mqtt.Client()
client.on_connect = on_connect
client.connect("192.168.1.5", 1883, 60)

while True:
    message = input('your message: ')
    client.publish('gc/elvis' , message)



