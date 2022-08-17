# Time to practice configuring your server with Puppet! Just as you did before, we’d like you to install and configure an Nginx server
# using Puppet instead of Bash.
# To save time and effort, you should also include resources in your manifest to perform a 301 redirect when querying /redirect_me.

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

# Se indica el estado en el que tiene que estar el servicio (en este caso queremos que este corriendo)
service { 'nginx':
    ensure  => running,
    require => Package['nginx'],
}
