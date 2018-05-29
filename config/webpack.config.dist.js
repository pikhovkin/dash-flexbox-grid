const config = require('./webpack.config.dev');

const webpack = require('webpack');

module.exports = {
  ...config,
  plugins: [
    new webpack.DefinePlugin({
      'process.env': {
        NODE_ENV: JSON.stringify('production')
      }
    }),
    new webpack.optimize.UglifyJsPlugin({
      include: /\.js/i,
      mangle: false,
      comments: false, // remove comments
      compress: {
        unused: true,
        dead_code: true, // big one--strip code that will never execute
        warnings: false,
        drop_console: false // strips console statements
      }
    })
  ]
};