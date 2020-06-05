# frozen_string_literal: true

require './test/test_helper'
require './lib/sns.rb'

class UserServiceTest < Minitest::Test
  describe 'ユーザーの重複を判定する' do
    def setup
      @db = SQLite3::Database.new('sns.db')
      sql = 'CREATE TABLE USERS(id string, name string)'
      @db.execute(sql)

      @service = UserService.new
    end

    def test_登録するユーザーがすでに存在している
      name = UserName.new('Bob')
      user = User.new(user_name: name)

      sql = 'INSERT INTO USERS(id, name) VALUES(:id, :name)'
      @db.execute(sql, id: user.id.value, name: user.name.value)

      assert @service.exist?(user)
    end

    def test_登録するユーザーが存在していない
      name = UserName.new('Alice')
      user = User.new(user_name: name)

      refute @service.exist?(user)
    end

    def teardown
      sql = 'DROP TABLE USERS'
      @db.execute(sql)
      @db.close
    end
  end
end
