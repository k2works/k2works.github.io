# frozen_string_literal: true

class FizzBuzzType
  TYPE_01 = 1
  TYPE_02 = 2
  TYPE_03 = 3

  def self.create(type)
    case type
    when FizzBuzzType::TYPE_01
      FizzBuzzType01.new
    when FizzBuzzType::TYPE_02
      FizzBuzzType02.new
    when FizzBuzzType::TYPE_03
      FizzBuzzType03.new
    else
      FizzBuzzTypeNotDefined.new
    end
  end

  def fizz?(number)
    number.modulo(3).zero?
  end

  def buzz?(number)
    number.modulo(5).zero?
  end
end
