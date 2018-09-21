import socket
import threading
from game2 import Game2
import json
s= socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind(('localhost', 50000))
s.listen(4)
# conn:add
connAddDic={}
while 1:
    try:
        conn,add = s.accept()
        if conn in connAddDic.keys():
            print("in",add)
        else:
            print("not in")
            print(conn)
            print(add)
            connAddDic.update({conn:add})
        data=''
        while 1:
            tmpdata=conn.recv(1024)
            if not tmpdata:
                print("data recived")
                break
            data+=tmpdata.decode("utf-8")
            if len(tmpdata.decode("utf-8")) < 1024:
                break
            print("1.2")
        matn = json.loads(data)
        print(matn)
        newgame = Game2(55)
        gameID = newgame.gameID
        matn = {"gameID":gameID}
        print(matn)
        b = json.dumps(matn).encode('utf-8')
        conn.send(b)


    except Exception as e:
        print(getattr(e, 'message', repr(e)))