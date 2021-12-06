import paho.mqtt.client as mqtt
import time
import heap_sort
import server


def on_connect(client, userdata, flags, rc):
	print("Connected with result code "+str(rc))
	client.subscribe("topic/test2")

def on_message(client, userdata, msg):
	numere = msg.payload.decode()
	array = []
	for i in numere.split(","):
		try:
			array.append(int(i))
		except:
			pass
	start_time = time.time()
	array = heap_sort.heap_sort(array)
	time_stack = time.time()-start_time
	#print("--------%s seconds ------------" % (time_stack))
	#client.disconnect()
	numere2 = ""
	numere2 += str(time_stack) + ","
	for i in array:
		numere2 += str(i) + ","
	server.send_data(numere2)

client = mqtt.Client()
client.connect("192.168.0.8", 1883, 60)
client.on_connect = on_connect
client.on_message = on_message

client.loop_forever()
