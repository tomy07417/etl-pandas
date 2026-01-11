import os
from dotenv import load_dotenv

load_dotenv()

REGION = os.getenv("REGION")
AWS_ACCESS_KEY_ID = os.getenv("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = os.getenv("AWS_SECRET_ACCESS_KEY")
BUCKET_NAME = os.getenv("BUCKET_NAME")

if not AWS_ACCESS_KEY_ID:
    raise ValueError("AWS_ACCESS_KEY_ID no configurado. Creá un archivo .env")

if not AWS_SECRET_ACCESS_KEY:
    raise ValueError("AWS_SECRET_ACCESS_KEY no configurado. Creá un archivo .env")

if not REGION:
    raise ValueError("REGION no configurado. Creá un archivo .env")

if not BUCKET_NAME:
    raise ValueError("BUCKET_NAME no configurado. Creá un archivo .env")