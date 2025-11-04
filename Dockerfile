# ========================================
# Lucy Network Real Estate V1 - Dockerfile
# ========================================

FROM python:3.10-slim

# Establecer el directorio de trabajo
WORKDIR /app

# Copiar archivos de requisitos y app
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Exponer el puerto 8080 (Cloud Run)
EXPOSE 8080

# Comando de inicio para Flask
CMD ["python", "app.py"]
