Esta es la primera version de una aplicacion para la gestion de una base de datos la cual se ejecuta en el navegador
Los componentes usados para el desarrollo de la aplicacion son:

Frontend:
    HTML, jinja2
    CSS, framework Bootstrap

Backend:
    Python, framework Flask

Base de datos:
    PostgreSQL

Para ejecutar la aplicacion se debe ejecutar el archivo App.py, se abre la consola de comandos y a la direccion que
se muestra luego de inicializar el programa dar crtl+click a la direccion mostrada, seguidamente se abrira el navegador
con la aplicacion ejecutandose.

En la primera pantalla se muestran 4 botones los cuales representan las tablas de la base de datos, al dar click en uno de ellos
nos redirige a las operaciones que se pueden hacer con la tabla, inicialmente se muestra un formulario y la tabla, en el formulario
podemos introducir los datos que queramos insertar en latabla, para insertar los datos se da click en insertar. Si se quiere modificar
un registro debemos ir al formulario de abajo y ahi insetar el campo de busqueda que nos pide, click en buscar. se genera otro formulario
con los campos de el registro buscado, listos para editarse, para modificar el registro hay que dar click en Actualizar, o si se pretende
eliminar el registro se da click en "eliminar registro" y automaticamente se eliminara el registro redirigiendonos a la pantalla anterior
Podemos navegar entre las tablas y la pantalla inicial con los botones de "volver" o con la barra de navegacion ubicada en la parte superior