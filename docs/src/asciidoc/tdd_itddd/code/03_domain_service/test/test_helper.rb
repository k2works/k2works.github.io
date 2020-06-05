# frozen_string_literal: true

require 'simplecov'
SimpleCov.start
require 'minitest/reporters'
Minitest::Reporters.use! [Minitest::Reporters::SpecReporter.new(color: true)]
require 'minitest/autorun'
