# Resultados de consumir api 

## Utilizamos TDD
Para la creación del consumo de la api y sus respectivas pruebas unitarias, nos basamos en la metodologia de crear las pruebas, ejecutar para que falle por la necesidad del código necesario, creamos el código, esperamos a que las pruebas pasaran y refactorizamos el código.
1. Antes
![Image text](url)
2. Despues
![Image text](url)
## Debugging
Utilizamos fuerza bruta ingresando prints en puntos críticos, para observar donde fallaba, también aplicamos el retroceso y eliminación de causa para algunos errores que no detectabamos a simple vista.

## Consumir api
Consumimos una api de libreria, en el cual filtramos por id y algunos otros filtros para mostrar la información necesaria.

## Eficiencia
Obtuvimos solo la información necesaria de los respectivos libros, para no mostrarle al usuario datos que no requiere, como lo podrian ser numero de serie, etc.
1. Sin filtros
![Image text](url)
2.- Con filtros
![Image text](url)

## Pruebas unitarias
Se realizaron pruebas unitarias de las funcion extraer, para obtener información de un libro con su id en especifico.
Se puede observar en test_book.py

## SetUP
Se utilizo la función SetUp en las pruebas unitarias al principio, para levantar en enlace con la conexión a la api, para su posterior uso en la busqueda de id's.

## Diagrama de Flujo



