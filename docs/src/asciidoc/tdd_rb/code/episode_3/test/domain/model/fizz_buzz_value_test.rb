# frozen_string_literal: true

require './test/test_helper'
require 'minitest/autorun'
require './lib/fizz_buzz'

class FizzBuzzValueTest < Minitest::Test
  def test_同じで値である
    value1 = FizzBuzzValue.new(1, '1')
    value2 = FizzBuzzValue.new(1, '1')

    assert value1.eql?(value2)
  end

  def test_to_stringメソッド
    value = FizzBuzzValue.new(3, 'Fizz')

    assert_equal '3:Fizz', value.to_s
  end
end
