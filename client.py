import socket
import threading

username = input("Ingrese un nombre de usuario: ")

host = '200.13.4.198'
port = 55555

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((host, port))

def receive_messages():
 while True:
     try:
         message=client.recv(1024).decode('utf-8')

         if message == "@username":
            client.send(username.encode("utf-8"))
         else:
                 print(message)
     except:
         print("Error")
         client.close
         break

def write_message():
    while True:
        message = f"{username}: {input('')}"
        client.send(message.encode('utf-8'))

recive_thread= threading.Thread(target=receive_messages)
recive_thread.start()

write_thread= threading.Thread(target=write_message)
write_thread.start()
