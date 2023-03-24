import os
from dotenv import load_dotenv

load_dotenv()

API_PORT = int(os.getenv('API_PORT', 5000))
QUEUE_FOLDER = os.getenv('QUEUE_FOLDER', './json_files/')
RUNPOD_API_BASE = os.getenv('RUNPOD_API_BASE', 'http://localhost:3000')
