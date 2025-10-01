import logging
from concurrent import futures

import grpc
import gpa_pb2
import gpa_pb2_grpc
from google.protobuf.empty_pb2 import Empty

class GPAServicer(gpa_pb2_grpc.GPAServicer):
    def __init__(self):
        self.gpa = {
            22028250: 3.0,
            22028315: 0.0,
            22028177: 3.1,
            22028068: 4.0
        }

    def GetGPA(self, request, context):
        student_id = request.id
        score = self.gpa[student_id]
        gpa_score = gpa_pb2.GPAResponse(gpa_score=score)
        return gpa_score
        
    def CreateGPA(self, request, context):
        # print("request is: ", request.student_id.id)
        # print("drls are: ", self.drl)
        student_id = request.student_id.id
        gpa_score = request.gpa_score
        self.gpa[student_id] = gpa_score
        return Empty()

        

def serve():
    port = "50052"
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    gpa_pb2_grpc.add_GPAServicer_to_server(GPAServicer(), server)
    server.add_insecure_port("[::]:" + port)
    server.start()
    print("Server started, listening on " + port)
    server.wait_for_termination()


if __name__ == "__main__":
    logging.basicConfig()
    serve()
