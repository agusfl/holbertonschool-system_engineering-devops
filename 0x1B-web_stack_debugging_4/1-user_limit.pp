# Fix problem for conecting to user "holberton" with too many files open

exec {'replace_1':
  command  => 'sudo sed -i "s/nofile 5/nofile 50000/" /etc/security/limits.conf',
  provider => shell
}

exec {'replace_2':
  command  => 'sudo sed -i "s/nofile 4/nofile 40000/" /etc/security/limits.conf',
  provider => shell
}
