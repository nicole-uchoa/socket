import socket

s = socket.socket()
host = socket.gethostname()
port = 1234                                
s.bind((host, port))

try:
    s.listen(5)
    print('Esperando conexao.')
    c, addr = s.accept()
    print('Conexão estabelecida com: ', addr)
    while True:
        data = c.recv(1024)
        msg = data.decode()
        print("CLIENTE: " + msg)
        if (msg == 'SAIR' or msg == 'sair' or msg == 'Sair'): 
            break
        data = input()
        if (data != 'SAIR' and data != 'sair' and data != 'Sair'):   
            c.send(data.encode())
        else:
            c.send(data.encode())
            break
    c.close()
except Exception as e:
    print(e)
    c.close
