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

5.- Crar base usuario en base de datos oracle xe 21c o superior utilizando el scrip del archivo:
        USUARIO.sql
        **SE DEBE EJECUTAR COMO USUARIO SYS / SYSADMIN
        
6.- Poblar base de datos utilizando el archivo:
        Poblado.sql

7.- Navegar a la ruta odyssey_web y levantar el servidor con el comando:
        python manage.py runserver