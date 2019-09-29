var express = require('express');
var router = express.Router();
const initOptions = {/* initialization options */};
var pgp = require('pg-promise')(initOptions)
const cn = {
  host: 'localhost',
  port: 5432,
  database: 'postgres',
  user: 'postgres',
  password: ''
}
var db = pgp(cn)

/* GET temps listing. */
router.get('/', function(req, res, next) {
  db.one('SELECT $1 AS value', 123)
    .then(function (data) {
      console.log('DATA:', data.value)
    })
    .catch(function (error) {
      console.log('ERROR:', error)
    })

  res.json({
    message: "Did some db stuff"
  });
});

router.get('/:id', function(req, res, next) {
  db.any('SELECT * FROM temps WHERE id = $1', [req.params.id])
    .then(function(data) {
      console.log(data)
    })
    .catch(function(error) {
      console.log(error)
    });
    res.json({data: data})
});

module.exports = router;
