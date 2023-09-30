from api_server import APIServer


from apis.batches import Batches
from apis.batch import Batch
from apis.students import Students
from apis.student import Student
from apis.fees import Fees
from apis.new_admissions import NewAdmissions
from apis.display_picture import DisplayPicture
from apis.recent_fees import RecentFees
from apis.pending_fees import PendingFees
from apis.summary import Summary

PORT_NUMBER = 4567


apis = [
            (r'/api/batches', Batches),
            (r'/api/batch', Batch),
            (r'/api/students', Students),
            (r'/api/student', Student),
            (r'/api/fees', Fees),

            (r'/api/new-admissions', NewAdmissions),
            (r'/api/dp', DisplayPicture),
            (r'/api/recent-fees', RecentFees),
            (r'/api/pending-fees', PendingFees),
            (r'/api/summary', Summary),

]
    



if __name__ == '__main__':
    server = APIServer(PORT_NUMBER, apis)
    server.start()
    
    print()
    print("___________________________________")
    print("|    APIs For Development 1.0     |")
    print("|_________________________________|")
    print()
    input("Press a key to exit ..")
    print()

    server.finish()