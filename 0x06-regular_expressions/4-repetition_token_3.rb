#!/usr/bin/env ruby
# Script to match "hbtn" and the t can be between 1 and 4 times without using square brackets
# Con el signo de ? chequeamos que sea 'b' o 't' y usamos el ++ para decirle que matchee todas las letras que vengan despues hasta la 'n'

puts ARGV[0].scan(/(hbt?++n)/).join