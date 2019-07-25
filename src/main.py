from config import *
from db.database import *


def run():
  print('Running the app `{}` in `{}` mode'.format(PROJECT_ID, ENV))
  init_db()

if __name__ == '__main__':
  run()
