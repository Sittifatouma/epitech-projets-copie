'use strict';

const basicFav = {
  user: 1,
  crypto: 1,
  createdAt: "2021-12-03T08:42:44.726Z",
  updatedAt: "2021-12-03T08:42:44.726Z"
}

module.exports = {
  up: async (queryInterface, Sequelize) => {
    await queryInterface.bulkInsert('Favs', [
      basicFav
    ], {});
   
  },

  down: async (queryInterface, Sequelize) => {
    await queryInterface.bulkDelete('Favs', [
      basicFav
    ], {})
  }
};
