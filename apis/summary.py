import tornado
import json

data = {
    'student_count': 90,
    'batch_count': 23,
    'earning_this_month': 100500,
}

class Summary(tornado.web.RequestHandler):
    def get(self):
        self.write(json.dumps(data))

    def post(self):
        self.write("Not supported")
