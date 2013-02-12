import socket
import sys

direcciones = []
nombres = []

def server():

    jugadores = 0

    '''localhost'''
    ip = '127.0.0.1'
    puerto = 5005

    '''SOCK_DGRAM datagram  '''
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    except:
        print 'No se pudo crear el socket'
        sys.exit()

    '''Ligar socket con puerto e ip para iniciar servidor'''
    try:
        sock.bind( (ip, puerto) )
        print 'Servidor iniciado...'
    except:
        print 'Error al iniciar servidor...'
        sys.exit()

    while True:
        '''tamano de buffer 1024 '''
        nombre,addr = sock.recvfrom(1024)
        
        if len(nombre) > 1:
            anadir(addr,nombre)
            jugadores+=1

        if jugadores == 1:
            sock.sendto('Espera a un jugador...', direcciones[0])
        else:
            adivina(sock,jugadores)

    sock.close()

def anadir(address,nombre):
    direcciones.append(address)
    nombres.append(nombre)

def adivina(sock,jugadores):
    
    for x in range( jugadores ):
        msj = 'Bienvenido ' + nombres[x]
        sock.sendto(msj, direcciones[x])
    
    sock.sendto('Palabra a adivinar? ', direcciones[0])
    palabra,addr = sock.recvfrom(1024)

    while True:
        for i in range(jugadores):
            if i == 0:
                sock.sendto('\nDa una pista ', direcciones[i])
                pista,addr = sock.recvfrom(1024)
            else:
                adivina = 'Pista: ' + pista
                sock.sendto(adivina, direcciones[i])
                respuesta,addr = sock.recvfrom(1024)
        if respuesta == palabra:
            ganador = nombres[1] + ' ha ganado'
            sock.sendto(ganador, direcciones[0])
            sock.sendto(ganador, direcciones[1])
            sock.close()
            sys.exit()

if __name__ == "__main__":
    server()
