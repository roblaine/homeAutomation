const axios = require('axios');
const router = require('express').Router();
require('../config/config');

router.get('/', (req, res) => {
  const base64Auth = Buffer.from(
    process.env.SPOTIFY_CLIENT_ID + ':' + process.env.SPOTIFY_CLIENT_SECRET,
  ).toString('base64');
  const headers = {
    Authorization: 'Basic ' + base64Auth,
    'Content-Type': 'application/x-www-form-urlencoded',
    Accept: 'application/json',
  };

  const data = {
    grant_type: 'client_credentials',
  };

  console.log(headers);

  axios({
    url: 'https://accounts.spotify.com/api/token',
    method: 'post',
    data,
    headers,
  })
    .then(function(response) {
      console.log('Response: ');

      console.log(response);
      res.json({ response });
    })
    .catch(function(error) {
      // console.log(error);
    });
});

module.exports = router;
