# frozen_string_literal: true

class FizzBuzz
  MAX_NUMBER = 100

  def self.generate(number)
    is_fizz = number.modulo(3).zero?
    is_buzz = number.modulo(5).zero?

    return 'FizzBuzz' if is_fizz && is_buzz
    return 'Fizz' if is_fizz
    return 'Buzz' if is_buzz

    number.to_s
  end

  def self.generate_list
    # 1から最大値までのFizzBuzz配列を1発で作る
    (1..MAX_NUMBER).map { |n| generate(n) }
  end
end
