import grpc
import todo_pb2
import todo_pb2_grpc

with grpc.insecure_channel("localhost:50001") as channel:
    stub = todo_pb2_grpc.TodoStub(channel)
    request = todo_pb2.TodoItem(id=-1, text='do laundry')
    # response = stub.CreateTodo(request)
    request = todo_pb2.void()
    response = stub.ReadTodos(request)
    print(response)
