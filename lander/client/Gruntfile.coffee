module.exports = (grunt) ->
    # Load all our tasks based on the 'grunt-*' pattern in package.json.
    require('load-grunt-tasks')(grunt)

    grunt.initConfig
        pkg: grunt.file.readJSON('package.json')

        # Compiled LESS to CSS, copy to static.
        less:
            production:
                options:
                    compress: true
                files:
                    '../static/css/base.min.css': 'less/styles.less'

        # On file changes, rebuild relevant deps.
        watch:
            options:
                livereload: true
            less:
                files: 'less/**/*.less'
                tasks: ['less']
                options:
                    livereload: true

    grunt.registerTask('default', ['less'])
