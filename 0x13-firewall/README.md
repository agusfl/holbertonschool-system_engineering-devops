# Firewall:

**Resources:**

* [Firewall - general knowledge](https://en.wikipedia.org/wiki/Firewall_%28computing%29)
* [Web stack debugging - concept page Holberton](https://intranet.hbtn.io/concepts/68)
* [Difference between Network based firewall and host based firewall](https://www.networkstraining.com/network-based-firewall-vs-host-based-firewall-discussion-and-comparison/)

## Info:

As explained in the **web stack debugging guide** concept page, ``telnet`` is a very good tool to check if sockets are open with ``telnet IP PORT``. For example, if you want to check if port 22 is open on ``web-02`` server:

```
sylvain@ubuntu$ telnet web-02.holberton.online 22
Trying 54.89.38.100...
Connected to web-02.holberton.online.
Escape character is '^]'.
SSH-2.0-OpenSSH_6.6.1p1 Ubuntu-2ubuntu2.8

Protocol mismatch.
Connection closed by foreign host.
sylvain@ubuntu$
```
We can see for this example that the connection is successful: ``Connected to web-02.holberton.online.``

Now let’s try connecting to port 2222:

```
sylvain@ubuntu$ telnet web-02.holberton.online 2222
Trying 54.89.38.100...
^C
sylvain@ubuntu$
```
We can see that the connection never succeeds, so after some time I just use ``ctrl+c`` to kill the process.

This can be used not just for this exercise, but for any debugging situation where two pieces of software need to communicate over sockets.

Note that the school network is filtering outgoing connections (via a network-based firewall), so you might not be able to interact with certain ports on servers outside of the school network. To test your work on web-01, please perform the test from outside of the school network, like from your web-02 server. If you SSH into your web-02 server, the traffic will be originating from web-02 and not from the school’s network, bypassing the firewall.

**Warning!**
Containers on demand cannot be used for this project (Docker container limitation)

**Be very careful with firewall rules! For instance, if you ever deny port 22/TCP and log out of your server, you will not be able to reconnect to your server via SSH, and we will not be able to recover it. When you install UFW, port 22 is blocked by default, so you should unblock it immediately before logging out of your server.**

## Environment
 
* Language: Bash
* Operating System: Ubuntu 20.04 LTS
* Style guidelines: [Shellcheck](https://github.com/koalaman/shellcheck)
 > **Note:** The file shoul have executable permissions: ``chmod u+x [filename]`` --> run with ``./filename``

## Description of each file:

| Files          |Desription
|:----------------|:-------------------------------:|
|0-block_all_incoming_traffic_but |Block all incoming traffic but ports: ``22 (SSH)``, ``443 (HTTP SSL)``, ``80 (HTTP)``
|100-port_forwarding |Firewalls can not only filter requests, they can also forward them.

## Authors :pen:

* [Agustin Flom](https://www.linkedin.com/in/agustin-f/)
