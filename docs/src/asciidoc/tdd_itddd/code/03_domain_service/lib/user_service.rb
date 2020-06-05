# frozen_string_literal: true

# UserService
class UserService
  def exist?(user)
    db = SQLite3::Database.new('sns.db')
    sql = 'SELECT * FROM USERS WHERE name = :name'
    result = db.execute(sql, name: user.name.value)
    !result.empty?
  end
end
