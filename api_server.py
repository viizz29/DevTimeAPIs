import tornado.ioloop
import tornado.web
import asyncio
import threading
import tornado.iostream
import tornado.httpserver
import tornado.websocket
import tornado.ioloop
import tornado.web
import tornado.iostream


class APIServer:
    def __init__(self, port,apis):
        self.web_application = tornado.web.Application(apis)
        tornado.ioloop.IOLoop.configure("tornado.platform.asyncio.AsyncIOLoop")
        self.http_server = tornado.httpserver.HTTPServer(self.web_application)
        self.port = port
       

    def start(self):
        self.http_server.listen(self.port)
        ioloop = tornado.ioloop.IOLoop.current()
        asyncio.set_event_loop(ioloop.asyncio_loop)
        event_loop_thread = threading.Thread(target=ioloop.start)
        event_loop_thread.daemon = True
        event_loop_thread.start()
        print("API server listening on port %s"%self.port)
        
    
    def finish(self):
        pass