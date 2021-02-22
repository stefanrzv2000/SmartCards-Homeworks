import socket
import mycrypt
import threading
import time

HOST = '127.0.0.1' # Standard loopback interface address (localhost)
PORT = 65432           # Port to listen on (non-privileged ports are > 1023)

buffer_size = 1<<16
threads = []
client_count = 0 
waiting = []
client_info = dict()

def process_message(msg,tid,sock):

    return 0

def manage_client(cs):

    global client_count

    my_idcount=client_count
    print(f'client #{client_count} from: {cs.getpeername()}' )
    # message=f'Hello client #{client_count}! Welcome to encrypted files sender! Type your commands to the command line!'
    # cs.sendall(bytes(message,'ascii'))

    # client_info[my_idcount] = cinfo(my_idcount,cs.getpeername())

    try:
        r_msg = cs.recv(buffer_size)
        ans = process_message(r_msg,my_idcount,cs)
        cs.sendall(ans)
    except socket.error as e_msg:
        print('Error:',e_msg.strerror)
        
    print(f"Thread {my_idcount} finished job")


if __name__ == "__main__":
    
    try:
        ss=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        ss.bind( (HOST,PORT) )
        ss.listen(5)
    except socket.error as e_msg:
        print(e_msg.strerror)
        exit(-1)
    
    while True:

        c_sock, c_addr = ss.accept()

        t = threading.Thread(target=manage_client, args=(c_sock,) )
        threads.append(t)
        client_count+=1
        t.start()