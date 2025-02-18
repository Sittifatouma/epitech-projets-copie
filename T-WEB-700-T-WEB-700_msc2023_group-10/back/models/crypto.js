'use strict';
const {
  Model
} = require('sequelize');
module.exports = (sequelize, DataTypes) => {
  class Crypto extends Model {
    /**
     * Helper method for defining associations.
     * This method is not a part of Sequelize lifecycle.
     * The `models/index` file will call this method automatically.
     */
    static associate(models) {
      // define association here
    }
  };
  Crypto.init({
    cmid: DataTypes.STRING,
    full_name: DataTypes.STRING,
    current_price: DataTypes.FLOAT,
    opening_price: DataTypes.FLOAT,
    highest_price: DataTypes.FLOAT,
    lowest_price: DataTypes.FLOAT,
    icon_url: DataTypes.STRING
  }, {
    sequelize,
    modelName: 'Crypto',
  });
  return Crypto;
};
