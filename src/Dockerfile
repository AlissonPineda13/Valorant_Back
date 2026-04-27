FROM python:3.11-slim

# Evita archivos .pyc y buffer
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

# Copiar requirements primero (mejora cache)
#COPY requirements.txt .

RUN apt-get update && apt-get install -y \
    gcc \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*


# Instalar dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el resto del código
COPY . .

# Dar permisos al entrypoint
RUN chmod +x entrypoint.sh

# Ejecutar script inicial
ENTRYPOINT ["./entrypoint.sh"]