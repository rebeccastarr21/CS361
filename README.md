# Microservice A
Receives a list of numbers, adds the numbers together, then returns the total.

### Code to create a socket

*import zmq
<br>context = zmq.Context()
<br>socket = context.socket(zmq.REQ)
<br>socket.connect("tcp://localhost:5555")*

Add the above code to the top of your program.

### Code to request data from the service

*socket.send_json(message)*

"message" should be a list of numbers

### Code to Receive data from the service

*response = socket.recv_json()*

[UML Diagram](https://lucid.app/lucidchart/cc05a18c-e68f-4684-8d77-bed9e10143cf/edit?viewport_loc=-52%2C-268%2C2155%2C1059%2C0_0&invitationId=inv_29954952-7e21-4268-aa3e-1cb3452a8962)

![image](https://github.com/rebeccastarr21/CS361/assets/55964395/d8679d17-2d4d-4eeb-8910-aa0c11fc3d33)
