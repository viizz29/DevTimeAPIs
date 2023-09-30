import tornado
import json
import os
from mimetypes import guess_type

dps = ['dp_unknown.png', 'dp_male.jpeg', 'dp_female.jpeg']

class DisplayPicture(tornado.web.RequestHandler):
    def get(self):
        user_id = int(self.get_argument('id','0'))
        file_location = "./images/"+dps[user_id%len(dps)]
        if not os.path.isfile(file_location):
            raise tornado.web.HTTPError(status_code=404)
        content_type, _ = guess_type(file_location)
        self.add_header('Content-Type', content_type)
        with open(file_location, "rb") as source_file:
            self.write(source_file.read())

    def post(self):
        self.write("Not supported")
