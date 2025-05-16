#
# Librerias
# 

# FastAPI
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

# Models
from models.Package import Package
from models.Testing import Test

from models.ref import ServerResponse

#
# Routes
#

# FastAPI
app = FastAPI()

# root o index
@app.get("/")
async def root():
    ''' Root '''
    return {"message": "Hello World"}

# para pruevas
@app.get("/test/{id}")
async def read_item(id: int):
    ''' Test
    Esta es solo para probar la API, no tiene ningun uso real y 
    debe ser eliminada en la version final.

    :param id: id del test
    :return: id y mensaje
    :rtype: dict
    '''
    return {"id": id, "Mensaje" : "Esto es una prueva"}

# el esp manda datos por aqui
@app.post("/esp32/submit")
async def read_item(package: Package): 
    ''' Recibe un paquete del ESP32
    :param package: Paquete enviado por el ESP32 el cual puede contener informacion de sensores
    :type package: Package
    :return: Paquete recibido
    :rtype: dict
    '''
    print(package)

    # queda pendiente el enviar a la base de datos

    return ServerResponse.confirmToESP32

# el esp recive datos e instrucciones por aqui
@app.get("/esp32/getInstructions/{fromESP}")
async def read_item(fromESP: int):
    ''' Envia instrucciones al ESP32
    :param fromESP: Origen del solicitante de la isntruccion
    :type from: int
    :return: Instrucciones enviadas
    :rtype: dict
    '''

    print(type)

    # queda pendiente el enviar a la base de datos
    # aun defi niendo el paquete de instrucciones

    return ServerResponse.notDefinedInstruction

@app.get("/mobile/query/{user}")
async def mobile_query(user: str):
    ''' Consulta de datos para el movil
    :param user: Usuario que solicita la consulta
    :type user: str
    :return: Consulta de datos
    :rtype: dict
    '''
    # queda pendiente el enviar a la base de datos

    return {"user": user, "message": "Consulta de datos"}