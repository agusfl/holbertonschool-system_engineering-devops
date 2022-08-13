# Just as in the previous configuration file task, we’d like you to set up your client
# SSH configuration file so that you can connect to a server without typing a password using puppet.
# Usamos file_line --> https://queirozf.com/entries/using-file-line-resource-from-puppet-s-stdlib-module
# more info --> https://stackoverflow.com/questions/46468922/how-to-change-the-contents-of-a-file-by-using-puppet

file_line { 'Identity file':
  ensure => 'present',
  path   => '/etc/ssh/ssh_config',
  line   => '    IdentityFile ~/.ssh/school',
}
file_line { 'disable password':
    path => '/etc/ssh/ssh_config',
    line => '    PasswordAuthentication no',
}
