const jwt = require('jsonwebtoken');
require('dotenv').config();

const generateAccessToken = (user) => {
    console.log(user)
    return jwt.sign(user.toJSON(), process.env.ACCESS_TOKEN_SECRET, { expiresIn: '1800s' });
}

module.exports = { generateAccessToken }