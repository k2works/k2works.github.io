# frozen_string_literal: true

require './test/test_helper'
require 'minitest/autorun'
require './lib/fizz_buzz'

class FizzBuzzListCommandTest < Minitest::Test
  describe '数を文字列にして返す' do
    describe 'タイプ1の場合' do
      describe '1から100までのFizzBuzzの配列を返す' do
        def setup
          fizzbuzz = FizzBuzzListCommand.new(FizzBuzzType01.new)
          @result = fizzbuzz.execute(100)
        end

        def test_配列の初めは文字列の1を返す
          assert_equal '1', @result.first.value
        end

        def test_配列の最後は文字列のBuzzを返す
          assert_equal 'Buzz', @result.last.value
        end

        def test_配列の2番目は文字列のFizzを返す
          assert_equal 'Fizz', @result[2].value
        end

        def test_配列の4番目は文字列のBuzzを返す
          assert_equal 'Buzz', @result[4].value
        end

        def test_配列の14番目は文字列のFizzBuzzを返す
          assert_equal 'FizzBuzz', @result[14].value
        end
      end
    end
  end

  describe '例外ケース' do
    def test_100より多い数を許可しない
      e = assert_raises RuntimeError do
        FizzBuzzListCommand.new(
          FizzBuzzType.create(FizzBuzzType::TYPE_01)
        ).execute(101)
      end

      assert_equal '上限は100件までです', e.message
    end
  end
end
