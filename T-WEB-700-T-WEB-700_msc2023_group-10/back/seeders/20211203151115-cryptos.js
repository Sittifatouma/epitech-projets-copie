'use strict';

const cryptoBitcoin = {
  cmid: "btc",
  full_name: "bitcoin2",
  current_price: 55555,
  opening_price: 55555,
  highest_price: 55555,
  lowest_price: 55555,
  icon_url: "https://upload.wikimedia.org/wikipedia/commons/thumb/4/46/Bitcoin.svg/1200px-Bitcoin.svg.png",
  createdAt: "2021-12-03T08:42:44.726Z",
  updatedAt: "2021-12-03T08:42:44.726Z"
}

module.exports = {
  up: async (queryInterface, Sequelize) => {
    await queryInterface.bulkInsert('Cryptos', [
      cryptoBitcoin
    ], {});
  },

  down: async (queryInterface, Sequelize) => {
    await queryInterface.bulkDelete('Cryptos', [
      cryptoBitcoin
    ], {});
  }
};
