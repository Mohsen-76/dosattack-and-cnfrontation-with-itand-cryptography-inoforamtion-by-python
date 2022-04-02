import socket
import time
ip=input('enter the ip : ')
counter=0
while True:
    time.sleep(2)
    counter+=1
    try:
        s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        s.connect((ip,8000))
        print(f'i connected {counter}')
    except:
        print('i cant connect')   
        break 

    
