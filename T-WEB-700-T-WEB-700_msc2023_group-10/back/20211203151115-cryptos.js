'use strict';

const cryptoBitcoin = {
  cmid: "btc",
  full_name: "bitcoin",
  current_price: 5618960,
  opening_price: 5656824,
  highest_price: 5756530,
  lowest_price: 5617923,
  icon_url: "https://upload.wikimedia.org/wikipedia/commons/thumb/4/46/Bitcoin.svg/1200px-Bitcoin.svg.png"
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
