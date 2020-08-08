# AKARin
El proyecto AKARin consiste en un gestor de archivos online, orientado 
basicamente a almacenar y organizar de manera remota documentos de
índole admninistrativo de la escuela de Ciencias de la Computación
de la Universidad Nacional de San Agustín de Arequipa.

##Prerequisitos
Para testear el proyecto actual de forma local se requiere
1. Python 3.x
2. Django 3.x
2. Librerias Pillow

##Ejecución

Para ejecutar el actual proyecto en desarrollo se ubica en el directorio
del proyecto y ejecuta el siguiente comando:

(En windows)

	$ python manage.py runserver

(En Linux)

	$ python3 manage.py runserver

Cabe resaltar que para modo testeo necesita configurar el archivo $akarin->config.py
con los valores de su esquema y su configuración de acceso:

```
#MYSQL DB
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'akarin',		#Nombre del Scheme
        'USER': 'root',		#Usuario de la conexión
        'PASSWORD': 'admin',	#Contraseñ de la conexión
        'HOST': 'localhost',	#Dirección del host
        'PORT': '3306'			#Puerto
    }
}
```
O en su defecto usar la configuración de la base de datos ligera implementada en
SQLite3:
```
#SQLite3
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
```

##Visualizar
Para interactuar con el proyecto se dirige al navegador y accede a la siguiente 
dirección
	http://127.0.0.1:8000/