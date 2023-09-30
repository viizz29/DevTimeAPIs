import tornado
import json

data = [
    {
        'id':1,
        'name': 'Tanisha Paul',
        'date': '2023-08-03',
    },
    {
        'id':2,
        'name': 'Ankit Kumar',
        'date': '2023-08-02',
    },
    {
        'id':3,
        'name': 'Suraj Pandey',
        'date': '2023-08-01',
    },
    {
        'id':4,
        'name': 'Lakhan Gorai',
        'date': '2023-08-01',
    },
    {
        'id':5,
        'name': 'Dinesh Yadav',
        'date': '2023-07-20',
    },
    {
        'id':6,
        'name': 'Surjeet Kundu',
        'date': '2023-08-02',
    }
]

class NewAdmissions(tornado.web.RequestHandler):
    def get(self):
        self.write(json.dumps(data))

    def post(self):
        self.write("Not supported")
