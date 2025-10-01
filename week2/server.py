from concurrent import futures

import grpc
import todo_pb2
import todo_pb2_grpc

class TodoServicer(todo_pb2_grpc.TodoServicer):
    def __init__(self):
        self.todos = []

    def CreateTodo(self , request, context):
        todo = todo_pb2.TodoItem(id=len(self.todos) + 1, text=request.text)
        self.todos.append(todo)
        print(self.todos)
        return todo

    def ReadTodos(self, request, context):
        print(request)
        print(context)
        print(self.todos)
        todos = todo_pb2.TodoItems()
        todos.items.extend(self.todos)
        return todos

server = grpc.server(futures.ThreadPoolExecutor(2))
todo_pb2_grpc.add_TodoServicer_to_server(
    TodoServicer(), server
)
server.add_insecure_port("[::]:50001")
server.start()
print("server is listening...")
server.wait_for_termination()
    


