const mysql = require('mysql');
const {
  dbAddr, dbPort, dbUser, dbName, dbPassword,
} = require('../config/config');

const db = mysql.createConnection({
  host: dbAddr,
  port: dbPort,
  database: dbName,
  user: dbUser,
  password: dbPassword,
});

module.exports = {
  db,
};
