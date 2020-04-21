# frozen_string_literal: true

module Fibonacci
  # Fibonacci Loop algorithm
  class Loop
    def exec(number)
      a = 0
      b = 1
      c = 0
      (0...number).each do |_i|
        a = b
        b = c
        c = a + b
      end
      c
    end
  end
end