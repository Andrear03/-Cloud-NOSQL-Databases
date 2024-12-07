# Cloud NoSQL Databases - MongoDB Atlas Connection with Python

## Descripción

Este proyecto demuestra cómo conectar una aplicación en **Python** a una base de datos en **MongoDB Atlas**, utilizando `pymongo` y `dotenv` para manejar las credenciales de forma segura. Incluye ejemplos de inserción y consulta de datos desde la colección `comments` en la base de datos de ejemplo `sample-mflix`.

---

## Requisitos

Antes de comenzar, asegúrate de cumplir con los siguientes requisitos:

- **Python** 3.6 o superior
- **MongoDB Atlas** configurado y accesible (con un clúster y base de datos creados)
- Un entorno virtual de Python (opcional, pero recomendado)

---

## Instalación

1. **Clonar el repositorio**
   ```bash
   git clone https://github.com/tu_usuario/tu_repositorio.git
   cd -Cloud-NOSQL-Databases
Crear y activar un entorno virtual

    En Windows:

python -m venv venv
venv\Scripts\activate

En macOS/Linux:

    python3 -m venv venv
    source venv/bin/activate

Instalar dependencias

pip install -r requirements.txt

Configurar las variables de entorno

    Crea un archivo .env en el directorio raíz del proyecto.
    Agrega lo siguiente, reemplazando <usuario>, <contraseña> y <tu-cluster> con tus credenciales de MongoDB Atlas:

        MONGO_URI=mongodb+srv://<usuario>:<contraseña>@<tu-cluster>.mongodb.net/?retryWrites=true&w=majority
        DATABASE_NAME=sample-mflix

Uso

    Ejecutar la aplicación

    python app.py

    Resultados esperados
        Se insertará un nuevo documento en la colección comments.
        Se listarán los primeros 5 documentos de la colección comments en la consola.

Estructura del Proyecto

-Cloud-NOSQL-Databases/
├── venv/                   # Entorno virtual (ignorado en el repositorio)
├── .env                    # Variables de entorno (ignorado en el repositorio)
├── .gitignore              # Archivos a ignorar por Git
├── README.md               # Documentación del proyecto
├── requirements.txt        # Dependencias del proyecto
├── app.py                  # Código principal de la aplicación

Ejemplo de Código
Inserción de Datos

def insert_comment():
    collection = db["comments"]  # Selecciona la colección
    result = collection.insert_one({
        "name": "Jane Doe",
        "email": "jane.doe@example.com",
        "text": "This is a new comment.",
        "date": "2024-01-01T00:00:00.000Z"
    })
    print(f"Documento insertado con ID: {result.inserted_id}")

Consulta de Datos

def get_comments():
    collection = db["comments"]  # Selecciona la colección
    results = collection.find().limit(5)  # Obtén los primeros 5 documentos
    for comment in results:
        print(comment)

Contribución

Si deseas contribuir al proyecto:

    Haz un fork del repositorio.
    Crea una rama para tu funcionalidad (git checkout -b feature/nueva-funcion).
    Realiza tus cambios y haz un commit (git commit -m "Añadir nueva funcionalidad").
    Sube tus cambios a tu fork (git push origin feature/nueva-funcion).
    Abre un Pull Request en este repositorio.

Licencia

Este proyecto está bajo la licencia MIT. Puedes consultar el archivo LICENSE para más información.
Autor

Desarrollado por Diego Andrés Oro como parte de la práctica sobre bases de datos NoSQL en la nube.
Referencias

    MongoDB Atlas Documentation
    Pymongo Documentation


Este README proporciona una guía clara y completa sobre tu proyecto. Solo necesitas ajustar el enlace del r
