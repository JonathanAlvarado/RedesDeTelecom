import socket
import sys

def cliente(puerto, jugador):
    '''localhost y puerto para comprar y saber si es el puerto correcto'''
    ip = '127.0.0.1'
    port = 5005

    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    except socket.error:
        print 'No se pudo crear socket cliente'
        sys.exit()

    '''comprueba si el puerto es el correcto'''
    if puerto == port:
        print 'Conexion exitosa'
    else:
        print 'Puerto equivocado'
        sys.exit()

    '''Envia nombre de jugador'''
    try:
        sock.sendto(jugador,(ip,puerto))
        juego(sock, ip, puerto)
    except socket.error:
        print 'Error'
        sys.exit()

    sock.close()

def juego(sock, ip, puerto):
    '''Espera por el msj de bienvenida del servidor'''
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
    '''Recibe los msjs del servidor y en caso de recibir el string
    con el ganador termina el programa'''
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
    nombre = sys.argv[1]
    puerto = int(sys.argv[2])
    cliente(puerto,nombre)
