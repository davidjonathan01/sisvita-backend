# Permite usar la imagen de python 3.12
FROM python:3.12  

# Copia el contenido de la carpeta actual al contenedor en la carpeta /app para que se ejecute la aplicación
COPY ./ /app 
# Establece el directorio de trabajo en /app
WORKDIR /app
# Instala las dependencias del archivo requirements.txt
RUN pip install -r requirements.txt
# Expone el puerto 5000
EXPOSE 5000

# Comando para ejecutar la aplicación
CMD ["python3", "-m", "flask", "run", "--host=0.0.0.0"]