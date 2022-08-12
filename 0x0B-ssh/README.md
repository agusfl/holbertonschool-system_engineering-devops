# Bash - SSH | Servers:

**Resources:**

* [What is a (physical) server - text](https://en.wikipedia.org/wiki/Server_%28computing%29#Hardware_requirement)
* [What is a (physical) server - video](https://www.youtube.com/watch?v=B1ANfsDyjeA&ab_channel=TechnologyProfession)
* [SSH essentials](https://www.digitalocean.com/community/tutorials/ssh-essentials-working-with-ssh-servers-clients-and-keys)
* [SSH Config File](https://www.ssh.com/academy/ssh/config)
* [Public Key Authentication for SSH](https://www.ssh.com/academy/ssh/public-key-authentication)
* [How Secure Shell Works](https://www.youtube.com/watch?v=ORcvSkgdA58&ab_channel=Computerphile)
* [SSH Crash Course](https://www.youtube.com/watch?v=hQWRp-FdTpc&ab_channel=TraversyMedia)

**Learning objectives:**

* What is a ``server``
* Where servers usually **live**
* What is ``SSH``
* How to create an ``SSH RSA key pair``
* How to ``connect`` to a **remote host** using an SSH RSA key pair
* The advantage of using #!/usr/bin/env bash instead of /bin/bash

**Commands to search:**

* ``ssh``
* ``ssh-keygen``
* ``env``

## Environment
 
* Language: Bash
* Operating System: Ubuntu 20.04 LTS
* Style guidelines: [Shellcheck](https://github.com/koalaman/shellcheck)
 > **Note:** The file shoul have executable permissions: ``chmod u+x [filename]`` --> run with ``./filename``

## Description of each file:

| Files          |Desription
|:----------------|:-------------------------------:|
|0-use_a_private_key |Bash script that uses ssh to connect to your server using the private key ~/.ssh/school with the user ubuntu.
|1-create_ssh_key_pair |Bash script that creates an RSA key pair.
|2-ssh_config |Your machine has an SSH configuration file for the local SSH client, let’s configure it to our needs so that you can connect to a server without typing a password. Share your SSH client configuration in your answer file.
|100-puppet_ssh_config.pp |Let’s practice using Puppet to make changes to our configuration file. Just as in the previous configuration file task, we’d like you to set up your client SSH configuration file so that you can connect to a server without typing a password.

## Authors :pen:

* [Agustin Flom](https://www.linkedin.com/in/agustin-f/)
