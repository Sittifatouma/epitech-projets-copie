'use strict';
module.exports = {
  up: async (queryInterface, Sequelize) => {
    await queryInterface.createTable('Cryptos', {
      id: {
        allowNull: false,
        autoIncrement: true,
        primaryKey: true,
        type: Sequelize.INTEGER
      },
      cmid: {
        type: Sequelize.STRING
      },
      full_name: {
        type: Sequelize.STRING
      },
      current_price: {
        type: Sequelize.FLOAT
      },
      opening_price: {
        type: Sequelize.FLOAT
      },
      highest_price: {
        type: Sequelize.FLOAT
      },
      lowest_price: {
        type: Sequelize.FLOAT
      },
      icon_url: {
        type: Sequelize.STRING
      },
      createdAt: {
        allowNull: false,
        type: Sequelize.DATE
      },
      updatedAt: {
        allowNull: false,
        type: Sequelize.DATE
      }
    });
  },
  down: async (queryInterface, Sequelize) => {
    await queryInterface.dropTable('Cryptos');
  }
};
