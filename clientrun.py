import socket
import json
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('localhost', 50000))
matn ={"askgame":2}
b = json.dumps(matn).encode('utf-8')
s.sendall(b)
data=''
while 1:
    tmpdata=s.recv(1024)
    if not tmpdata:
        print("data recived")
        # wcondition=False
        break
    data += tmpdata.decode("utf-8")
    if len(tmpdata.decode("utf-8")) < 1024:
        break
print(data)
ack = json.loads(data)
print(ack['gameID'])
if "gameID" in ack.keys():
    gameID = ack["gameID"]
    print("gameID",gameID)

s.close()

