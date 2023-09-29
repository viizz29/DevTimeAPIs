import tornado
import json

class Fees(tornado.web.RequestHandler):
    def get(self):
        data = [
            {
                'id':1,
                'name': 'Suraj Kumar',
                'standard': 12,
                'amount': 700,
                'date': '2023-01-01',
                'remark': "paid cash."
            },
            {
                'id':2,
                'name': 'Rani Kumari',
                'standard': 12,
                'amount': 700,
                'date': '2023-02-02',
                "remark": "paid through google pay"
            }
        ]
        self.write(json.dumps(data))

    def post(self):
        self.write("Not supported")