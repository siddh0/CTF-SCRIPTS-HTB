import socket
import time

def send_requests(host, port, words):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host, port))
        print(s.recv(1024).decode())
        while True:
            for idx, word in enumerate(words):
                print(word)
                s.sendall(f"{word}\n".encode())
                response = s.recv(120000).decode()
                print(response)
                
                time.sleep(2)  # Optional: Add a delay between requests

if __name__ == "__main__":
    host = '94.237.55.212'
    port = 53967
    word_list = ['ArithmeticError', 'BlockingIOError', 'BrokenPipeError', 'BufferError', 'ConnectionError', 'EOFError', 'EncodingWarning', 'EnvironmentError', 'Exception',  'FloatingPointError', 'FileNotFoundError','FutureWarning', 'GeneratorExit', 'IOError', 'ImportError', 'ImportWarning', 'IndentationError', 'IndexError', 'InterruptedError', 'KeyError', 'LookupError', 'MemoryError', 'ModuleNotFoundError', 'NameError','NotADirectoryError', 'NotImplementedError', 'OSError', 'OverflowError', 'ReferenceError', 'RuntimeError', 'RuntimeWarning', 'StopIteration', 'SyntaxError', 'SyntaxWarning', 'TimeoutError', 'TypeError', 'UnicodeWarning', 'ValueError', 'Warning', 'complex', 'copyright','dict', 'dir', 'float', 'format', 'getattr',  'hex', 'id', 'input', 'int', 'iter', 'len', 'map', 'max', 'memoryview', 'min', 'next', 'oct', 'open', 'ord', 'pow', 'print', 'property', 'quit', 'range', 'repr', 'round', 'tuple', 'type', 'zip']
    # Replace with your list of words
    send_requests(host, port, word_list)
