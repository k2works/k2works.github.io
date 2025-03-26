const tasks =  {
    task1: (cb) => {
        // place code for your default task here
        cb();
    }
}

exports.tasks = tasks;

const { series, watch, src, dest } = require('gulp');
const fs = require('fs-extra');
const kroki = require('asciidoctor-kroki');
const browserSync = require('browser-sync').create();
const exec = require('gulp-exec');
const gulpRename = require('gulp-rename');

// Windows環境かどうかをチェック
const isWindows = process.platform === 'win32';
// プロジェクトのルートディレクトリを取得
const projectRoot = process.cwd();

const asciidoctor = {
    clean: async (cb) => {
        await fs.remove("./public/docs"); // fs-extraでディレクトリを非同期で削除
        cb(); // コールバック関数を呼び出す
    },
    build: (cb) => {
        const asciidoctor = require("@asciidoctor/core")();
        const krokiRegister = () => {
            const registry = asciidoctor.Extensions.create();
            kroki.register(registry);
            return registry;
        };

        const inputRootDir = "./docs";
        const outputRootDir = "./public/docs";
        const fileNameList = fs.readdirSync(inputRootDir);
        const docs = fileNameList.filter(RegExp.prototype.test, /.*\.adoc$/);

        docs.map((input) => {
            const file = `${inputRootDir}/${input}`;
            asciidoctor.convertFile(file, {
                safe: "safe",
                extension_registry: krokiRegister(),
                to_dir: outputRootDir,
                mkdirs: true,
            });
        });
        src(`${inputRootDir}/images/*.*`, {encoding: false}).pipe(dest(`${outputRootDir}/images`))
            .on('end', cb); // src.pipeの完了後にcb()を実行
    },
    watch: (cb) => {
        watch("./docs/**/*.adoc", asciidoctor.build);
        cb();
    },
    server: (cb) => {
        browserSync.init({
            server: {
                baseDir: "./public",
            },
        });
        watch("./public/**/*.html").on("change", browserSync.reload);
        cb();
    },
}

exports.asciidoctor = asciidoctor;
exports.asciidoctorBuildTasks = () => {
    return series(asciidoctor.clean, asciidoctor.build);
}

const marp = {
    build: (cb) => {
        const { marpCli } = require('@marp-team/marp-cli')
        const inputRootDir = "./docs/slides";
        const outputRootDir = "./public/docs/slides";

        marpCli([
            `${inputRootDir}/PITCHME.md`,
            "--html",
            "--output",
            `${outputRootDir}/index.html`,
        ])
            .then((exitStatus) => {
                if (exitStatus > 0) {
                    console.error(`Failure (Exit status: ${exitStatus})`);
                } else {
                    console.log("Success");
                }
            })
            .catch(console.error);

        src(`${inputRootDir}/images/*.*` , {encoding: false}).pipe(dest(`${outputRootDir}/images`));

        cb();
    },
    clean: async (cb) => {
        await fs.remove("./public/docs/slides");
        cb();
    },
    watch: (cb) => {
        watch("./docs/slides/**/*.md", marp.build);
        cb();
    }
}

exports.marp = marp;
exports.marpBuildTasks = () => {
    return series(marp.clean, marp.build);
}

const webpackConfig = require("../../../webpack.config");
const path = require("path");
const webpack = {
    clean: async (cb) => {
        await fs.remove("./public");
        cb();
    },
    build: (cb) => {
        const webpack = require("webpack");
        webpack(webpackConfig, (err, stats) => {
            if (err || stats.hasErrors()) {
                console.error(err);
            }
            cb();
        });
    },
    watch: (cb) => {
        const webpack = require("webpack");
        const compiler = webpack(webpackConfig);
        compiler.watch({}, (err, stats) => {
            if (err || stats.hasErrors()) {
                console.error(err);
            }
        });
        cb();
    },
    server: (cb) => {
        const webpack = require("webpack");
        const compiler = webpack(webpackConfig);
        const WebpackDevServer = require("webpack-dev-server");

        // デフォルトのdevServer設定をクリーンアップする
        const { _assetEmittingPreviousFiles, ...validDevServerOptions } = webpackConfig.devServer;

        const devServerOptions = Object.assign({}, validDevServerOptions, {
            open: false,
        });

        const server = new WebpackDevServer(devServerOptions, compiler);
        server.start(devServerOptions.port, devServerOptions.host, () => {
            console.log("Starting server on http://localhost:8080");
        });
        cb();

        // 古いバージョン用のオプションがある場合
        // server.listen(devServerOptions.port, devServerOptions.host, () => {
        //     console.log("Starting server on http://localhost:8080");
        // });
    },
}
exports.webpackBuildTasks = () => {
    return series(webpack.clean, webpack.build);
}

exports.webpack = webpack;

const adr = {
    build: (cb) => {
        const adr = require("@k2works/adr");
        fs.ensureDir("./public/docs/adr").then(() => {
            src("./docs/adr/images/**").pipe(dest("./public/docs/adr/images"));
            const builder = new adr.default.HtmlBuilder("./docs/adr/", "./public/docs/adr/");
            let output = builder.buildContent();
            builder.output();
            return output
        });
        cb();
    },
    clean: async (cb) => {
        await fs.remove("./public/docs/adr");
        cb();
    },
}

exports.adrBuildTasks = () => {
    return series(adr.clean, adr.build);
}

const wikijs = {
    buildWiki: () => {
        const command = 'docker compose build wiki';
        return src('./', { read: false })
            .pipe(exec(command));
    },
    startWiki: () => {
        const command = 'docker compose up -d wiki';
        return src('./', { read: false })
            .pipe(exec(command));
    },
    stopWiki: () => {
        const command = 'docker compose down wiki';
        return src('./', { read: false })
            .pipe(exec(command));
    },
    openWiki: () => {
        const command = isWindows ? 'start' : 'open';
        return src('./', {read: false})
            .pipe(exec(`${command} http://localhost`));
    }
}
exports.wiki = wikijs;