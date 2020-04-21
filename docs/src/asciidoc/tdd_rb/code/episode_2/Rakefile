# frozen_string_literal: true

require 'rake/testtask'
require 'rubocop/rake_task'
RuboCop::RakeTask.new

task default: [:guard]

Rake::TestTask.new do |test|
  test.test_files = Dir['./test/fizz_buzz_test.rb']
  test.verbose = true
end

desc 'Run Format'
task :format do
  sh 'rubocop --fix-layout'
end

desc 'Run Guard'
task :guard do
  sh 'guard start'
end
