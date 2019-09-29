var express = require('express');
var router = express.Router();
var pgp = require('pg-promise')(/* options */)
var db = pgp('postgres://postgres@localhost:5432/postgres')

/* GET temps listing. */
router.get('/', function(req, res, next) {

  db.one('SELECT $1 AS value', 123)
  .then(function (data) {
    console.log('DATA:', data.value)
  })
  .catch(function (error) {
    console.log('ERROR:', error)
  })

  res.send('{"message": "Did some db stuff"}');
});

router.get('/:id', function(req, res, next) {
  db.one('SELECT $1 AS value', req.params.id)
  .then(function(data) {
    // Construct the return object

  })
  .catch(function (error) {
    console.log('ERROR:', error)
  })
  // Respond with the object that was requested
  res.send(`{"id":"${req.params.id}", "data": "${data.value}"}`)
});

module.exports = router;
