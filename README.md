# Socket Programming

# Requirements:

- Python installed on your system.

# Setting up the Environment:

1. Make sure you have the Python client and server files ready to be executed.
2. Ensure that you have a network connection available between the client and server if they are on different machines.
3. If you are using different machines, use the IP address connected to the network.

# Running the Server:

1. Open the terminal or command prompt.
2. Navigate to the directory that contains the Python server file using the `cd` command, for example:

   ```
   cd socket-python
   ```

3. Next, execute the server file using the following command:

   **UDP:**

   ```
   python udp_server.py
   ```

   **TCP:**

   ```
   python tcp_server.py
   ```

   The Python server will start and begin listening for UDP packets or TCP client connections, depending on the file you executed.

# Running the Client:

1. Open another terminal or command prompt. Make sure it is on a different machine from the server if possible, or open 2 terminals or command prompts.
2. Navigate to the directory that contains the Python client file using the `cd` command, for example:

   ```
   cd www/networking/socket/python
   ```

3. Next, execute the Python client file using the following command:

   **UDP:**

   ```
   python udp_client.py
   ```

   **TCP:**

   ```
   python tcp_client.py
   ```

   The Python client will connect to the server and initiate communication.

# Communication between Client and Server:

- After running the client and server, the communication between them will be established.
- Check the available files: small.txt, medium.txt, large.txt.
- Enter the name of the file you want to receive.
- Finally, a brief description of your request will appear on the screen.

# Ending the Execution:

- To terminate the client or server, you can press `Ctrl + C` in the terminal where they are running, or type 'bye' to exit the application.
- Make sure to terminate the server before closing the client.
