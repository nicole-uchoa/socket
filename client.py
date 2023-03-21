import socket                          

s = socket.socket()                    
host = socket.gethostname()            
port = 1234                           

try:
    s.connect((host, port))
    print("Inicie a conversa.")
    while True:
        message = input()
        if (message == 'SAIR' or message == 'sair' or message == 'Sair'):
            break
        s.send(message.encode())
        data = s.recv(1024)
        data = data.decode()
        if (data == 'SAIR' or data == 'sair' or data == 'Sair'):
            break
        print("SERVIDOR: "+ data)
except Exception as e:
    print(e)

s.close()                              