import config
import db.database as db
import temp_sense.temp as temp


def run():
  print('Running the app `{}` in `{}` mode'.format(config.PROJECT_ID, config.ENV))
  db.init_db()
  # Log the current temperature into the database
  timestamp, curr_temp, location = temp.read_temp()
  print('\n{}\n{}\n{}\n'.format(timestamp, curr_temp, location))
  temp.save_to_db(timestamp=timestamp, temp_val=curr_temp, location=location)

if __name__ == '__main__':
  run()
