#!/usr/bin/env ruby
# Script to match "hbttn" that can have a 't' between 2 and 5 times.

puts ARGV[0].scan(/(hbt{2,5}n)/).join
