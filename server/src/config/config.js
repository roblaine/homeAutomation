var env_vars = require('dotenv').config({ path: './.env' })
console.log(env_vars)
module.exports = env_vars
