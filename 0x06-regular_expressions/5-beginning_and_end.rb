#!/usr/bin/env ruby
# Script that: The regular expression must be exactly matching a string that starts with 'h' ends with 'n' and can have any single character in between.
# Con el: ^ se le indica que la palabra tiene que arrancar con la letra 'h'.
# El punto indica: que puede venir un solo caracter entre la 'h' y la 'n'.
# El $ indica: que la palabra tiene que terminar con la letra 'n'.

puts ARGV[0].scan(/^h.n$/).join