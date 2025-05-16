'''
                Utils.py
Aui estaran varias funciones utiles para el proyecto, desde el manejo de la
fecha y hora, entre otras cosas pequenas pero utiles.

:author D
'''

#
# Librerias
#
from datetime import datetime

#
# Funciones relacionadas con la fecha y hora
#
def date():
    ''' Obtener la fecha actual '''
    return datetime.now().date()  # Retorna solo la fecha (sin hora)

def time():
    ''' Obtener la hora actual '''
    return datetime.now().time()  # Retorna solo la hora (sin fecha)

def now():
    ''' Obtener la fecha y hora actual '''
    return datetime.now()  # Retorna la fecha y hora actual