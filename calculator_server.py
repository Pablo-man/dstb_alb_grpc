import grpc
from concurrent import futures
import calculator_pb2
import calculator_pb2_grpc

# Implementación del servicio
class CalculatorServicer(calculator_pb2_grpc.CalculatorServicer):
    def Add(self, request, context):
        result = request.num1 + request.num2
        return calculator_pb2.Result(value=result)

    def Multiply(self, request, context):
        result = request.num1 * request.num2
        return calculator_pb2.Result(value=result)

# Inicialización del servidor
def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    calculator_pb2_grpc.add_CalculatorServicer_to_server(CalculatorServicer(), server)
    server.add_insecure_port('[::]:50051')
    print("Servidor gRPC corriendo en el puerto 50051...")
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    serve()
