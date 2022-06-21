#!/usr/bin/env ruby
# Script that: The regular expression must be exactly matching a string that starts with 'h' ends with 'n' and can have any single character in between.
# Con la /d indicamos que sean solo digitos y con {10} se indica que sean 10 digitos, ^ y $ es para indicar que arranca y termina con 10 digitos.

puts ARGV[0].scan(/^\d{10}$/).join