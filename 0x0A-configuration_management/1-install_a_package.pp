# Install flask version 2.1.0
# Info sobre package: https://puppet.com/docs/puppet/5.5/types/package.html#package-attribute-ensure
package { 'flask':
  ensure   => '2.1.0', # se indica la version a instalar de flask
  provider => 'pip3' # se le indica el package manager que se va a usar.
}
