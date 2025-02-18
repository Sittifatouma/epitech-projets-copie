const db = require("../models");
const {CoinGeckoClient} = require("coingecko-api-v3");
const Crypto = db.cryptos;
const Op = db.Sequelize.Op;
const fetch = (...args) => import('node-fetch').then(({default: fetch}) => fetch(...args));



// Create and Save a new Crypto
async function create(req, res) {
    // Validate request
    if (!req.body.cmid) {
        res.header('Access-Control-Allow-Origin', '*')
        res.status(400).send({
            message: "Content can not be empty!"
        });
        return;
    }
    // Create a Crypto
    const crypto = {
        cmid: req.body.cmid,
        full_name: req.body.full_name,
        current_price: req.body.current_price,
        opening_price: req.body.opening_price,
        highest_price: req.body.highest_price,
        lowest_price: req.body.lowest_price,
        icon_url: req.body.icon_url,

    };

    // Save Crypto in the database
    Crypto.create(crypto)
        .then(data => {
            res.header('Access-Control-Allow-Origin', '*')
            res.send(data);
        })
        .catch(err => {
            res.header('Access-Control-Allow-Origin', '*')
            res.status(500).send({
                message:
                    err.message || "Some error occurred while creating the Crypto."
            });
        });
};

// Retrieve all crypto name and id from the database.
async function findAllIdNameOnly(req, res) {
    const cmid = req.query.cmid;
    var condition = cmid ? {cmid: {[Op.iLike]: `%${cmid}%`}} : null;

    Crypto.findAll({where: condition, attributes: ['id', 'full_name']})
        .then(data => {
            res.header('Access-Control-Allow-Origin', '*')
            res.send(data);
        })
        .catch(err => {
            res.header('Access-Control-Allow-Origin', '*')
            res.status(500).send({
                message:
                    err.message || "Some error occurred while retrieving tutorials."
            });
        });
};

// Retrieve all crypto from the database.
async function findAll(req, res) {
    const cmid = req.query.cmid;
    var condition = cmid ? {cmid: {[Op.iLike]: `%${cmid}%`}} : null;
    Crypto.findAll({where: condition})
        .then(data => {
            res.header('Access-Control-Allow-Origin', '*')
            res.send(data);
        })
        .catch(err => {
            res.header('Access-Control-Allow-Origin', '*')
            res.status(500).send({
                message:
                    err.message || "Some error occurred while retrieving tutorials."
            });
        });
};

// Find a single crypto with an id
async function findOne(req, res) {
    const id = req.params.id;

    Crypto.findByPk(id)
        .then(data => {
            res.header('Access-Control-Allow-Origin', '*')
            res.send(data);
        })
        .catch(err => {
            res.header('Access-Control-Allow-Origin', '*')
            res.status(500).send({
                message: "Error retrieving Crypto with id=" + id
            });
        });
};

// Update a crypto by the id in the request
async function update(req, res) {
    const id = req.params.id;

    Crypto.update(req.body, {
        where: {id: id}
    })
        .then(num => {
            if (num == 1) {
                res.header('Access-Control-Allow-Origin', '*')
                res.send({
                    message: "Crypto was updated successfully."
                });
            } else {
                res.header('Access-Control-Allow-Origin', '*')
                res.send({
                    message: `Cannot update Crypto with id=${id}. Maybe Crypto was not found or req.body is empty!`
                });
            }
        })
        .catch(err => {
            res.header('Access-Control-Allow-Origin', '*')
            res.status(500).send({
                message: "Error updating Crypto with id=" + id
            });
        });
};

// Delete a crypto with the specified id in the request
async function deleteCrypto(req, res) {
    const id = req.params.id;

    Crypto.destroy({
        where: {id: id}
    })
        .then(num => {
            if (num == 1) {
                res.header('Access-Control-Allow-Origin', '*')
                res.send({
                    message: "Crypto was deleted successfully!"
                });
            } else {
                res.header('Access-Control-Allow-Origin', '*')
                res.send({
                    message: `Cannot delete Crypto with id=${id}. Maybe Crypto was not found!`
                });
            }
        })
        .catch(err => {
            res.header('Access-Control-Allow-Origin', '*')
            res.status(500).send({
                message: "Could not delete Crypto with id=" + id
            });
        });
};

