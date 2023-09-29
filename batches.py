import tornado
import json

data = [
    {
        'id':1,
        'title': 'TTS 7:00PM',
        'subject': 'PHYSICS',
        'standard': 12,
        'fee': 700,
        'started_on': '2023-01-01'
    },
    {
        'id':2,
        'title': 'TTS 7:00PM',
        'subject': 'CHEMISTRY',
        'standard': 11,
        'fee': 700,
        'started_on': '2023-02-01'
    }
]

class Batches(tornado.web.RequestHandler):
    def get(self):
        self.write(json.dumps(data))

    def post(self):
        self.write("Not supported")
