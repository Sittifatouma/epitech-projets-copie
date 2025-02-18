const db = require("../models");
const jwt = require('jsonwebtoken');
const bcrypt = require('bcrypt');
const User = db.users;
const Op = db.Sequelize.Op;
const saltRounds = 10;
const {google} = require('googleapis');


const oauth2Client = new google.auth.OAuth2(
    "701045814161-v0ja9jknuk7l75r0ig4n1vqnqelob1fd.apps.googleusercontent.com",
    "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",
    "http://localhost:4000/api/users/redirect/google"
  );

const scopes = [
'https://www.googleapis.com/auth/userinfo.email',
];

const GoogleUrl = oauth2Client.generateAuthUrl({
    scope : scopes
});

// Create and Save a new User

async function createWithoutOnlyMail (req, res) {
    if (!req.body.email) {
        res.header('Access-Control-Allow-Origin', '*')
        res.status(400).send({
            message: "Content can not be empty!"
        })
        return;
    }
    const user = {email: req.body.email}
    User.findOne({where: {email: user.email}})
        .then(userFind => {
            if (userFind) {
                res.header('Access-Control-Allow-Origin', '*')
                res.status(200).json({
                    userID: userFind.id,
                    token: jwt.sign(
                        {userId: userFind.id},
                        'RANDOM_TOKEN_SECRET',
                        { expiresIn: '24h' }
                    ) 
                })
            } else {
                User.create(user)
                    .then(data => {
                        res.header('Access-Control-Allow-Origin', '*')
                        res.status(201).json({
                            userID: data.dataValues.id,
                            token: jwt.sign(
                                {userId: data.dataValues.id},
                                'RANDOM_TOKEN_SECRET',
                                {expiresIn: "24h"}
                            )
                        })
                    })
                    .catch(err => {
                        res.header('Access-Control-Allow-Origin', '*')
                        res.status(500).send({
                            message:
                                err.message || "Some error occurred while creating the User."
                        });
                    });
            }
        })
};

async function create (req, res) {
    // Validate request
    if (!req.body.firstname) {
        res.header('Access-Control-Allow-Origin', '*')
        res.status(400).send({
            message: "Content can not be empty!"
        });
        return;
    }
    // Hash password
    bcrypt.hash(req.body.password, saltRounds, (err, hash) => {
        // Create a User
        const user = {
            firstname: req.body.firstname,
            lastname: req.body.lastname,
            email: req.body.email,
            password: hash,
            avatar: req.body.avatar
        };
        User.findOne({where: {email: user.email}})
            .then(userFind => {
                if (userFind) {
                    res.header('Access-Control-Allow-Origin', '*')
                    res.status(400).json({
                        message: "User already exist"
                    })
                } else {
                    User.create(user)
                        .then(data => {
                            res.header('Access-Control-Allow-Origin', '*')
                            res.status(201).json({
                                userId: data.dataValues.id,
                                token: jwt.sign(
                                  { userId: data.dataValues.id },
                                  'RANDOM_TOKEN_SECRET',
                                  { expiresIn: '24h' }
                                )
                            });
                        })
                        .catch(err => {
                            res.header('Access-Control-Allow-Origin', '*')
                            res.status(500).send({
                                message:
                                    err.message || "Some error occurred while creating the User."
                            });
                        });
                }
            })
        // Save User in the database
    })
};

// Retrieve all user from the database.
async function findAll (req, res) {
    if (req.headers.authorization)
    {
        const auth = req.headers.authorization.replace('Bearer ', '')
        try {
            decoded = jwt.verify(auth, 'RANDOM_TOKEN_SECRET');
            console.log(decoded)
        } catch (e) {
            console.log(e)
            res.header('Access-Control-Allow-Origin', '*')
            return res.status(401).send('unauthorized');
        }
    }
    const firstname = req.query.firstname;
    var condition = firstname ? { firstname: { [Op.iLike]: `%${firstname}%` } } : null;

    User.findAll({ where: condition })
        .then(data => {
            res.header('Access-Control-Allow-Origin', '*')
            res.send(data);
        })
        .catch(err => {
            res.header('Access-Control-Allow-Origin', '*')
            res.status(500).send({
                message:
                    err.message || "Some error occurred while retrieving User."
            });
        });
};

// Find a single user with an id
async function findOne (req, res) {
    const id = req.params.id;
    User.findByPk(id)
        .then(data => {
            res.header('Access-Control-Allow-Origin', '*')
            res.send(data);
        })
        .catch(err => {
            res.header('Access-Control-Allow-Origin', '*')
            res.status(500).send({
                message: "Error retrieving User with id=" + id
            });
        });
};

