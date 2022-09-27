# Change limit of requests for nginx

# Se cambia el limite de requests para nginx
exec {'replace':
  provider => shell,
  command  => 'sudo sed -i "s/ULIMIT=\"-n 15\"/ULIMIT=\"-n 2000\"/" /etc/default/nginx',
}

# Restart Nginx para que queden los cambios
exec { 'restart_nginx': # se puede poner cualquier nombre aca
  command  => 'sudo service nginx restart', # Aca se le pasa el comando a ejecutar
  provider => 'shell' # Se le indica donde se va a correr
}
