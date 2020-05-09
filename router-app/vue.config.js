const path = require('path');
// module.exports = { runtimeCompiler: true }
module.exports = {
    publicPath: process.env.NODE_ENV === 'production'
    ? '/dlcc/'
    : './'
  }
    // configureWebpack: config => {
    //     if (process.env.NODE_ENV === 'production') {
    //         'output': {
    //             'path': path.resolve(__dirname, '../docs')
    //           }
    //     } else {
    //         console.log("FUCK");
    //     }
    // },
    // outputDir: path.resolve(__dirname, '../docs')
    // configureWebpack: {
    //     output: {
    //       path: path.resolve(__dirname, '../docs'),
    //     //   filename: '[name].js',
    //       publicPath: '../assets/static/',
        //   publicPath: process.env.NODE_ENV === 'production'
        //   ? '/dlcc/'
        //   : '/'
        // }
    // }
}
