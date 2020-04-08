require('dotenv').config();

module.exports = {
  dbAddr: process.env.DB_ADDR,
  dbPort: process.env.DB_PORT,
  dbUser: process.env.DB_USER,
  dbName: process.env.DB_NAME,
  dbPassword: process.env.DB_PASS,
};
