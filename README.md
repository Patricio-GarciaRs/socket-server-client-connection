
# Project Title

This is a simple socket server - client connection to start understanding the socket package from Python.

Here we can initiate a server within the terminal with the following command:

```
python3 ./server.py
```

This will create a server that can accept all the request connections from the clients.

To initiate a client connection, type the following command in the terminal:
```
python3 ./client.py
```

This will create a connection with the server and it will allow you to send messages to the server as well as close the connection with the server.

You can create multiple connections to the server open several terminals and initiate the client file again. This is managed using threads of python and registering them in an array to have the posibility to close all connections at once as well as the main thread.

I will also look to implement several updates for the functionality of the server and maybe create a chat between the clients and manage the server with several functions to remove a certain client or send personalized messages to all clients or one in particular.

