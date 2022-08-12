# Create a file in /tmp
file { '/tmp/school':
  ensure  => file,  # se asegura que el archivo exista y sino lo crea
  path    => '/tmp/school',
  mode    => '0744',
  owner   => 'www-data',
  group   => 'www-data',
  content => 'I love Puppet'
}
