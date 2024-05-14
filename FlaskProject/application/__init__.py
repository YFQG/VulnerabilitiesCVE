from flask import Flask
from pymongo import MongoClient

app = Flask(__name__)

# Configura la conexión a MongoDB
# Reemplaza 'nombre_de_usuario', 'contraseña', 'nombre_de_host' y 'puerto' con tus propias credenciales y detalles de conexión
client = MongoClient('mongodb+srv://pipequiroga34:fRn70Ys7zX88KCxO@cluster0.h2lbkt0.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0')

# Selecciona la base de datos
db = client.get_database('Vulnerabilities')  # Cambia 'nombre_de_tu_base_de_datos' por el nombre de tu base de datos

collection = db['PcSoftwareCVE']

db = collection.find()

from . import routes