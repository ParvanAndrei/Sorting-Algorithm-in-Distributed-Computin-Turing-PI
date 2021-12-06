import paho.mqtt.client as mqtt
import time
import heap_sort
import merge_sort

array = []
array2 = []
i=0
time1 = 0
time2 = 0
def on_connect(client, userdata, flags, rc):
	print("Connected with result code "+str(rc))
	client.subscribe("topic/test")

def on_message(client, userdata, msg):
	numere = msg.payload.decode()
	#print("datele primite")
	#print(numere)
	global i
	i += 1
	global array
	global array2
	global time1
	global time2
	if i == 1:
		arr = numere.split(",")
		time1 = float(arr[0])
		for j in range(1,len(arr)):
			try:
				array.append(int(arr[j]))
			except:
				pass
		#print("array1")
		#print(time1)
	elif i == 2:
		arr2 = numere.split(",")
		time2 = float(arr2[0])
		for k in range(1,len(arr2)):
			try:
				array2.append(int(arr2[k]))
			except:
				pass
		#print("array2:")
		#print(array2)
		start_time=time.time()
		final_array = array + array2
		raspuns = merge_sort.mergeSort(final_array)
		time_stack_final = time.time()-start_time
		print("response:")
		print(raspuns)
		full_time=time_stack_final+time1 + time2
		print("time: %s" % (full_time))
		client.disconnect()


client = mqtt.Client()
client.connect("localhost", 1883, 60)
client.on_connect = on_connect
client.on_message = on_message

client.loop_forever()
