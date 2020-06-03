const mysql = require('mysql');
require('../config/config');

if (process.env.ENV === 'dev') {
  console.log('Running in development env, not exporting DB...');

  module.exports.db = null;
  return;
}

module.exports.db = mysql.createConnection({
  host: process.env.DB_ADDR,
  port: process.env.DB_PORT,
  database: process.env.DB_NAME,
  user: process.env.DB_USER,
  password: process.env.DB_PASS,
});
