Mqtt communication protocol -TEST-
=======================

- sudo apt-add-repository ppa:mosquitto-dev/mosquitto-ppa
- sudo apt-get update
- sudo apt-get install mosquitto
- sudo apt-geet install mosquitto-clients

- run mosquitto -v to start the server, if it says that the port 1883 ( the default port is already in use it means it already started when the installation has finised )

- optional: nestat -at to check the ports status, it will list the ports in use and if the port 1883 is already there it should signal that the mosquitto server is running


- sudo apt-get install python3-pip
- pip3 install paho-mqtt

- run python3 subber.py, subber it is a script that listens to port 1883 and prints whatever the message has beeen sent through mqtt, it prints the message and then it will disconnect from the mqtt server

- run python3 server.py to send the desired message to the listener
