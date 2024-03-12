#!/usr/bin/env ruby

# Check if the argument matches the regular expression

def match_school(argument)
  regex = /School/
  if argument =~ regex
    puts "The argument '#{argument}' matches 'School'."
  else
    puts "The argument '#{argument}' does not match 'School'."
  end
end

#main script

if ARG.length == 1
  match_school(ARG[0])
else
  puts "Usage: ruby scripts_name.rb <argument>"
end
