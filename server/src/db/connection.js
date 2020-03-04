var mysql = require('mysql')
var env_vars = require('../config/config').parsed

module.exports.db = mysql.createConnection({
  host: env_vars.DB_ADDR,
  port: 3306,
  database: env_vars.DB_DB,
  user: env_vars.DB_USER,
  password: env_vars.DB_PASS
})
