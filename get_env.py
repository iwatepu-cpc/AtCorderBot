import os
import os.path
import dotenv

dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
dotenv.load_dotenv(dotenv_path)

API_KEY = os.environ.get("ACBOT_KEY")
WEBHOOK1 = os.environ.get("WEBHOOK1")
WEBHOOK2 = os.environ.get("WEBHOOK2")