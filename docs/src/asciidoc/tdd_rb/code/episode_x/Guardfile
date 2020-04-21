# frozen_string_literal: true

# Add files and commands to this file, like the example:
#   watch(%r{file/path}) { `command(s)` }
#
guard :shell do
  watch(%r{lib/(.*).rb}) { |_m| `rake test` }
end

guard :minitest do
  # with Minitest::Unit
  watch(%r{test\/*.rb})
end

guard :rubocop, cli: %w[--auto-correct --format fuubar --format html -o ./tmp/rubocop_results.html] do
  watch(/(.*).rb/)
end