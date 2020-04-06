const router = require('express').Router();
const { db } = require('../db/connection');

db.connect();

// db.query('CREATE TABLE IF NOT EXISTS \
//     sensors(id int NOT NULL AUTO_INCREMENT, \
//     location VARCHAR(50) NOT NULL, \
//     primary key(id));');

// Get the sensor info by UID
router.get('/:uid', (req, res) => {
  console.log(req.body.uid);
  console.log(req.params.uid);
  db.query(`SELECT * FROM sensors WHERE uid = ${req.body.uid}`, (err, data) => {
    if (err) {
      console.log(err);
      throw (err);
    }
    res.json({ sensor: data });
  });
});
