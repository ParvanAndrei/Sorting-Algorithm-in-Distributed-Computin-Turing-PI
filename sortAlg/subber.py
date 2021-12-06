import paho.mqtt.client as mqtt
import time
import heap_sort
import server

def random_num():
        numere =""
        for i in range(4000):
                numere += str(random.randint(1,1000000)) + ","
        return numere


def on_connect(client, userdata, flags, rc):
	print("Connected with result code "+str(rc))
	client.subscribe("topic/test3")

def on_message(client, userdata, msg):
	numere = msg.payload.decode()
	array = []
	for i in numere.split(","):
		try:
			array.append(int(i))
		except:
			pass
	#start_time = time.time()
	#array = heap_sort.heap_sort(array)
	#time_stack = time.time()-start_time
	#print("--------%s seconds ------------" % (time_stack))
	#client.disconnect()
	numere2 = ""
	numere2 += str(time_stack) + ","
	for i in array:
                numere2 += str(i) + ","
	usorted = random_num()
	server.send_data(usorted)

client = mqtt.Client()
client.connect("192.168.0.8", 1883, 60)
client.on_connect = on_connect
client.on_message = on_message

client.loop_forever()
