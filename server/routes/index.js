var express = require('express');
var router = express.Router();

/* GET home page. */
router.get('/', function(req, res, next) {
  res.json({ message: 'Invalid route. For a list of routes that are available' });
});

module.exports = router;
