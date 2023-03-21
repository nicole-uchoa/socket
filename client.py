import socket                          

s = socket.socket()                    
host = socket.gethostname()            
port = 1234                           

try:
    s.connect((host, port))
    print("Inicie a conversa.")
    while True:
        message = input()
        if (message == 'SAIR'):
            s.send(message.encode())
            break
        s.send(message.encode())
        data = s.recv(1024)
        data = data.decode()
        print("SERVIDOR: "+ data)
except Exception as e:
    print(e)

s.close()                              