# Just as in task #0, we’d like you to automate the task of creating a custom HTTP header response, but with Puppet.

# update
exec { 'update':
  command  => 'sudo apt-get -y update',
  provider => shell,
  before   => Exec['install Nginx'],
}

# Install nginx:
exec {'install Nginx':
  provider => shell,
  command  => 'sudo apt-get -y install nginx',
  before   => Exec['add_header'],
}

# Add Header
file_line { 'add_header':
  ensure => present,
  path   => '/etc/nginx/sites-enabled/default',
  after  => 'listen 80 default_server;',
  line   => "add_header X-Served-By '${hostname}'';",
  before => Exec['restart_nginx'],
}

# Restart Nginx para que queden los cambios
exec { 'restart_nginx': # se puede poner cualquier nombre aca
  command  => 'sudo service nginx restart', # Aca se le pasa el comando a ejecutar
  provider => 'shell' # Se le indica donde se va a correr
  }
