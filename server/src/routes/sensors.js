const router = require('express').Router();
const { db } = require('../db/connection');

db.connect();

db.query('CREATE TABLE IF NOT EXISTS \
    sensors(id int NOT NULL AUTO_INCREMENT, \
    location VARCHAR(50) NOT NULL, \
    primary key(id));');

router.get('/', (req, res, next) => {
  db.query('SELECT * FROM sensors', (err, data, fields) => {
    if (err) {
      console.log(err);
      throw (err);
    }
    res.json({ sensors: data });
  });
});
