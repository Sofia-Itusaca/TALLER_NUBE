# SPEC 02 - Consulta del clima

## 1. Descripción

El sistema debe permitir al usuario consultar las condiciones meteorológicas actuales de una ciudad mediante una API externa de información climática.

## 2. Datos de entrada

- Nombre de la ciudad

## 3. API utilizada

WeatherAPI

## 4. Requisitos funcionales

### RF-01
El sistema debe mostrar un campo para ingresar el nombre de una ciudad.

### RF-02
El usuario debe poder ejecutar la consulta mediante el botón "Consultar".

### RF-03
El sistema debe enviar la ciudad ingresada a la API de WeatherAPI.

### RF-04
El sistema debe mostrar el nombre de la ciudad consultada.

### RF-05
El sistema debe mostrar la temperatura actual.

### RF-06
El sistema debe mostrar la sensación térmica.

### RF-07
El sistema debe mostrar la humedad.

### RF-08
El sistema debe mostrar la velocidad del viento.

### RF-09
El sistema debe mostrar la descripción del estado del clima.

### RF-10
El sistema debe mostrar un icono representativo del estado meteorológico.

### RF-11
Si ocurre un error durante la consulta, el sistema debe mostrar un mensaje informativo al usuario.

## 5. Resultado esperado

Al ingresar una ciudad válida, el sistema debe mostrar la información meteorológica actual proporcionada por WeatherAPI.

## 6. Evolución prevista

En una segunda versión del sistema se incorporará una segunda API meteorológica como mecanismo de respaldo.

Si la API principal no responde correctamente, el sistema podrá utilizar la segunda API para realizar la consulta.