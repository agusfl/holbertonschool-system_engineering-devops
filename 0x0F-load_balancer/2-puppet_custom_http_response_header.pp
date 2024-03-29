# Just as in task #0, we’d like you to automate the task of creating a custom HTTP header response, but with Puppet.

# update
exec { 'update':
  command  => 'sudo apt-get -y update',
  provider => shell,
  before   => Exec['install_Nginx'],
}

# Install nginx:
exec {'install_Nginx':
  command  => 'sudo apt-get -y install nginx',
  provider => shell,
  before   => Exec['add_header'],
}

exec { 'add_header':
  provider => shell,
  command  => "sudo sed -i '/listen 80 default_server/a add_header X-Served-By ${hostname};' /etc/nginx/sites-enabled/default",
  before   => Exec['restart_nginx'],
}

# Restart Nginx para que queden los cambios
exec { 'restart_nginx': # se puede poner cualquier nombre aca
  command  => 'sudo service nginx restart', # Aca se le pasa el comando a ejecutar
  provider => 'shell' # Se le indica donde se va a correr
  }
