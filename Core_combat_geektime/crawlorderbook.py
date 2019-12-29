# -*- coding: UTF-8 -*-
import copy
import ssl
import time
import websocket
import json


class OrderBook(object):
    BIDS = "bid"
    ASKS = "ask"

    def __init__(self, limit=20):
        self.limit = limit
        # price amount
        self.bids = {}
        self.asks = {}
        self.bids_sorted = []
        self.asks_sorted = []

    def insert(self, price, amount, direction):
        if direction == self.BIDS:
            if price in self.bids:
                del self.bids[price]
            else:
                self.bids[price] = amount
        elif direction == self.ASKS:
            if amount == 0:
                if price in self.asks:
                    del self.asks[price]
            else:
                self.asks[price] = amount
        else:
            print("警告：不可知的 direction {}".format(direction))

    def sort_and_trucate(self):
        # sort
        self.bids_sorted = sorted([(price, amount) for price, amount in self.bids], reverse=True)
        self.asks_sorted = sorted([(price, amount) for price, amount in self.asks])

        # truncate
        self.bids_sorted = self.bids_sorted[:self.limit]
        self.asks_sorted = self.asks_sorted[:self.limit]

        # copy back to bids and asks
        self.bids = dict(self.bids_sorted)
        self.asks = dict(self.asks_sorted)

    def get_copy_of_bids_and_asks(self):

        return copy.deepcopy(self.bids_sorted), copy.deepcopy(self.asks_sorted)


class Crawler():
    def __init__(self, symbol, output_file):
        self.orderbook = OrderBook(limit=10)
        self.output_file = output_file
        self.ws = websocket.WebSocketApp("wss://api.gemini.com/v1/marketdata/{}".format(symbol),
                                         on_message=lambda ws, mesage: self.on_message(mesage))
        self.ws.run_forever(sslopt={"cert_reqs": ssl.CERT_NONE})

    def on_message(self, message):
        # 收到的信息进行处理，然后发给orderbook
        data = json.loads(message)
        for event in data["events"]:
            price, amount, directon = float(event["price"]), float(event["remaining"]), event["side"]
            self.orderbook.insert(price, amount, directon)

        # 整理orderbook,排序，只选取需要的前几个
        self.orderbook.sort_and_trucate()
        # 选取的结果，输出道文件
        with open(self.output_file, "a+") as f:
            bids, asks = self.orderbook.get_copy_of_bids_and_asks()
            output = {
                "bids": bids,
                "asks": asks,
                "ts": int(time.time() * 1000)
            }
            f.write(json.dumps(output) + "\n")


if __name__ == '__main__':
    crawler = Crawler(symbol="BTCUSD", output_file="BTCUSD.txt")
    # Crawler()
