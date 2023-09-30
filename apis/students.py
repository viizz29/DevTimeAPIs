import tornado
import json

data = [
    {
        'id':1,
        'name': 'Suraj Kumar',
        'standard': 12,
        'fee': 700,
        'admission_date': '2023-01-01',
        'school': 'Gulmohar',
    },
    {
        'id':2,
        'name': 'Rani Kumari',
        'standard': 12,
        'fee': 700,
        'admission_date': '2023-02-02',
        'school': 'JPS',
    }
]

class Students(tornado.web.RequestHandler):
    def get(self):
        self.write(json.dumps(data))

    def post(self):
        self.write("Not supported")