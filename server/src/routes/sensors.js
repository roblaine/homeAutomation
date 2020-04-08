const router = require('express').Router();
const { db } = require('../db/connection');

// SQL to reseed the DB
// INSERT INTO sensors (location, sensor_type, uid) VALUES
//    ("Bedroom", "DS18B20", "28-0214685409ff");
// INSERT INTO sensors (location, sensor_type, uid) VALUES
//    ("Bedroom", "DS18B20", "28-03146d2bb7ff");

// Get the sensor info by UID
router.post('/find', (req, res) => {
  db.query(`SELECT * FROM sensors WHERE uid = '${req.body.uid}'`, (err, data) => {
    if (err) {
      throw (err);
    }
    res.json({ data });
  });
});

module.exports = router;
