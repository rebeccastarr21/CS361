#Receipt.py

import zmq

context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5555")

while True:
    #Receive request
    message = socket.recv_json()

    total = sum(message)

    print("Sending %.2f" % total)

    #Send reply
    socket.send_json(total)
