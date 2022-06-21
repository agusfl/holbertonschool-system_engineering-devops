#!/usr/bin/env ruby
# Script to match "hbtn" or hb

puts ARGV[0].scan(/(hbt{1,4}n)/).join