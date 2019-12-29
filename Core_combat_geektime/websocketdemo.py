# -*- coding: UTF-8 -*-
import websocket
import threading
import time
def on_message(ws,message):
    print("received："+message)

def on_open(ws):
    def gao():
        for i in range(5):
            time.sleep(0.01)
            msg="{0}".format(i)
            ws.send(msg)
            print("Sent: "+msg)
        #休息1秒用于接收服务器回复的消息
        time.sleep(1)
        ws.close()
        print("websocket 关闭连接")
    t=threading.Thread(target=gao,name="gao")
    t.start()

if __name__=='__main__':
    # websocket.enableTrace(True)
    ws = websocket.WebSocketApp("ws://echo.websocket.org/",on_message=on_message,on_open=on_open)
    # ws.on_open = on_open
    ws.run_forever()