#!/usr/bin/env ruby
# Script to match "hbtn" and the t can be between 1 and 4 times.

puts ARGV[0].scan(/h+b+t+n/).join