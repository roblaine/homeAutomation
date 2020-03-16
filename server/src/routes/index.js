const express = require('express');

const router = express.Router();

/* GET home page. */
router.get('/', (req, res, next) => {
  res.json({ message: 'Invalid route. For a list of routes that are available' });
});

module.exports = router;
