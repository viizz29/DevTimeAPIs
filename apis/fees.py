import tornado
import json

data = {
    'name': 'Suraj Kumar',
    'fees': [
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
                'name': 'Suraj Kumar',
                'standard': 12,
                'amount': 700,
                'date': '2023-02-01',
                'remark': "paid cash."
            },
        ]
}
class Fees(tornado.web.RequestHandler):
    def get(self):
        self.write(json.dumps(data))

    def post(self):
        self.write("Not supported")