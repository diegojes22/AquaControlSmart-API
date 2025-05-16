#
# Librerias
#
import Utils

#
# Respuestas del servidor al ESP32
#

'''
Plantilla de respuesta del servidor al ESP32.

Esta es la estructura basica de la respuesta del servidor al ESP32.
'''
template : dict = {
    "message" : "Respuesta del servidor",
    "date" : "fecha actual",
    "time" : "hora actual",
    "data" : dict # En caso de que se envien instrucciones al ESP32 se colocaran aqui.
}

''' 
Respuesta aun no definida en el servidor.

Esta es la respuesta que se envia al ESP cuando aun
no se define el paquete de instrucciones a enviar.
'''
notDefinedInstruction : dict = {
    "message" : "Instruction not defined",
    "date" : Utils.date(),
    "time" : Utils.time(),
    "data" : None
}

''' 
Respuesta de confirmacion al ESP32.

Este es la plantilla de respuesta del servidor al ESP32 cuando
el servidor recibe datos del ESP32.
'''
confirmToESP32 : dict = {
    "message" : "Data received",
    "date" : Utils.date(),
    "time" : Utils.time(),
    "data" : None
}