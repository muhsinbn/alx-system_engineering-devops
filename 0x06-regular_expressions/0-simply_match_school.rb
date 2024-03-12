#!/usr/bin/env ruby

# Check if the argument matches the regular expression
def match_school(argument)
  if argument.match?(/School/)
    puts "The argument '#{argument}' matches 'School'."
  else
    puts "The argument '#{argument}' does not match 'School'."
  end
end

# Main script
if ARG.length == 1
  match_school(ARG[0])
else
  puts "Usage: ruby script_name.rb <argument>"
end
