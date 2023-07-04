import os

# Load env variables to use. For now this is used as a custom 
# config file that can be transformed to pydantic Settings class or similar
BACK_NAME = os.getenv("BACK_NAME")
BACK_HOST = os.getenv("BACK_HOST")
BACK_PORT = int(os.getenv("BACK_PORT"))

DB_HOST = os.getenv("POSTGRES_HOST")
DB_PORT = os.getenv("POSTGRES_PORT")
DB_USER = os.getenv("POSTGRES_USER")
DB_PASSWORD = os.getenv("POSTGRES_PASSWORD")
DB_DATABASE =os.getenv("POSTGRES_DB")