// Update a user by the id in the request
async function update (req, res) {
    const id = req.params.id;

    User.update(req.body, {
        where: { id: id }
    })
        .then(num => {
            if (num == 1) {
                res.header('Access-Control-Allow-Origin', '*')
                res.send({
                    message: "User was updated successfully."
                });
            } else {
                res.header('Access-Control-Allow-Origin', '*')
                res.send({
                    message: `Cannot update User with id=${id}. Maybe User was not found or req.body is empty!`
                });
            }
        })
        .catch(err => {
            res.header('Access-Control-Allow-Origin', '*')
            res.status(500).send({
                message: "Error updating User with id=" + id
            });
        });
};

// Delete a user with the specified id in the request
async function deleteUser (req, res) {
    const id = req.params.id;

    User.destroy({
        where: { id: id }
    })
        .then(num => {
            if (num == 1) {
                res.header('Access-Control-Allow-Origin', '*')
                res.send({
                    message: "User was deleted successfully!"
                });
            } else {
                res.header('Access-Control-Allow-Origin', '*')
                res.send({
                    message: `Cannot delete User with id=${id}. Maybe User was not found!`
                });
            }
        })
        .catch(err => {
            res.header('Access-Control-Allow-Origin', '*')
            res.status(500).send({
                message: "Could not delete User with id=" + id
            });
        });
};

// Delete all Users from the database.
async function deleteAll (req, res) {
    User.destroy({
        where: {},
        truncate: false
    })
        .then(nums => {
            res.header('Access-Control-Allow-Origin', '*')
            res.send({ message: `${nums} User were deleted successfully!` });
        })
        .catch(err => {
            res.header('Access-Control-Allow-Origin', '*')
            res.status(500).send({
                message:
                    err.message || "Some error occurred while removing all users."
            });
        });
};

//Login User
async function login (req, res, next) {
    User.findOne({where: { email: req.body.email }})
        .then(user => {
            if (!user) {
                res.header('Access-Control-Allow-Origin', '*')
                return res.status(401).json({ error: 'Utilisateur non trouvé !' });
            }
            bcrypt.compare(req.body.password, user.password)
            .then(valid => {
                if (!valid) {
                    res.header('Access-Control-Allow-Origin', '*')
                    return res.status(401).json({ error: 'Mot de passe incorrect !' });
                }
                res.header('Access-Control-Allow-Origin', '*')
                res.status(200).json({
                userId: user.id,
                token: jwt.sign(
                    { userId: user.id },
                    'RANDOM_TOKEN_SECRET',
                    { expiresIn: '24h' }
                )
                });
            })
            .catch(error => {
                res.header('Access-Control-Allow-Origin', '*')
                res.status(500).json({ error })
            });
        })
        .catch(error => {
            res.header('Access-Control-Allow-Origin', '*')
            res.status(500).json({ error })
        });
  };

async function oAuth2Register (_req, res, _next) {
    res.header('Access-Control-Allow-Origin', '*')
    res.json({"url": GoogleUrl})
  };

async function oAuth2Redirect (req, res, _next) {
    const code = req.query.code
    const {tokens} = await oauth2Client.getToken(code)
    oauth2Client.setCredentials(tokens);
    const axios = require('axios');
    const test = await axios.get("https://www.googleapis.com/oauth2/v1/userinfo?access_token=" + oauth2Client.credentials.access_token)
    const user = {
        email: test.data.email
    }
    User.findOne({where: {email: user.email}})
        .then(userFind => {
            if (!userFind) {
                User.create(user)
                    .then(data => {
                        res.header('Access-Control-Allow-Origin', '*')
                        res.status(201).json({
                            userId: data.dataValues.id,
                            token: jwt.sign(
                                { userId: data.dataValues.id },
                                'RANDOM_TOKEN_SECRET',
                                { expiresIn: '24h' }
                            )
                        });
                    })
                    .catch(err => {
                        res.header('Access-Control-Allow-Origin', '*')
                        res.status(500).send({
                            message:
                                err.message || "Some error occurred while creating the User."
                        });
                    });

            } else {
                res.header('Access-Control-Allow-Origin', '*')
                res.status(200).json({
                    userId: userFind.id,
                    token: jwt.sign(
                        { userId: userFind.id },
                        'RANDOM_TOKEN_SECRET',
                        { expiresIn: '24h' }
                    )
                });
            }
        })
};

exports.create = create
exports.findAll = findAll
exports.findOne = findOne
exports.update = update
exports.deleteUser = deleteUser
exports.deleteAll = deleteAll
exports.login = login
exports.createWithoutOnlyMail = createWithoutOnlyMail
exports.oAuth2Register = oAuth2Register
exports.oAuth2Redirect = oAuth2Redirect