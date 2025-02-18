const cryptos = require("../controllers/crypto.controller.js");
module.exports = app => {
    const cryptos = require("../controllers/crypto.controller.js");

    const router = require("express").Router();

    // Retrieve all Cryptos
    router.get("/", cryptos.findAll);

    // Retrieve all Cryptos name and id
    router.get("/list", cryptos.findAllIdNameOnly);

    // Retrieve a single Crypto with cmid
    router.get("/:id", cryptos.findOne);

    router.get('/crawl', cryptos.crawlCryptoData);

    // Retrieve a single Crypto history over a period
    router.get("/:cmid/history/:period", cryptos.getOHLCPeriod);

    // Update a Crypto with cmid
    router.put("/:cmid", cryptos.update);

    // Delete a Crypto with cmid
    router.delete("/:id", cryptos.deleteCrypto);

    // Create a new Crypto
    router.post("/", cryptos.create);

    // Delete all Cryptos
    router.delete("/", cryptos.deleteAll);

    app.use("/api/cryptos", router);
};