# -*- coding: utf-8 -*-
from tornado import gen
from tornado.ioloop import IOLoop
from tornado.iostream import StreamClosedError
from tornado.tcpclient import TCPClient
# from tornado.options import options

tcp_client = TCPClient()

async def listen():
    try:
        stream = await tcp_client.connect('localhost', 8889)

        while True:
            # print('aa')
            response = await stream.read_until(b"\r\n")
            response = response.decode('utf-8').rstrip('\r\n')
            print('response: {}'.format(response))
    except StreamClosedError:
        print("Server is unavailable.")
        # stream.close()
    # except KeyboardInterrupt:
    #     print("Listener is killed.")
    #     stream.close()


if __name__ == '__main__':
    # options.parse_command_line()
    print("Listener start.")
    IOLoop.current().run_sync(listen)