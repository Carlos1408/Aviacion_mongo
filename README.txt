Esta es una aplicacion para la gestion de una base de datos la cual se ejecuta en el navegador
Los componentes usados para el desarrollo de la aplicacion son:

Frontend:
    HTML, jinja2
    CSS, framework Bootstrap

Backend:
    Python, framework Flask

Base de datos:
    PostgreSQL

Se deben tener los modulos flask y psycopg2 instalados, en caso de no tenerlos ejecutar los siguientes comandos en
la consola de comandos.
pip install flask
pip install psycopg2

Para ejecutar la aplicacion se debe ejecutar el archivo App.py, ubicado en la carpeta src, se abre la consola de comandos y en el
navegador deberemos escribir la siguiente ruta: http://127.0.0.1:3000/

En la pantalla principal se muestran 8 botones, los cuales nos llevaran a los datos de las tablas correspondientes.
En la panalla de cada tabla se muestra un espacio donde podemos ingresar datos, asi mismo un campo select, este nos servira para
buscar registros en la tabla.
El boton "Nuevo registro" nos redirigira a un formulario donde se llenaran los datos ncesarios para ingresar un nuevo registro.
Cada registro tiene un boton "editar" y "eliminar", los cuales nos ayudaran a realizar dichas operaciones con los registros.

Repositorio de github: https://github.com/Carlos1408/Aviacion.git