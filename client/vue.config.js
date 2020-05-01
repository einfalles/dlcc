const path = require('path');
module.exports = { runtimeCompiler: true }
module.exports = {
    outputDir: path.resolve(__dirname, '../docs'),
    publicPath: process.env.NODE_ENV === 'production'
      ? '/dlcc/'
      : '/'
  }