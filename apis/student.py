import tornado
import json

class Student(tornado.web.RequestHandler):
    def get(self):
        student_id = self.get_argument('id','1')
        data = {
            '1':{
                'id':1,
                'name': 'Suraj Kumar',
                'standard': 12,
                'fee': 700,
                'admission_date': '2023-01-01',
                'school': 'Gulmohar',
            },
            '2': {
                'id':2,
                'name': 'Rani Kumari',
                'standard': 12,
                'fee': 700,
                'admission_date': '2023-02-02',
                'school': 'JPS',
            }
        }
        self.write(json.dumps(data[student_id]))

    def post(self):
        self.write("Not supported")
