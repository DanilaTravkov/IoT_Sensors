import paho.mqtt.client as mqtt

def on_connect(client, userdata, flags, reasonCode, properties):
    print("Connected:", reasonCode)
    client.subscribe("smarthome/#")

def on_message(client, userdata, msg):
    print(msg.topic, msg.payload.decode())

client = mqtt.Client(protocol=mqtt.MQTTv5)
client.on_connect = on_connect
client.on_message = on_message
client.connect("host.docker.internal", 1883)
client.loop_forever()
