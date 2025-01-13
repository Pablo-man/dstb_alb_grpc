import grpc
import calculator_pb2
import calculator_pb2_grpc

def run():
    # Conectar al servidor gRPC
    channel = grpc.insecure_channel('localhost:50051')
    stub = calculator_pb2_grpc.CalculatorStub(channel)

    # Realizar operaciones
    num1, num2 = 7, 3

    # Llamar a Add
    response_add = stub.Add(calculator_pb2.Numbers(num1=num1, num2=num2))
    print(f"Suma: {num1} + {num2} = {response_add.value}")

    # Llamar a Multiply
    response_multiply = stub.Multiply(calculator_pb2.Numbers(num1=num1, num2=num2))
    print(f"Multiplicación: {num1} * {num2} = {response_multiply.value}")

if __name__ == '__main__':
    run()
