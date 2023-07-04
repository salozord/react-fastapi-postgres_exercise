import os

# Load env variables to use. For now this is used as a custom 
# config file that can be transformed to pydantic Settings class or similar
BACK_NAME = os.getenv("BACK_NAME", "backend")
BACK_HOST = os.getenv("BACK_HOST", "0.0.0.0")
BACK_PORT = os.getenv("BACK_PORT", "8000")

DB_HOST = os.getenv("POSTGRES_HOST", "localhost")
DB_PORT = os.getenv("POSTGRES_PORT", "5432")
DB_USER = os.getenv("POSTGRES_USER", "admin")
DB_PASSWORD = os.getenv("POSTGRES_PASSWORD", "admin")
DB_DATABASE =os.getenv("POSTGRES_DB", "backend")