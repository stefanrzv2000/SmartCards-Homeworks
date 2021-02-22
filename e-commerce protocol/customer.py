import socket
import mycrypt

PG_HOST = '127.0.0.1'   # The server's hostname or IP address
PG_PORT = 65432             # The port used by the server

MC_HOST = '127.0.0.1' # Standard loopback interface address (localhost)
MC_PORT = 54321           # Port to listen on (non-privileged ports are > 1023)

buffer_size = 1<<16

def process_message(msg,sock):

    msg = msg.decode('ascii')

    de_afisat = msg

    return de_afisat

def get_command():

    msg = input("Introduce next command: ")

    if msg == 'end':
        fin = True

    else:
        fin = False

    return msg, fin

def send_message(msg,sock):

    pass

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((MC_HOST, MC_PORT))

    fin = False    
    while not fin:

        r_msg = s.recv(buffer_size)

        de_afisat = process_message(r_msg,s)

        print(de_afisat)
        #print(f"Message from server: {r_msg.decode('ascii')}")

        msg, fin = get_command()
        send_message(msg,s)
