# frozen_string_literal: true

require './test/test_helper'
require 'minitest/autorun'
require './lib/fizz_buzz'

class FizzBuzzValueCommandTest < Minitest::Test
  describe '数を文字列にして返す' do
    describe 'タイプ1の場合' do
      def setup
        @fizzbuzz = FizzBuzzValueCommand.new(FizzBuzzType01.new)
      end

      describe '三の倍数の場合' do
        def test_3を渡したら文字列Fizzを返す
          assert_equal 'Fizz', @fizzbuzz.execute(3)
        end
      end

      describe '五の倍数の場合' do
        def test_5を渡したら文字列Buzzを返す
          assert_equal 'Buzz', @fizzbuzz.execute(5)
        end
      end

      describe '三と五の倍数の場合' do
        def test_15を渡したら文字列FizzBuzzを返す
          assert_equal 'FizzBuzz', @fizzbuzz.execute(15)
        end
      end

      describe 'その他の場合' do
        def test_1を渡したら文字列1を返す
          assert_equal '1', @fizzbuzz.execute(1)
        end
      end
    end

    describe 'タイプ2の場合' do
      def setup
        @fizzbuzz = FizzBuzzValueCommand.new(FizzBuzzType02.new)
      end

      describe '三の倍数の場合' do
        def test_3を渡したら文字列3を返す
          assert_equal '3', @fizzbuzz.execute(3)
        end
      end

      describe '五の倍数の場合' do
        def test_5を渡したら文字列5を返す
          assert_equal '5', @fizzbuzz.execute(5)
        end
      end

      describe '三と五の倍数の場合' do
        def test_15を渡したら文字列15を返す
          assert_equal '15', @fizzbuzz.execute(15)
        end
      end

      describe 'その他の場合' do
        def test_1を渡したら文字列1を返す
          assert_equal '1', @fizzbuzz.execute(1)
        end
      end
    end

    describe 'タイプ3の場合' do
      def setup
        @fizzbuzz = FizzBuzzValueCommand.new(FizzBuzzType03.new)
      end

      describe '三の倍数の場合' do
        def test_3を渡したら文字列3を返す
          assert_equal '3', @fizzbuzz.execute(3)
        end
      end

      describe '五の倍数の場合' do
        def test_5を渡したら文字列5を返す
          assert_equal '5', @fizzbuzz.execute(5)
        end
      end

      describe '三と五の倍数の場合' do
        def test_15を渡したら文字列FizzBuzzを返す
          assert_equal 'FizzBuzz', @fizzbuzz.execute(15)
        end
      end

      describe 'その他の場合' do
        def test_1を渡したら文字列1を返す
          assert_equal '1', @fizzbuzz.execute(1)
        end
      end
    end

    describe 'それ以外のタイプの場合' do
      def test_未定義のタイプを返す
        fizzbuzz = FizzBuzzType.create(4)

        assert_equal '未定義', fizzbuzz.to_s
      end

      def test_空の文字列を返す
        type = FizzBuzzType.create(4)
        command = FizzBuzzValueCommand.new(type)

        assert_equal '', command.execute(3)
      end
    end
  end

  describe '例外ケース' do
    def test_値は正の値のみ許可する
      e = assert_raises RuntimeError do
        FizzBuzzValueCommand.new(
          FizzBuzzType.create(FizzBuzzType::TYPE_01)
        ).execute(-1)
      end

      assert_equal '正の値のみ有効です', e.message
    end
  end
end
