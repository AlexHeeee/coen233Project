
const path = require('path')
function resolve(dir) {
    return path.join(__dirname, dir)
}
function publicPath(){
    if (process.env.NODE_ENV == 'production') {
        return "././";
    } else {
        return "/";
    }
}

module.exports = {

    publicPath: publicPath(),

    configureWebpack: {
        resolve: {
            alias: {
                '@': resolve('src')
            }
        }
    },
lintOnSave: false,
    devServer: {
        host: "0.0.0.0",
        port: 8080,
        hot: true,
        https: false,
        proxy: {
            '/djangoz3gw0': {
                target: 'http://localhost:8080/djangoz3gw0/',
                changeOrigin: true,
                secure: false,
                pathRewrite: {
                    '^/djangoz3gw0': ''
                }
            }
        }
    },
}
