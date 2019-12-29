# -*- coding: UTF-8 -*-
import ssl
import websocket
import json
count=5
def on_message(ws,message):
    # print(json.loads(message))
    print(message)
    global count
    count-=1
    print(count)
    if count==0:
        ws.close()

if __name__=='__main__':
    ws=websocket.WebSocketApp("wss://api.gemini.com/v1/marketdata/btcusd?top_of_book=true&offers=true",on_message=on_message)
    ws.run_forever(sslopt={"cert_reqs":ssl.CERT_NONE})



