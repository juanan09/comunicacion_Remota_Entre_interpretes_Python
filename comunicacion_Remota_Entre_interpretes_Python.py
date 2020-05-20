import traceback
from  multiprocessing.connection import Listener



def cliente(conexion):
    """
    Definicion del cliente
    :param conexion: host y puerto
    """
    try:
        while True:
            msg =conexion.recv()
            conexion.send(msg)
    except EOFError:
        print('La conexion se ha cerrado')

def servidor(direccion, clave):
    """
    Definicion del servidor
    :param direccion: host y puerto
    :param clave: clave e autenticacion en b
    """
    s = Listener(direccion, authkey=clave)

    while True:
        try:
            print('Servidor listo y esperando a recibir')
            c = s.accept()
            print('Se ha conectado el host: {} al puerto: {} '.format(s.address[0], s.address[1]))
            cliente(c)
        except Exception:
            traceback.print_exc()


servidor(('192.168.0.121', 20064), clave=b'User2k20')
