const express = require('express');
const bodyParser = require('body-parser');
const cors = require('cors');
const app = express();
const {crawlCryptoData} = require('../controllers/crypto.controller');

crawlCryptoData();

// var corsOptions = {
// 	origin: 'http://localhost:8080'
// };

app.use(cors(/*corsOptions*/));

// parse requests of content-type - application/json
app.use(bodyParser.json());

// parse requests of content-type - application/x-www-form-urlencoded
app.use(bodyParser.urlencoded({extended: true}));

// const db = require('../models');
// drop the table if it already exists
// db.sequelize.sync({force: true}).then(() => {
// 	console.log('Drop and re-sync db.');
// });

// simple route
app.get('/', (req, res) => {
	res.json({message: 'Welcome to count money application.'});
});

require('../routes/user.routes')(app);
require('../routes/fav.routes')(app);
require('../routes/crypto.routes')(app);

// set port, listen for requests
const PORT = process.env.PORT || 8080;
app.listen(PORT, () => {
	console.log(`Server is running on port http://localhost/${PORT}.`);
});
