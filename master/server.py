import paho.mqtt.client as mqtt
import random

def random_num():
	numere =""
	for i in range(2000):
		numere += str(random.randint(1,1000000)) + ","
	return numere

def send_data(data):
    client = mqtt.Client()
    client.connect("localhost", 1883, 60)
    #dumped = json.dumps(data, cls=NumpyEncoder)
    client.publish(data, random_num())
    client.disconnect()


#send_data("topic/test3")
send_data("topic/test1")
send_data("topic/test2")


