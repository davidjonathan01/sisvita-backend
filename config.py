from dotenv import load_dotenv
import os

load_dotenv()

# Obtener las variables de entorno
pwd = os.getenv('PASSWORD')
user = os.getenv('USER')
host = os.getenv('HOST')
database = os.getenv('DATABASE')
server = os.getenv('SERVER')

# Formar la cadena de conexión
DATABASE_CONNECTION = f'{server}://{user}:{pwd}@{host}/{database}'