# frozen_string_literal: true

# User name value object
class UserName
  attr_reader :value

  def initialize(value)
    raise if value.nil?
    raise 'ユーザー名は3文字以上です。' if value.length < 3

    @value = value
  end
end
