# Usa una imagen base de Python compatible con M1
FROM --platform=linux/amd64 python:3.10-slim

# Establece el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copia todos los archivos del proyecto
COPY . .

# Instala las dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Expone el puerto 8080 (usado por Cloud Run y local)
EXPOSE 8080

# Comando para ejecutar Flask
CMD ["python", "app_multimodal.py"]
