# frozen_string_literal: true

require './lib/fizz_buzz.rb'

command = FizzBuzzListCommand.new(FizzBuzzType.create(FizzBuzzType::TYPE_01))
command.execute(100).each { |i| puts i.value }
