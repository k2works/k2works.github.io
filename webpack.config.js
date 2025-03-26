const path = require("path");
const HtmlWebpackPlugin = require("html-webpack-plugin");
const webpack = require("webpack");

const env = process.env.NODE_ENV || "development";
const isDevelopment = env === "development";

module.exports = {
    mode: env,
    devtool: isDevelopment ? "source-map" : false,
    entry: './index.js',
    output: {
        path: __dirname + '/public',
        filename: 'bundle.js',
    },
    devServer: {
        static: {
            directory: path.join(__dirname, 'public'),
        },
        compress: true,
        port: 9000,
    },
    externals: {
        jquery: '$',
        lodash: "_",
        moment: "moment",
    },
    module: {
        rules: [
            {
                test: /\.js$/,
                use: [
                    {
                        loader: 'babel-loader',
                        options: {
                            presets: ['@babel/preset-env'],
                        },
                    },
                ],
            },
            {
                test: /\.css/,
                use: [
                    "style-loader",
                    {
                        loader: "css-loader",
                        options: {
                            url: false,
                            sourceMap: true,
                        }
                    }
                ]
            },
        ],
    },
    target: ['web', 'es5'],
    plugins: [
        new HtmlWebpackPlugin({
            template: 'index.html',
        }),
        new webpack.ProvidePlugin({
            $: 'jquery',
            jQuery: 'jquery',
            _: "lodash",
            "window._": "lodash",
            moment: "moment",
            "window.moment": "moment",
        }),
    ],
}
