import json
import websocket
import gzip
import io

URL = "wss://api.wallex.ir/ws"
# CHANNEL = ["subscribe", {"channel": "BTCTMN@marketCap"}]
CHANNEL = ["subscribe", {"channel": "USDTTMN@sellDepth"}]

# URL = "wss://stream.binance.com/stream"
# CHANNEL = {"method":"SUBSCRIBE", "params": ["btcusdt@kline_1m"], "id":3}
# CHANNEL = {"method":"SUBSCRIBE", "params": ["!ticker@arr"]}


class Test(object):

    def __init__(self):
        self.url = URL
        self.ws = None

    def on_open(self, ws):
        print('WebSocket connected')
        subStr = json.dumps(CHANNEL)
        ws.send(subStr)
        print("Subscribed to :", subStr)

    def on_data(self, ws, string, type, continue_flag):
        pass

    def on_message(self, ws, message):
        message = json.loads(message)
        print(message)

    def on_error(self, ws, error):
        print(error)

    def on_close(self, ws, close_status_code, close_msg):
        print('The connection is closed!')

    def start(self):
        self.ws = websocket.WebSocketApp(
            self.url,
            on_open=self.on_open,
            on_message=self.on_message,
            # on_data=self.on_data,
            on_error=self.on_error,
            on_close=self.on_close,
        )
        self.ws.run_forever()


if __name__ == "__main__":
    test = Test()
    test.start()
