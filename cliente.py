import socket
import sys

def cliente(puerto):
    ip = '127.0.0.1'
    port = 5005

    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    except socket.error:
        print 'No se pudo crear socket cliente'
        sys.exit()

    if puerto == port:
        print 'Conexion exitosa'
    else:
        print 'Puerto equivocado'
        sys.exit()

    while True:
        jugador = raw_input('Nombre: ')

        try:
            sock.sendto(jugador,(ip,puerto))
            juego(sock, ip, puerto)
        except socket.error:
            print 'Error'
            sys.exit()

    sock.close()

def juego(sock, ip, puerto):
    
    while True:
        try:
            msj, address = sock.recvfrom(1024)
            print msj
        except:
            print 'Problema con la conexion con el servidor\n'
            sys.exit()

        if len(msj) >= 11 and 'Espera' not in msj:
            adivina(sock,ip,puerto)

def adivina(sock,ip,puerto):
    while True:
        try:
            msj, address = sock.recvfrom(1024)
            if 'ganado' in msj:
                print msj
                sock.close()
                sys.exit()
            print '\n',msj
            palabra = raw_input('Palabra: ')
            sock.sendto(palabra,(ip,puerto))
        except socket.error:
            print 'Error'
            sys.exit()
        
            
    

if __name__ == '__main__':
    puerto = int(sys.argv[1])
    cliente(puerto)
