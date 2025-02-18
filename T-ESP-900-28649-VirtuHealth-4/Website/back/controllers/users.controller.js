const usersModel = require('../models/users');
const { generateAccessToken } = require('../utils/sign-jwt');


exports.getAllUsers = async (req, res) => {
    const users = await usersModel.find({});

    try {
        res.send(users);
    } catch (error) {
        res.status(500).send(error);
    }
}
exports.getUser = async (req, res) => {
    const users = await usersModel.findOne({ _id: req.params.id });

    try {
        res.send(users);
    } catch (error) {
        res.status(500).send(error);
    }
}
exports.createUser = async (req, res) => {
    console.log(req.body)
    const user = await usersModel.create(req.body);

    try {
        res.send(user);
    } catch (error) {
        res.status(500).send(error);
    }
}
exports.deleteUser = async (req, res) => {
    try {
        const user = await usersModel.deleteOne({ _id: req.params.id });
        res.send(user);
    } catch (error) {
        res.status(500).send(error);
    }
}
exports.updateUser = async (req, res) => {
    try {
        const user = await usersModel.updateOne({ _id: req.params.id }, req.body);
        res.send(user);
    } catch (error) {
        res.status(500).send(error);
    }
}
exports.logIn = async (req, res) => {
    const { email, password } = req.body
    const user = await usersModel.findOne({ email })

    if (!user || password != user.password) {
        res.status(401).send({ message: "wrong email or password" })
    }
    console.log(user)
    const accessToken = generateAccessToken(user);
    res.send({
        accessToken,
    })
};
