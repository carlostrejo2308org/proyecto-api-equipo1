# Resultados de consumir api 

## Utilizamos TDD
Para la creación del consumo de la api y sus respectivas pruebas unitarias, nos basamos en la metodologia de crear las pruebas, ejecutar para que falle por la necesidad del código necesario, creamos el código, esperamos a que las pruebas pasaran y refactorizamos el código.
1. Antes
![Image text](https://github.com/carlostrejo2308org/proyecto-api-equipo1/blob/main/images/Screenshot%20from%202022-04-22%2001-49-08.png)
2. Despues
![Image text](https://github.com/carlostrejo2308org/proyecto-api-equipo1/blob/main/images/MicrosoftTeams-image%20(1).png)
## Debugging
Utilizamos fuerza bruta ingresando prints en puntos críticos, para observar donde fallaba, también aplicamos el retroceso y eliminación de causa para algunos errores que no detectabamos a simple vista.
1.- Fuerza Bruta (Prints)
![Image text](https://github.com/carlostrejo2308org/proyecto-api-equipo1/blob/main/images/Screenshot%20from%202022-04-22%2001-05-42.png)

## Consumir api
Consumimos una api de libreria, en el cual filtramos por id y algunos otros filtros para mostrar la información necesaria.

## Eficiencia
Obtuvimos solo la información necesaria de los respectivos libros, para no mostrarle al usuario datos que no requiere, como lo podrian ser numero de serie, etc.
1. Sin filtros
Web
![Image text](https://github.com/carlostrejo2308org/proyecto-api-equipo1/blob/main/images/Screenshot%20from%202022-04-22%2001-02-52.png)
Consola
![Image text](https://github.com/carlostrejo2308org/proyecto-api-equipo1/blob/main/images/Screenshot%20from%202022-04-22%2001-21-26.png)
![Image text](https://github.com/carlostrejo2308org/proyecto-api-equipo1/blob/main/images/Screenshot%20from%202022-04-22%2001-31-09.png)
2.- Con filtros
![Image text](https://github.com/carlostrejo2308org/proyecto-api-equipo1/blob/main/images/Screenshot%20from%202022-04-22%2001-04-39.png)

## Pruebas unitarias
Se realizaron pruebas unitarias de las funcion extraer, para obtener información de un libro con su id en especifico.
Se puede observar en test_book.py

## SetUP
Se utilizo la función SetUp en las pruebas unitarias al principio, para levantar en enlace con la conexión a la api, para su posterior uso en la busqueda de id's.

## Mock Mock
En este ejemplo estamos mockeando el valor que retorna la funcion ExtraerElementos, podemos ver que el resultado siempre es el mismo por el mock, no importa el id que le estemos enviando.
![Image text](https://github.com/carlostrejo2308org/proyecto-api-equipo1/blob/main/images/MicrosoftTeams-image%20(2).png)

## Coverage alcanzado
Medimos la covertura del lineas de código de nuestro programa y pruebas con la libreria de coverage, se adjuntan resultados:
![Image text](https://github.com/carlostrejo2308org/proyecto-api-equipo1/blob/main/images/MicrosoftTeams-image%20(3).png)
![Image text](https://github.com/carlostrejo2308org/proyecto-api-equipo1/blob/main/images/MicrosoftTeams-image%20(4).png)
pd: Ayuda con el missing del main, no sabemos el porque 😞

## Diagrama de Flujo
![Image text](https://github.com/carlostrejo2308org/proyecto-api-equipo1/blob/main/images/DiagramaFlujoApi.png)

## System testing
En el archivo SystemTestingApi.xslx
