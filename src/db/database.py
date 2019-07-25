import sqlalchemy as db

def init_db():
  engine = db.create_engine('sqlite:///dev.db', echo=True)
  connection = engine.connect()
  metadata = db.MetaData()

  """
  Create all of the database tables required for the app
  """
  temperatures = db.Table('temperatures',
                          metadata,
                          db.Column('id', db.Integer()),
                          db.Column('location', db.String(255), nullable=False), # Location of sensor
                          db.Column('sensor_id', db.String(255), nullable=False), # Id of sensor
                          db.Column('temperature', db.Float(), nullable=False), #temperature in celsius
                          db.Column('time', db.Integer(), nullable=False) # Time as seconds from epoch
                        )

  metadata.create_all(engine)
