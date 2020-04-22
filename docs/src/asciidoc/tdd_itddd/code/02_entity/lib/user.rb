# frozen_string_literal: true

# User
class User
  attr_reader :id, :name

  def initialize(user_id:, user_name:)
    @id = user_id
    @name = user_name
  end

  def change_name(name)
    raise if name.nil?

    @name = name
  end

  def eql?(other)
    self == other
  end

  def ==(other)
    other.equal?(self) ||
      (other.instance_of?(self.class) && other.id == id && other.name == name)
  end

  def hash
    id.hash
  end
end
