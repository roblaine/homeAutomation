import os
from dotenv import load_dotenv


load_dotenv(verbose=True)

PROJECT_ID = os.environ.get('PROJECT_ID')

# Define the configuration for connection to the cloudsql db
CLOUDSQL_USER = os.environ.get('DB_USER')
CLOUDSQL_PASSWORD = os.environ.get('DB_PASS')
CLOUDSQL_DATABASE = os.environ.get('DB_NAME')
CLOUDSQL_ADDRESS = os.environ.get('CLOUDSQL_ADDRESS')

# Whether running in prod or dev
ENV = os.environ.get('ENV')

# Local SQLITE3 database
LOCAL_SQLALCHEMY_DATABASE_URI = (
  'sqlite:///src/db/dev.db'
)

# Connect directly via the ipv4 address
LIVE_SQLALCHEMY_DATABASE_URI = (
  'mysql+pymysql://{user}:{password}@{cloud_sql_address}/{database}').format(
  user=CLOUDSQL_USER, password=CLOUDSQL_PASSWORD,
  cloud_sql_address=CLOUDSQL_ADDRESS, database=CLOUDSQL_DATABASE)

# Set the Database URI to the local or live URI
if os.environ.get('ENV') == 'production':
  SQLALCHEMY_DATABASE_URI = LIVE_SQLALCHEMY_DATABASE_URI
else:
  SQLALCHEMY_DATABASE_URI = LOCAL_SQLALCHEMY_DATABASE_URI
