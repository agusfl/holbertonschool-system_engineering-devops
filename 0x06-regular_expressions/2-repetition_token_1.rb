#!/usr/bin/env ruby
# Script to match "htn" or "hbtn"
# Ademas de esta pagina: https://rubular.com/, use esta otra: https://regexone.com/lesson/repeating_characters?
# Con el signo de pregunta se dice que contenga si es una u otra opcion, en este caso si tiene la letra 'b' o 't'.

puts ARGV[0].scan(/(hb?tn)/).join
