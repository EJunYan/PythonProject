
import tornado.ioloop
import tornado.httpserver
import tornado.web
import dbm

class MainHandler(tornado.web.RequestHandler):

    # 处理所有逻辑

    def get(self, *args, **kwargs):
        self.write("Hello My Name Is Alone");

    def post(self, *args, **kwargs):
        db = dbm.DBM.get_instance()
        db.inset_data(self.request.body)
        # dbm.inset_data(self.request.body)
        self.write("请求成功")

def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
    ])


if __name__ == '__main__':
    print("Hello Alone APP Server");
    app = make_app()
    server = tornado.httpserver.HTTPServer(app)
    server.bind(8888)
    server.start(0)
    tornado.ioloop.IOLoop.current().start();