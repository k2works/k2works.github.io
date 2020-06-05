# frozen_string_literal: true

# User
class User
  attr_reader :id, :name

  def initialize(user_name:)
    @id = UserId.new(SecureRandom.uuid.to_str)
    @name = user_name
  end

  def change_name(name)
    raise if name.nil?

    @name = name
  end

  def eql?(other)
    @id == other.id
  end

  def ==(other)
    other.equal?(self) || other.instance_of?(self.class) && other.id == id
  end

  def hash
    id.hash
  end
end
