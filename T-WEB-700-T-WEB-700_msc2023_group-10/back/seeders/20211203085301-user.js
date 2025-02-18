'use strict';

const userJohnDoe = {
  firstname: 'John',
  lastname: "Doe",
  email: "john.doe@gmail.com",
  password: "password",
  avatar: "bull.png",
  createdAt: "2021-12-03T08:42:44.726Z",
  updatedAt: "2021-12-03T08:42:44.726Z"
}

module.exports = {
  up: async (queryInterface, Sequelize) => {
     await queryInterface.bulkInsert('Users', [
       userJohnDoe
     ], {});
  },

  down: async (queryInterface, Sequelize) => {
     await queryInterface.bulkDelete('Users', [
       userJohnDoe
     ], {});
  }
};
