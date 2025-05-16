# AquaControlSmart-API
Sistema Backend para el proyecto de InnovaTec AquaControlSmart

> ## Funcionamiento
> Este servidor usa FastApi y debe ser arrancado con uvicorn.
> Para iniciar el servidor se hace con el siguiente comando:
> 
> `uvicorn main:app --host 0.0.0.0 --port 5050`
>
> El ESP32 estara configurado para enviar las peticiones al 
> puerto `5050`, de lo contrario no funcionara.

El servicio se iniciara en modo `localhost` pero puede ser
accedido desde cualquier dispositivo de una red LAN. Para esto
es recomendable que la maquina que contiene el server tenga
una IP estatica.


## Sobre FastApi
**FastApi** genera la documentacion de forma automatica pero
para poder acceder a la misma se debe de encender el servidor
y acceder a la siguiente ruta:
    `localhost:5050/docs/`

## Novedades
* Definicion de los EndsPoints.
* Definiendo paquetes de comunicacion.

