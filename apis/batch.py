import tornado
import json

data = {'1':
    {
        'id':1,
        'title': 'TTS 7:00PM',
        'subject': 'PHYSICS',
        'standard': 12,
        'fee': 700,
        'started_on': '2023-01-01'
    },
    '2': {
        'id':2,
        'title': 'TTS 7:00PM',
        'subject': 'CHEMISTRY',
        'standard': 11,
        'fee': 700,
        'started_on': '2023-02-01'
    }
}

class Batch(tornado.web.RequestHandler):
    def get(self):
        batch_id = self.get_argument('id','1')
        self.write(json.dumps(data[batch_id]))

    def post(self):
        self.write("Not supported")
