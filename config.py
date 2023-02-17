import re, os

id_pattern = re.compile(r'^.\d+$') 

API_ID = os.environ.get("API_ID", "28174152")

API_HASH = os.environ.get("API_HASH", "9f87e0e7706715122a4c95404cf510b9")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "6113683154:AAEE-1cYGF8em7wed56XVdU1J7uHKMbA20Y") 

FORCE_SUB = os.environ.get("FORCE_SUB", "S2kMovies") 

DB_NAME = os.environ.get("DB_NAME","Cluster0")     

DB_URL = os.environ.get("DB_URL","mongodb+srv://Santhosh:soniya@cluster0.mtz5pve.mongodb.net/?retryWrites=true&w=majority")
 
FLOOD = int(os.environ.get("FLOOD", "10"))

START_PIC = os.environ.get("START_PIC", "https://graph.org/Rename-Bot-01-15")

ADMIN = [int(admin) if id_pattern.search(admin) else admin for admin in os.environ.get('ADMIN', '2014579187').split()]

PORT = os.environ.get("PORT", "8080")