// Delete all Cryptos from the database.
async function deleteAll(req, res) {
    Crypto.destroy({
        where: {},
        truncate: false
    })
        .then(nums => {
            res.header('Access-Control-Allow-Origin', '*')
            res.send({message: `${nums} Crypto were deleted successfully!`});
        })
        .catch(err => {
            res.header('Access-Control-Allow-Origin', '*')
            res.status(500).send({
                message:
                    err.message || "Some error occurred while removing all cryptos."
            });
        });
};

// Test route
async function getOHLCPeriod(req, res) {
    const cmid = req.params.cmid;
    const period = req.params.period;
    const resolution = {
        'minute': 1,
        'hourly': 60,
        'daily': 'D'
    };
    let now = new Date(Date.now());
    const date = {
        'now': parseInt((now.getTime() / 1000).toFixed(0)),
        'minute': parseInt((new Date(now.setHours(now.getHours() - 2)).getTime() / 1000).toFixed(0)),
        'hourly': parseInt((new Date(now.setDate(now.getDate() - 2)).getTime() / 1000).toFixed(0)),
        'daily': parseInt((new Date(now.setMonth(now.getMonth() - 2)).getTime() / 1000).toFixed(0))

    }
    const urlBase = 'https://finnhub.io/api/v1/crypto/candle'
    const token = 'c6tnd9qad3ibuuho5en0';
    const symbol = `BINANCE:${cmid.toUpperCase()}EUR`;
    const url = `${urlBase}?symbol=${symbol}&resolution=${resolution[period]}&from=${date[period]}&to=${date.now}&token=${token}`

    const response = await fetch(url)
    const data = await response.json();
    res.header('Access-Control-Allow-Origin', '*')
    res.send(data);
};

async function crawlCryptoData(req, res) {
    let filter = []
    await Crypto.findAll()
        .then(data => {
            for (let i = 0; i < data.length; i++) {
                filter.push({
                    id: data[i].id,
                    full_name: data[i].full_name
                })
                console.log(filter)
            }
        })
        .catch(err => {
            console.log(err.message || "Some error occurred while retrieving tutorials.");
        });

    const ohlc = {
        open: 1,
        high: 2,
        low: 3,
        close: 4,
    }
    const client = new CoinGeckoClient({
        timeout: 0,
        autoRetry: true,
    });


    for (let cCount = 0; cCount < filter.length; cCount++) {
        let params = {
            id: filter[cCount].full_name,
            vs_currency: 'eur',
            days: 1
        }

        let data = await client.coinIdOHLC(params);

        let date,
            open,
            highest,
            lowest,
            close

        for (let k = 0; k < data.length; k++) {
            data[k][0] = new Date(data[k][0]);
            if (k === 1) {
                date = new Date(data[k][0]);
                open = data[k][ohlc.open];
                highest = data[k][ohlc.high];
                lowest = data[k][ohlc.low];
            }
            if (k === data.length - 1) {
                close = data[k][ohlc.close];
            }
            if (highest < data[k][ohlc.high]) {
                highest = data[k][ohlc.high];
            }
            if (lowest > data[k][ohlc.low]) {
                lowest = data[k][ohlc.low];
            }
        }

        let final = {
            date: date,
            open: open,
            highest: highest,
            lowest: lowest,
            close: close
        }


        console.log('Crawled ' + filter[cCount].full_name)
        // Create a Crypto
        const crypto = {
            current_price: final.close,
            opening_price: final.open,
            highest_price: final.highest,
            lowest_price: final.highest,
        };

        console.log(filter[cCount].id)
        // Save Crypto in the database
        Crypto.update(crypto, {
            where: {id: filter[cCount].id}
        })
            .then(num => {
                if (num == 1) {
                    console.log({
                        message: "Crypto was updated successfully."
                    });
                } else {
                    console.log({
                        message: `Cannot update Crypto with id=${id}. Maybe Crypto was not found or req.body is empty!`
                    });
                }
            })
            .catch(err => {
                console.log(err.message || "Some error occurred while creating the Crypto.")
            });
    }
    // setTimeout(crawlCryptoData, 1800000);
};

exports.create = create
exports.findAll = findAll
exports.findOne = findOne
exports.findAllIdNameOnly = findAllIdNameOnly
exports.crawlCryptoData = crawlCryptoData
exports.getOHLCPeriod = getOHLCPeriod
exports.update = update
exports.deleteCrypto = deleteCrypto
exports.deleteAll = deleteAll
