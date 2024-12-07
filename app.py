from pymongo import MongoClient
import os
from dotenv import load_dotenv

# Cargar variables de entorno desde el archivo .env
load_dotenv()

# Obtener las credenciales de conexión desde las variables de entorno
MONGO_URI = os.getenv("MONGO_URI")
DATABASE_NAME = os.getenv("DATABASE_NAME")

# Conectar a MongoDB Atlas
client = MongoClient(MONGO_URI)
db = client[DATABASE_NAME]

# Función para insertar datos en la colección
def insert_data(collection_name, data):
    collection = db[collection_name]
    result = collection.insert_one(data)
    print(f"Documento insertado con ID: {result.inserted_id}")

# Función para consultar datos desde la colección
def query_data(collection_name, query):
    collection = db[collection_name]
    results = collection.find(query)
    for document in results:
        print(document)

# Ejecutar las funciones como ejemplo
if __name__ == "__main__":
    # Insertar un documento de ejemplo
    print("Insertando datos...")
    insert_data("productos", {
        "nombre": "Teléfono Móvil",
        "precio": 750,
        "categoria": "Electrónica",
        "marca": "Samsung",
        "stock": 25
    })

    # Consultar documentos de ejemplo
    print("\nConsultando datos:")
    query_data("productos", {"categoria": "Electrónica"})
from pymongo import MongoClient
import os
from dotenv import load_dotenv

# Cargar variables de entorno desde el archivo .env
load_dotenv()

# Obtener las credenciales de conexión desde las variables de entorno
MONGO_URI = os.getenv("MONGO_URI")
DATABASE_NAME = os.getenv("DATABASE_NAME")

# Conectar a MongoDB Atlas
client = MongoClient(MONGO_URI)
db = client[DATABASE_NAME]

# Función para insertar datos en la colección
def insert_data(collection_name, data):
    collection = db[collection_name]
    result = collection.insert_one(data)
    print(f"Documento insertado con ID: {result.inserted_id}")

# Función para consultar datos desde la colección
def query_data(collection_name, query):
    collection = db[collection_name]
    results = collection.find(query)
    for document in results:
        print(document)

# Ejecutar las funciones como ejemplo
if __name__ == "__main__":
    # Insertar un documento de ejemplo
    print("Insertando datos...")
    insert_data("productos", {
        "nombre": "Teléfono Móvil",
        "precio": 750,
        "categoria": "Electrónica",
        "marca": "Samsung",
        "stock": 25
    })

    # Consultar documentos de ejemplo
    print("\nConsultando datos:")
    query_data("productos", {"categoria": "Electrónica"})
