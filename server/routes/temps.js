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

// GET all temps
router.get('/', function(req, res, next) {
  db.many('SELECT * FROM TEMPERATURES')
    .then(function (data) {
      console.log('DATA:', data)
      // Return the json data
      res.json({
        data: data
      });
    })
    .catch(function (error) {
      console.log('ERROR:', error)
    })

});

// GET temperature by id
router.get('/:id', function(req, res, next) {
  db.any('SELECT * FROM TEMPERATURES WHERE ID = $1', [req.params.id])
    .then(function(data) {
      console.log('DATA:', data)
      // Return the data
      res.json({
        data: data
      })
    })
    .catch(function(error) {
      console.log('ERROR:', error)
    });
});

// POST temperature to the server
router.post('/:id', function(req, res, next) {

});

module.exports = router;
