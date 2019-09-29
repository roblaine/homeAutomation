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
  db.many('SELECT * FROM TEMPERATURES')
    .then(function (data) {
      console.log('DATA:', data)
      res.json({
        message: data
      });
    })
    .catch(function (error) {
      console.log('ERROR:', error)
    })

});

router.get('/:id', function(req, res, next) {
  db.any('SELECT * FROM TEMPERATURES WHERE ID = $1', [req.params.id])
    .then(function(data) {
      console.log(data)
    })
    .catch(function(error) {
      console.log(error)
    });
    res.json({data: data})
});

module.exports = router;
