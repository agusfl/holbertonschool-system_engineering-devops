# Fix 500 (internal error) when a GET HTTP method is requested to Apache2 web server
# Con el comando sed y las flags "-i" "s | g" le indicamos que se cambie todos los phpp por
# php en el archivo que esta en la ruta: /var/www/html/wp-settings.php

exec {'fix_500_error':
  provider => shell,
  command  => 'sed -i "s/phpp/php/g" /var/www/html/wp-settings.php'
}
