import paho.mqtt.client as mqtt
import json
import numpy as np

class NumpyEncoder(json.JSONEncoder):
    """ Special json encoder for numpy types """
    def default(self, obj):
        if isinstance(obj, np.integer):
            return int(obj)
        elif isinstance(obj, np.floating):
            return float(obj)
        elif isinstance(obj, np.ndarray):
            return obj.tolist()
        return json.JSONEncoder.default(self, obj)



def send_data(data):
    client = mqtt.Client()
    client.connect("localhost", 1883, 60)
    #dumped = json.dumps(data, cls=NumpyEncoder)
    client.publish("topic/test", "2,5")
    client.disconnect()


send_data(1)
