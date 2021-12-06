import paho.mqtt.client as mqtt

def send_data(data):
    client = mqtt.Client()
    client.connect("192.168.0.8", 1883, 60)
    client.publish("topic/test", data)
    client.disconnect()


