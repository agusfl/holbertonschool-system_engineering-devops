# Just as in task #0, we’d like you to automate the task of creating a custom HTTP header response, but with Puppet.

# Install nginx:
package { 'nginx':
  ensure => 'installed'
}

# Add Header
file_line { 'add_path':
  ensure => present,
  path   => '/etc/nginx/sites-enabled/default',
  after  => 'listen 80 default_server;',
  line   => "add_header X-Served-By ${hostname};",
}

# Se indica el estado en el que tiene que estar el servicio (en este caso queremos que este corriendo)
service { 'nginx':
    ensure  => running,
    require => Package['nginx'],
}
