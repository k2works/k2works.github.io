require './lib/fibonacci'

number = ARGV[0].to_i
command = Fibonacci::Command.new(Fibonacci::GeneralTerm.new)
puts command.exec(number)