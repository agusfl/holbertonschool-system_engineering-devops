# Just as in task #0, we’d like you to automate the task of creating a custom HTTP header response, but with Puppet.

# update
exec { 'update':
  command  => 'sudo apt-get update',
  provider => shell,
}

# Install nginx:
package { 'nginx':
  ensure => 'installed'
}

# Se agrega Hello World en el archivo --> index.nginx-debian.html para mostrarlo en la pagina web
file { '/var/www/html/index.nginx-debian.html':
  content => 'Hello World!',
}

# Redirection 301 permanently
file_line { 'redirect_301_status':
  ensure => present,
  path   => '/etc/nginx/sites-available/default',
  after  => 'server_name _;',
  line   => 'rewrite ^/redirect_me https://www.youtube.com/watch?v=QH2-TGUlwu4 permanent;',
}

# Add Header
file_line { 'add_path':
  ensure => present,
  path   => '/etc/nginx/sites-enabled/default',
  after  => 'listen 80 default_server;',
  line   => "add_header X-Served-By '${hostname}'';",
}

# Restart Nginx para que queden los cambios
exec { 'restart_nginx': # se puede poner cualquier nombre aca
  command  => 'sudo service nginx restart', # Aca se le pasa el comando a ejecutar
  provider => 'shell' # Se le indica donde se va a correr
  }
