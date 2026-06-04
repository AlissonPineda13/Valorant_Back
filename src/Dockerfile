FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

# Copiar requirements
COPY src/requirements.txt .

# Instalar dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Copiar solo src (mejor que copiar todo)
COPY src/ .

# Copiar entrypoint explícitamente
COPY src/entrypoint.sh .

# Permisos
RUN chmod +x entrypoint.sh

ENTRYPOINT ["./entrypoint.sh"]