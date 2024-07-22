import socket
import time 

def automate_game():
    host = '83.136.255.230'
    port = 47612

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host, port))
        print(s.recv(1024).decode())
        s.sendall(b"y\n")
        while True:
            data = s.recv(1024).decode()
            print(data)
            if "HTB" in data:
                break
            actions = parse_data(data)
            response = "-".join(actions)
            print(response)
            s.sendall(response.encode()+b"\n")
            time.sleep(0.5)

def parse_data(data):
    actions = []
    scenarios = data.split(", ")
    for scenario in scenarios:
        if "GORGE" in scenario:
            actions.append("STOP")
        elif "PHREAK" in scenario:
            actions.append("DROP")
        elif "FIRE" in scenario:
            actions.append("ROLL")
    return actions

if __name__ == "__main__":
    automate_game()
