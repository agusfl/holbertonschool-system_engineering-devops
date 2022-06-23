# Bash - Networking basics #1:

**Resources:**

* [What is localhost](https://en.wikipedia.org/wiki/Localhost)
* [What is 0.0.0.0](https://en.wikipedia.org/wiki/0.0.0.0)
* [What is the hosts file](https://www.makeuseof.com/tag/modify-manage-hosts-file-linux/)
* [Netcat examples](https://www.thegeekstuff.com/2012/04/nc-command-examples/)

**Commands to search:**

* ``ifconfig``
* ``telnet``
* ``nc``
* ``cut``

**Learning objectives:**

* What is localhost/127.0.0.1
* What is 0.0.0.0
* What is /etc/hosts
* How to display your machine’s active network interfaces

## Environment
 
* Language: Bash
* Operating System: Ubuntu 20.04 LTS
* Style guidelines: [Shellcheck](https://github.com/koalaman/shellcheck)
 > **Note:** The file shoul have executable permissions: ``chmod u+x [filename]`` --> run with ``./filename``

## Description of each file:

| Files          |Desription
|:----------------|:-------------------------------:|
|0-change_your_home_IP |Bash script that configures an Ubuntu server with the below requirements.
|1-show_attached_IPs |Bash script that displays all active IPv4 IPs on the machine it’s executed on.
|100-port_listening_on_localhost |Bash script that listens on port 98 on localhost.

## Authors :pen:

* [Agustin Flom](https://www.linkedin.com/in/agustin-f/)