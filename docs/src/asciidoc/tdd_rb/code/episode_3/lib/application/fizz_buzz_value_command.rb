# frozen_string_literal: true

class FizzBuzzValueCommand < FizzBuzzCommand
  def initialize(type)
    @type = type
  end

  def execute(number)
    @type.generate(number).value
  end
end
