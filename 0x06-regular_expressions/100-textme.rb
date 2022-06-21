#!/usr/bin/env ruby
# Your script should output: [SENDER],[RECEIVER],[FLAGS]
# The sender phone number or name (including country code if present)
# The receiver phone number or name (including country code if present)
# The flags that were used
# Lo que hay que devolver es lo que este en el 'from', en el 'to' y en el 'flags' del texto que se pase 
# separado por comas, por eso es que cambiamos el "join" para que sea por coma.
# Info: https://www.regular-expressions.info/lookaround.html - https://www.regular-expressions.info/brackets.html

puts ARGV[0].scan(/(?:from:|to:|flags:)(.+?)(?=\])/).join(",")