const fav = require("../controllers/fav.controller.js");
module.exports = app => {
    const fav = require("../controllers/fav.controller.js");

    const router = require("express").Router();

    // Retrieve all fav
    router.get("/", fav.findAll);   // OK

    // Retrieve a single fav with cmid
    router.get("/:id", fav.findOne); // OK

    // Update a fav with cmid
    router.put("/:id", fav.update); // OK

    // Delete a fav with cmid
    router.delete("/:id", fav.deleteFav); // OK

    // Create a new fav
    router.post("/", fav.create);   // OK

    // Delete all fav
    router.delete("/", fav.deleteAll); // OK

    app.use("/api/fav", router);
};