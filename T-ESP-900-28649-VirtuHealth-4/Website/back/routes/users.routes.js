const express = require("express");
const router = express.Router();
const controller = require('../controllers/users.controller');
const { authenticateToken } = require("../middlewares/authenticate-jwt");
router.get("/all", controller.getAllUsers);
router.get("/:id", controller.getUser);
router.post('/create', controller.createUser)
router.delete('/delete/:id', controller.deleteUser)
router.put('/update', authenticateToken, controller.updateUser)
router.post('/login', controller.logIn)
module.exports = router;