# Instalación de app web Odyssey
1.- Instalar Python 3.9.4
        Link: https://www.python.org/downloads/release/python-394/

2.- Crear ambiente virtual
        comando: python -m venv venv

3.- Ejecutar ambiente virtual
        comando 1: cd venv/Scripts
        comando 2: activate

4.- Instalar librerias
        comando: pip install -r requirements.txt

5.- Crar usuario en base de datos oracle xe 21c o superior utilizando el scrip del archivo:
        usuario.sql
        **SE DEBE EJECUTAR COMO USUARIO SYS / SYSADMIN

6.- Navegar a la ruta odyssey_web y realizar migraciones a la base de datos con los comandos:
        comando 1: python manage.py makemigrations
        comando 2: python manage.py migrate

7.- Poblar base de datos utilizando el archivo:
        Poblado.sql

8.- Crear procedimiento almacenado y trigger utilizando el archivo
        procedimiento_almacenado.sql

9.- Navegar a la ruta odyssey_web y levantar el servidor con el comando:
        python manage.py runserver

***Para realizar una compra debe utilizar los datos que aparecen en el archivo
        datos_tarjeta.txt