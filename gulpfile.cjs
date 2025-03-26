const { series, parallel } = require('gulp');
const core = require('./ops/gulp/tasks/core');

const build = series(
    core.webpackBuildTasks(),
    core.asciidoctorBuildTasks(),
    core.marpBuildTasks(),
    core.adrBuildTasks(),
);
exports.build = build;

const start = series(
    series(
        parallel(core.webpack.server, core.asciidoctor.server),
        parallel(core.webpack.watch, core.asciidoctor.watch, core.marp.watch),
    ),
    parallel(core.wiki.openWiki, core.wiki.startWiki),
);

exports.default = start;

exports.dev = series(
    build,
    core.wiki.buildWiki,
    start,
);

exports.docs = series(
    parallel(core.asciidoctorBuildTasks(), core.marpBuildTasks()),
    core.adrBuildTasks(),
    parallel(core.asciidoctor.server, core.asciidoctor.watch, core.marp.watch),
);
exports.slides = series(core.marp.build);
