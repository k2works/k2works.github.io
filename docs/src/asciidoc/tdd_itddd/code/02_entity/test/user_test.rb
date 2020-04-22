# frozen_string_literal: true

require './test/test_helper'
require './lib/sns.rb'

class UserTest < Minitest::Test
  describe 'ユーザーを登録する' do
    def setup
      id = UserId.new('1')
      name = UserName.new('Bob')
      @user = User.new(user_id: id, user_name: name)
    end

    def test_IDと名前を持ったユーザーを作成する
      assert_equal '1', @user.id.value
      assert_equal 'Bob', @user.name.value
    end

    def test_ユーザー名が３文字未満の場合はエラー
      e = assert_raises RuntimeError do
        UserName.new('a')
      end

      assert_equal 'ユーザー名は3文字以上です。', e.message
    end

    def test_ユーザー名が４文字の場合は登録される
      user = User.new(user_id: UserId.new('1'),
                      user_name: UserName.new('abcd'))
      assert_equal 'abcd', user.name.value
    end

    def test_ユーザー名を指定しない場合はエラー
      assert_raises RuntimeError do
        UserName.new(nil)
      end
    end

    def test_IDを指定しない場合はエラー
      assert_raises RuntimeError do
        UserId.new(nil)
      end
    end
  end

  describe 'ユーザーを更新する' do
    def setup
      id = UserId.new('1')
      name = UserName.new('Bob')
      @user = User.new(user_id: id, user_name: name)
    end

    def test_ユーザー名を更新する
      @user.change_name('Alice')
      assert_equal 'Alice', @user.name
    end
  end

  describe 'ユーザーの同一性を判断する' do
    def setup
      id = UserId.new('1')
      name = UserName.new('Bob')
      @user = User.new(user_id: id, user_name: name)
    end

    def test_同じ名前の異なるユーザー
      id = UserId.new('2')
      name = UserName.new('Bob')
      @user2 = User.new(user_id: id, user_name: name)

      refute @user.eql?(@user2)
    end

    def test_同じ名前の同じユーザー
      assert @user.eql?(@user)
    end

    def test_名前を変更した同じユーザー
      @user.change_name('Alice')

      assert @user.eql?(@user)
    end
  end
end
