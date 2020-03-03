import os
from dotenv import load_dotenv


load_dotenv(verbose=True)

PROJECT_ID = os.environ.get('PROJECT_ID')
SERVER = os.environ.get('SERVER')
ENV = os.environ.get('ENV')
