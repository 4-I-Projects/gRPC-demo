import logging
from concurrent import futures

import grpc
import drl_pb2
import drl_pb2_grpc
from google.protobuf.empty_pb2 import Empty

class DRLServicer(drl_pb2_grpc.DRLServicer):
    def __init__(self):
        self.drl = {
            22028250: 90,
            22028315: 90,
            22028177: 1,
            22028068: 20
        }

    def GetDRLScore(self, request, context):
        student_id = request.id
        score = self.drl[student_id]
        drl_score = drl_pb2.DRLResponse(drl_score=score)
        return drl_score
        
    def CreateDRLScore(self, request, context):
        print("request is: ", request.student_id.id)
        print("drls are: ", self.drl)
        student_id = request.student_id.id
        drl_score = request.drl_score
        self.drl[student_id] = drl_score
        return Empty()

        

def serve():
    port = "50051"
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    drl_pb2_grpc.add_DRLServicer_to_server(DRLServicer(), server)
    server.add_insecure_port("[::]:" + port)
    server.start()
    print("Server started, listening on " + port)
    server.wait_for_termination()


if __name__ == "__main__":
    logging.basicConfig()
    serve()
