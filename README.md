#Microservice A
//Receives a list of numbers, adds the numbers together, then returns the total.

//Code to create a socket

import zmq
context = zmq.Context()
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:5555")

Add this code to the top of your program:


//Code to request data from the service:

socket.send_json(message)

"message" should be a list of numbers


//Code to Receive data from the service:

response = socket.recv_json()
