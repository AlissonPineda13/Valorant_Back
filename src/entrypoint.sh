#!/bin/sh

echo "Aplicando migraciones..."
flask db upgrade

echo "Insertando datos iniciales..."
flask insert_agents
flask insert_weapons

echo "Iniciando aplicación..."
python run.py