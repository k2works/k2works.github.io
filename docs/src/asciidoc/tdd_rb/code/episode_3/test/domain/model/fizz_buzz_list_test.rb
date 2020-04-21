# frozen_string_literal: true

require './test/test_helper'
require 'minitest/autorun'
require './lib/fizz_buzz'

class FizzBuzzListTest < Minitest::Test
  def test_新しいインスタンスが作られる
    command = FizzBuzzListCommand.new(FizzBuzzType.create(FizzBuzzType::TYPE_01))
    array = command.execute(50)
    list1 = FizzBuzzList.new(array)
    list2 = list1.add(array)

    assert_equal 50, list1.value.count
    assert_equal 100, list2.value.count
  end
end
