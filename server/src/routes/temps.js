const express = require('express');

const router = express.Router();
const mysql = require('mysql');
const { db } = require('../db/connection');

db.connect();

db.query('CREATE TABLE IF NOT EXISTS temps(id int NOT NULL AUTO_INCREMENT, temperature float NOT NULL, location VARCHAR(50) NOT NULL, recorded_at TIMESTAMP NOT NULL, primary key(id));');

// GET all temps
router.get('/', (req, res, next) => {
  db.query('SELECT * FROM temps', (err, data, fields) => {
    if (err) {
      console.log(err);
      throw (err);
    }

    res.json({ temps: data });
  });
});

// GET temperature by id
router.get('/:id', (req, res, next) => {
  if (isNaN(req.params.id)) {
    res.json({
      error: `Id must be an integer, instead was ${typeof req.params.id}`,
    });
    return;
  }

  db.query(`SELECT * FROM temps WHERE ID = ${req.params.id}`,
    (err, data, fields) => {
      res.json({ data });
    });
});

// POST temperature to the server
router.post('/new', (req, res, next) => {
  // Validate that the posted object is correct
  console.log(req.params.length);
  // console.log(req.params.length);

  if (!req.body || req.body.length < 3) {
    res.json({
      error: 'Insert API query must have 3 args',
    });
  }

  db.query(`INSERT INTO temps(temperature, location, recorded_at) \
      VALUES(${req.body.temperature}, "${req.body.location}", "${req.body.recorded_at}")`,
  (err, data, fields) => {
    if (err) {
      console.log(err);
    }
    res.json({
      data,
    });
  });
});

module.exports = router;
