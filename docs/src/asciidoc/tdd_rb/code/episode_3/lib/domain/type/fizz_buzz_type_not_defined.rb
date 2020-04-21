# frozen_string_literal: true

class FizzBuzzTypeNotDefined < FizzBuzzType
  def generate(number)
    FizzBuzzValue.new(number, '')
  end

  def to_s
    '未定義'
  end
end
