from pathlib import Path
from dotenv import load_dotenv
import os

# project configuration from .env (secret part)
env_path = Path(__file__).resolve().parent / '.env'
load_dotenv(dotenv_path=env_path)  # loads into os.environ
api_key = os.getenv("API_KEY")


# project configuration
DATA_DIR = "../data"
RESULTS_DIR = "../results"




