"""
Script principal para ejecutar la aplicación Flask.
"""
import os
from musica_api import create_app
from dotenv import load_dotenv

# TODO: Cargar variables de entorno desde archivo .env si existe
load_dotenv()

# TODO: crear la aplicación
app = create_app()

if __name__ == "__main__":
    # TODO: Obtener puerto del ambiente o usar 5000 por defecto
    port = int(os.environ.get("PORT", 5000))
    
    # TODO: Determinar si se debe usar modo debug
    debug_mode = os.environ.get("FLASK_DEBUG", "False").lower() == "true"
    # TODO: Ejecutar aplicación
    app.run(host="0.0.0.0", port=port, debug=debug_mode)
    pass
 