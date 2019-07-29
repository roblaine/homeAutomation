import config
import db.database as db
import temp_sense.temp as temp
import time


def run():
  print('Running the app `{}` in `{}` mode'.format(config.PROJECT_ID, config.ENV))
  db.init_db()
  while True:
    # Log the current temperature into the database
    timestamp, curr_temp, location = temp.read_temp()
    print('\n{}\n{}\n{}\n'.format(timestamp, curr_temp, location))
    temp.save_to_db(timestamp=timestamp, temp_val=curr_temp, location=location)
    # Wait 60 seconds
    time.sleep(60)

if __name__ == '__main__':
  run()
