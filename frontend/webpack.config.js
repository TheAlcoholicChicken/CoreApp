const webpack = require('webpack');
const path = require('path');
const HtmlWebpackPlugin = require('html-webpack-plugin');
const CopyWebpackPlugin = require('copy-webpack-plugin');
const DIST_DIR = path.resolve(__dirname, "public");
const SRC_DIR = path.resolve(__dirname, "src");

const config = {
  entry: {
      index : SRC_DIR + "/index.js",
      login   : SRC_DIR + "/login.js"
  }, // configure which file to start
  output: {
    path: DIST_DIR,
    filename: '[name].js',
  },
  module:{
    rules: [
      {
        test: /\.js$/,  // what files to look for
        exclude: /node_modules/,
        use:{
          loader: 'babel-loader'
        }
      },
      {
        test: /\.css$/,
        use: ['style-loader', 'css-loader'],
      },
      {
        test: /\.(jpg|png|ico)$/,
        use: ['file-loader']
      },
    ],
  },
  plugins: [
    new HtmlWebpackPlugin({
      filename: 'index.html',
      template: SRC_DIR + '/index.html',
      inject:false
    }),
    new HtmlWebpackPlugin({
      filename: 'login.html',
      template: SRC_DIR + '/login.html',
      inject:false
    }),
    new CopyWebpackPlugin([
    // relative path is from src
    { from: SRC_DIR + '/favicon.ico' }, // <- your path to favicon
  ])
  ]
};

module.exports = config;
