FROM python:3.11-slim

# Ver logs en tiempo real
ENV PYTHONUNBUFFERED=1
#directorio de trabajo donde vamos a pararnos
WORKDIR /crud

# Instala dependencias
COPY requirements.txt .
#instala las dependencias via pip
RUN pip install --no-cache-dir -r requirements.txt

# Copia el código fuente
COPY crud/ .

