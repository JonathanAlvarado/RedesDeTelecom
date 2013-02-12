import socket
import sys

'''Arreglos para guardar las direcciones y los nombres de los jugadores'''
direcciones = []
nombres = []

def server():
    '''Contador de jugadores'''
    jugadores = 0

    '''localhost y puerto a utilizar'''
    ip = '127.0.0.1'
    puerto = 5005

    '''SOCK_DGRAM para sockets udp  '''
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
        
        '''Si el nombre recibido es mayor 1 se anade a los arreglos'''
        if len(nombre) > 1:
            anadir(addr,nombre)
            jugadores+=1

        '''Si solo hay un jugador debe esperar, sino pasa al juego'''
        if jugadores == 1:
            sock.sendto('Espera a un jugador...', direcciones[0])
        else:
            adivina(sock,jugadores)

    sock.close()


def anadir(address,nombre):
    '''Funcion para anadir direcciones y jugadores'''
    direcciones.append(address)
    nombres.append(nombre)


def adivina(sock,jugadores):
    '''Rutina del juego'''
    
    for x in range( jugadores ):
        '''Envia msj de bienvenida a los jugadores'''
        msj = 'Bienvenido ' + nombres[x]
        sock.sendto(msj, direcciones[x])
    
    '''Pregunta al jugador 1 la palabra que debe adivinar el jugador 2'''
    sock.sendto('Palabra a adivinar? ', direcciones[0])
    palabra,addr = sock.recvfrom(1024)

    while True:
        '''ciclo para preguntar a ambos jugadores, al jugador 1 por una pista
        y al dos se le da la pista y se le pregunta por una palabra.
        Esto es por turnos, en caso de que un jugador no conteste espera
        hasta que reciba respuesta'''
        for i in range(jugadores):
            if i == 0:
                sock.sendto('\nDa una pista ', direcciones[i])
                pista,addr = sock.recvfrom(1024)
            else:
                adivina = 'Pista: ' + pista
                sock.sendto(adivina, direcciones[i])
                respuesta,addr = sock.recvfrom(1024)
        '''Cuando la respuesta y la palabra a adivinar coinciden se le envia
        a ambos clientes un string y asi cerrar clientes y servidor'''
        if respuesta == palabra:
            ganador = nombres[1] + ' ha ganado'
            sock.sendto(ganador, direcciones[0])
            sock.sendto(ganador, direcciones[1])
            sock.close()
            sys.exit()

if __name__ == "__main__":
    server()
