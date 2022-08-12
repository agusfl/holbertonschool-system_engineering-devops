# Create a manifest that kills a process named killmenow.
# Info exec: https://puppet.com/docs/puppet/7/types/exec.html

exec { 'killmenow': # se puede poner cualquier nombre aca
  command  => 'pkill killmenow', # Aca se le pasa el comando a ejecutar
  provider => 'shell' # Se le indica donde se va a correr
  }
