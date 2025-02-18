const jwt = require('jsonwebtoken');
require('dotenv').config();




const generateRefreshToken = (user) => {
    return jwt.sign(user, process.env.REFRESH_TOKEN_SECRET, { expiresIn: '1y' });
}

const accessToken = generateAccessToken(user);
const refreshToken = generateRefreshToken(user);
res.send({
    accessToken,
    refreshToken,
});
module.exports = { generateRefreshToken }