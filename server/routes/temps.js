var express = require('express');
var router = express.Router();
var mysql = require('mysql')

var db = mysql.createConnection({
  host: 'localhost',
  port: 3306,
  database: 'mysql_db',
  user: 'admin',
  password: 'admin_password'
})

db.connect()
db.query('CREATE TABLE IF NOT EXISTS temps(id int NOT NULL AUTO_INCREMENT, temperature float NOT NULL, location VARCHAR(50) NOT NULL, recorded_at TIMESTAMP NOT NULL, primary key(id));')

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

  db.query(`INSERT INTO temps(temperature, location, recorded_at) VALUES(${req.body.temperature}, ${req.body.location}, ${req.body.recorded_at})`, function(err, data, fields) {
    if (err) {
      console.log(err);
    }
    res.json({
      data
    })

  });

});

module.exports = router;
