from api_server import APIServer


from batches import Batches
from batch import Batch
from students import Students
from student import Student
from fees import Fees

PORT_NUMBER = 4567


apis = [
            (r'/api/batches', Batches),
            (r'/api/batch', Batch),
            (r'/api/students', Students),
            (r'/api/student', Student),
            (r'/api/fees', Fees),

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