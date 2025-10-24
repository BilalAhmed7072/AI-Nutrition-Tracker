import os
from dotenv import load_dotenv


load_dotenv()


OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
EDAMAM_APP_ID = os.getenv("EDAMAM_APP_ID")
EDAMAM_APP_KEY = os.getenv("EDAMAM_APP_KEY")
NUTRITIONIX_APP_ID = os.getenv("NUTRITIONIX_APP_ID")
NUTRITIONIX_APP_KEY = os.getenv("NUTRITIONIX_APP_KEY")
VECTOR_DB_PATH = os.getenv("VECTOR_DB_PATH", "data/diet_vector_db")


# Set OPENAI env for some libs
os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY or ""