# frozen_string_literal: true

class FizzBuzzListCommand < FizzBuzzCommand
  def initialize(type)
    @type = type
  end

  def execute(number)
    FizzBuzzList.new((1..number).map { |i| @type.generate(i) }).value
  end
end
