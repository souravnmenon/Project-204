import socket
from threading import Thread

SERVER = None
IP_ADDRESS = "127.0.0.1"
PORT = 6000

CLIENTS = {}

def setup():
  print("\n\t\t\t\t\t*** Welcome To Tambola Game ***\n")

  global SERVER, IP_ADDRESS, PORT

  SERVER = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  SERVER.bind((IP_ADDRESS, PORT))

  SERVER.listen(10)

def acceptConnections():
  global SERVER
  global CLIENTS

  while True:
    playerSocket, addr = SERVER.accept()
    playerName = playerSocket.recv(1024).decode().strip()
    print(playerName)

    if (len(CLIENTS.keys()) == 0):
      CLIENTS[playerName] = {"player_type": "player1"}
    else:
      CLIENTS[playerName] = {"player_type": "player2"}

    CLIENTS[playerName]["player_socket"] = playerSocket
    CLIENTS[playerName]["address"] = addr
    CLIENTS[playerName]["player_name"] = playerName
    CLIENTS[playerName]["turn"] = False

    print(f"Connection established with {playerName} : {addr}")