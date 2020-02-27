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
	db.query('SELECT * FROM temps', function(err, rows, fields) {
		if (err) throw err

		res.json({rows});
	});

/*
	db.many('SELECT * FROM TEMPERATURES')
    .then(function (data) {
      console.log('DATA:', data)
      // Return the json data
      res.json({
        data
      });
    })
    .catch(function (error) {
      console.log('ERROR:', error)
    })
*/
});

// GET temperature by id
router.get('/:id', function(req, res, next) {

  if(typeof req.params.id != 'number') {
    res.json({
      message: `${req.params.id} is not a number`
    })
  }

  db.any('SELECT * FROM TEMPERATURES WHERE ID = $1', [req.params.id])
    .then(function(data) {
      console.log('DATA:', data)
      // Return the data
      res.json({
        data
      })
    })
    .catch(function(error) {
      console.log('ERROR:', error)
    });
});

// POST temperature to the server
router.post('/new', function(req, res, next) {
  // Validate that the posted object is correct
  console.log(req.body);
  // console.log(req.params.length);

  if(!req.body || req.body.length < 2) {
    res.json({
      error: "Must have 2 args"
    });
  }

  db.one('INSERT INTO TEMPERATURES(temperature, location) VALUES($1, $2) RETURNING *', [req.body.temperature, req.body.location])
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
