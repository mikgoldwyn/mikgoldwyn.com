module.exports = {
  publicPath: "/dist/",

  // cache busting
  chainWebpack: config => {
    config.plugin('html').tap(args => {
      args[0].hash = true
      return args
    })
  }
};
