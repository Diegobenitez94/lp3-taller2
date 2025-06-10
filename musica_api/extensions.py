"""
Módulo de extensiones para la aplicación Flask.
Define las instancias de las extensiones utilizadas en todo el proyecto.
"""
from flask import Flask
from flask_sqlalchemy import SQLAlchemy 
from flask_restx import Api

app = Flask(__name__)

# API RESTful con documentación Swagger integrada
api = Api(
    title="API de Música",
    version="1.0",
    description="API para gestionar Usuarios, Canciones y Favoritos",
    doc="/docs"
)

api.init_app(app)

# ORM para interactuar con la base de datos
# FIXME: el objeto está mal inicializado

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mibasededatos.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


if __name__ == '__main__':
    app.run(debug=True)