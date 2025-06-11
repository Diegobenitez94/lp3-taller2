"""
Script principal para ejecutar la aplicación Flask.
"""
import os
import logging 
from dotenv import load_dotenv

from musica_api import create_app

logger = logging.getLogger(__name__)

logger.setLevel(logging.INFO)


console_handler = logging.StreamHandler()

formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(name)s - %(message)s')
console_handler.setFormatter(formatter)
logger.addHandler(console_handler)

# TODO: Cargar variables de entorno desde archivo .env si existe
env_path = '.env'
if os.path.isfile(env_path):
    load_dotenv(env_path)
    print("archivo .env cargado")
else:
    print("no existe el archivo .env")
    env_path = '.env'
if os.path.isfile(env_path):
    load_dotenv(env_path)
    logger.info("Archivo .env cargado exitosamente.")
else:
    logger.warning("No se encontró el archivo .env. Asegúrese de que las variables de entorno estén configuradas.")
# TODO: crear la aplicación
app = create_app()

if __name__ == "__main__":
    # TODO: Obtener puerto del ambiente o usar 5000 por defecto
    port = int(os.environ.get("PORT", 5000))
    
    # TODO: Determinar si se debe usar modo debug
    debug_mode = os.environ.get ("FLASK_DEBUG", "False").lower() == "true"
    
    # TODO: Ejecutar aplicación
    logger.info(f"Iniciando la aplicación Flask en http://0.0.0.0:{port} (Modo Debug: {debug_mode})")
    app.run(host="0.0.0.0", port=port, debug=debug_mode)
    pass
 