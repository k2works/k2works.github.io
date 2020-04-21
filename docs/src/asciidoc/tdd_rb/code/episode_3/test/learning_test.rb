# frozen_string_literal: true

require './test/test_helper'
require 'minitest/autorun'
require './lib/fizz_buzz'

class LearningTest < Minitest::Test
  describe '配列や繰り返し処理を理解する' do
    def test_繰り返し処理
      $stdout = StringIO.new
      [1, 2, 3].each { |i| p i * i }
      output = $stdout.string

      assert_equal "1\n" + "4\n" + "9\n", output
    end

    def test_selectメソッドで特定の条件を満たす要素だけを配列に入れて返す
      result = [1.1, 2, 3.3, 4].select(&:integer?)
      assert_equal [2, 4], result
    end

    def test_find_allメソッドで特定の条件を満たす要素だけを配列に入れて返す
      result = [1.1, 2, 3.3, 4].find_all(&:integer?)
      assert_equal [2, 4], result
    end

    def test_特定の条件を満たさない要素だけを配列に入れて返す
      result = [1.1, 2, 3.3, 4].reject(&:integer?)
      assert_equal [1.1, 3.3], result
    end

    def test_mapメソッドで新しい要素の配列を返す
      result = %w[apple orange pineapple strawberry].map(&:size)
      assert_equal [5, 6, 9, 10], result
    end

    def test_collectメソッドで新しい要素の配列を返す
      result = %w[apple orange pineapple strawberry].collect(&:size)
      assert_equal [5, 6, 9, 10], result
    end

    def test_findメソッドで配列の中から条件に一致する要素を取得する
      result = %w[apple orange pineapple strawberry].find(&:size)
      assert_equal 'apple', result
    end

    def test_detectメソッドで配列の中から条件に一致する要素を取得する
      result = %w[apple orange pineapple strawberry].detect(&:size)
      assert_equal 'apple', result
    end

    def test_指定した評価式で並び変えた配列を返す
      result1 = %w[2 4 13 3 1 10].sort
      result2 = %w[2 4 13 3 1 10].sort { |a, b| a.to_i <=> b.to_i }
      result3 = %w[2 4 13 3 1 10].sort { |b, a| a.to_i <=> b.to_i }

      assert_equal %w[1 10 13 2 3 4], result1
      assert_equal %w[1 2 3 4 10 13], result2
      assert_equal %w[13 10 4 3 2 1], result3
    end

    def test_配列の中から条件に一致する要素を取得する
      result = %w[apple orange pineapple strawberry apricot].grep(/^a/)
      assert_equal %w[apple apricot], result
    end

    def test_ブロック内の条件式が真である間までの要素を返す
      result = [1, 2, 3, 4, 5, 6, 7, 8, 9].take_while { |item| item < 6 }
      assert_equal [1, 2, 3, 4, 5], result
    end

    def test_ブロック内の条件式が真である以降の要素を返す
      result = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10].drop_while { |item| item < 6 }
      assert_equal [6, 7, 8, 9, 10], result
    end

    def test_injectメソッドで畳み込み演算を行う
      result = [1, 2, 3, 4, 5].inject(0) { |total, n| total + n }
      assert_equal 15, result
    end

    def test_reduceメソッドで畳み込み演算を行う
      result = [1, 2, 3, 4, 5].reduce { |total, n| total + n }
      assert_equal 15, result
    end
  end
end
