# frozen_string_literal: true

class FizzBuzzType02 < FizzBuzzType
  def generate(number)
    FizzBuzzValue.new(number, number.to_s)
  end
end
