# Puppet - Configuration management:

**Resources:**

* [Intro to Configuration Management](https://www.digitalocean.com/community/tutorials/an-introduction-to-configuration-management)
* [Puppet resource type: file (check “Resource types” for all manifest types in the left menu)](https://puppet.com/docs/puppet/5.5/types/file.html)
* [Puppet’s Declarative Language: Modeling Instead of Scripting](https://puppet.com/blog/puppets-declarative-language-modeling-instead-of-scripting/)
* [Puppet lint](http://puppet-lint.com/)

**How to install Puppet and puppet-lint for Linux:**
Install Puppet:

```
apt-get install -y ruby=1:2.7+1 --allow-downgrades
apt-get install -y ruby-augeas
apt-get install -y ruby-shadow
apt-get install -y puppet
```
Instal puppet-lint (syntaxis):

```
gem install puppet-lint
```

## Environment
 
* Language: Puppet
* Operating System: Ubuntu 20.04 LTS
* Style guidelines: [puppet-lint](http://puppet-lint.com/)
 > **Note:** The file shoul have executable permissions: ``chmod u+x [filename]`` --> run with ``./filename``

## Description of each file:

| Files          |Desription
|:----------------|:-------------------------------:|
|0-create_a_file.pp |Using ``Puppet``, **create a file** in /tmp.
|1-install_a_package.pp |Using ``Puppet``, install ``flask`` from pip3.
|2-execute_a_command.pp |Using ``Puppet``, create a manifest that **kills a process** named **killmenow**.

## Authors :pen:

* [Agustin Flom](https://www.linkedin.com/in/agustin-f/)
