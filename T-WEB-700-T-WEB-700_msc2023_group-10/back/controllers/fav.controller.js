const db = require("../models");
const Fav = db.favs;
const Op = db.Sequelize.Op;


// Create and Save a new fav
async function create(req, res) {
    // Validate request
    if (!req.body.user) {
        res.header('Access-Control-Allow-Origin', '*')
        res.status(400).send({
            message: "Content can not be empty!"
        });
        return;
    }
    // Create a fav
    const fav = {
        user: req.body.user,
        crypto: req.body.crypto
    };

    // Save fav in the database
    Fav.create(fav)
        .then(data => {
            res.header('Access-Control-Allow-Origin', '*')
            res.send(data);
        })
        .catch(err => {
            res.header('Access-Control-Allow-Origin', '*')
            res.status(500).send({
                message:
                    err.message || "Some error occurred while creating the fav."
            });
        });
};

// Retrieve all fav from the database.
async function findAll(req, res) {
    const user = parseInt(req.query.user);
    var condition = user ? {user: {[Op.eq]: `${user}`}} : null;
    Fav.findAll({where: condition})
        .then(data => {
            res.header('Access-Control-Allow-Origin', '*')
            res.send(data);
        })
        .catch(err => {
            res.header('Access-Control-Allow-Origin', '*')
            res.status(500).send({
                message:
                    err.message || "Some error occurred while retrieving fav."
            });
        });
};

// Find a single fav with an id
async function findOne(req, res) {
    const id = req.params.id;

    Fav.findByPk(id)
        .then(data => {
            res.header('Access-Control-Allow-Origin', '*')
            res.send(data);
        })
        .catch(err => {
            res.header('Access-Control-Allow-Origin', '*')
            res.status(500).send({
                message: "Error retrieving fav with id=" + id
            });
        });
};

// Update a fav by the id in the request
async function update(req, res) {
    const id = req.params.id;

    Fav.update(req.body, {
        where: {id: id}
    })
        .then(num => {
            if (num == 1) {
                res.header('Access-Control-Allow-Origin', '*')
                res.send({
                    message: "fav was updated successfully."
                });
            } else {
                res.header('Access-Control-Allow-Origin', '*')
                res.send({
                    message: `Cannot update fav with id=${id}. Maybe fav was not found or req.body is empty!`
                });
            }
        })
        .catch(err => {
            res.header('Access-Control-Allow-Origin', '*')
            res.status(500).send({
                message: "Error updating fav with id=" + id
            });
        });
};

// Delete a fav with the specified id in the request
async function deleteFav(req, res) {
    const id = req.params.id;

    Fav.destroy({
        where: {id: id}
    })
        .then(num => {
            if (num == 1) {
                res.header('Access-Control-Allow-Origin', '*')
                res.send({
                    message: "fav was deleted successfully!"
                });
            } else {
                res.header('Access-Control-Allow-Origin', '*')
                res.send({
                    message: `Cannot delete fav with id=${id}. Maybe fav was not found!`
                });
            }
        })
        .catch(err => {
            res.header('Access-Control-Allow-Origin', '*')
            res.status(500).send({
                message: "Could not delete fav with id=" + id
            });
        });
};

// Delete all Fav from the database.
async function deleteAll(req, res) {
    Fav.destroy({
        where: {},
        truncate: false
    })
        .then(nums => {
            res.header('Access-Control-Allow-Origin', '*')
            res.send({message: `${nums} Fav were deleted successfully!`});
        })
        .catch(err => {
            res.header('Access-Control-Allow-Origin', '*')
            res.status(500).send({
                message:
                    err.message || "Some error occurred while removing all Fav."
            });
        });
};


exports.create = create
exports.findAll = findAll
exports.findOne = findOne
exports.update = update
exports.deleteAll = deleteAll
exports.deleteFav = deleteFav
