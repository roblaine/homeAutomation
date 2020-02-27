var express = require('express');
var router = express.Router();
var mysql = require('mysql')

var db = mysql.createConnection({
  host: '10.0.0.74',
  port: 3306,
  database: 'mysql_db',
  user: 'admin',
  password: 'admin_password'
})

db.connect()

// GET all temps
router.get('/', function(req, res, next) {
	db.query('SELECT * FROM temps', function(err, data, fields) {
		if (err) {
      console.log(err);
      throw (err);
    }

		res.json({ temps: data });
	});
});

// GET temperature by id
router.get('/:id', function(req, res, next) {

  if (isNaN(req.params.id)) {
    res.json({
      error: `Id must be an integer, instead was ${typeof req.params.id}`
    });
    return;
  };

  db.query(`SELECT * FROM temps WHERE ID = ${req.params.id}`,
      function(err, data, fields) {
    res.json({ data });
  });
});

// POST temperature to the server
router.post('/new', function(req, res, next) {
  // Validate that the posted object is correct
  console.log(req.body);
  // console.log(req.params.length);

  if (!req.body || req.body.length < 3) {
    res.json({
      error: "Insert API query must have 3 args"
    });
  }

  db.query('INSERT INTO temps(temperature, location, recorded_at) VALUES($1, $2, $3) RETURNING *', [req.body.temperature, req.body.location, time.now()])
    .then(data => {
      console.log('Created new temp object: ', data.id);
      res.json(data)
    })
    .catch(error => {
      console.log('ERROR:', error); // print error;
      res.json({
        error: `Failed to insert into database: ${error}`
      })
    });
});

module.exports = router;
