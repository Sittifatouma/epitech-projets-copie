module.exports = app => {
    const users = require("../controllers/user.controller.js");

    const router = require("express").Router();

    // Create a new User
    router.post("/", users.create);

    router.post("/createWithoutOnlyMail", users.createWithoutOnlyMail)

    // Retrieve all Users
    router.get("/", users.findAll);


    // Retrieve a single User with id
    router.get("/:id", users.findOne);

    // Update a User with id
    router.put("/:id", users.update);

    // Delete a User with id
    router.delete("/:id", users.deleteUser);

    // Delete all Users
    router.delete("/", users.deleteAll);

    // Login User
    router.post("/login", users.login)

    // Register as Oauth
    router.get("/oaut2/register", users.oAuth2Register)

    // Redirect from Oauth2
    router.get("/redirect/google", users.oAuth2Redirect)
    app.use("/api/users", router);
};
