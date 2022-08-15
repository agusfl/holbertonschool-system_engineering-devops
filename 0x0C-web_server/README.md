# Web server:

**Resources:**

* [How the web works](https://developer.mozilla.org/en-US/docs/Learn/Getting_started_with_the_web/How_the_Web_works)
* [Nginx](https://en.wikipedia.org/wiki/Nginx)
* [How to Configure Nginx](https://www.digitalocean.com/community/tutorials/how-to-set-up-nginx-server-blocks-virtual-hosts-on-ubuntu-16-04)
* [Root and sub domain](https://landingi.com/help/domains-vs-subdomains/)
* [HTTP requests](https://www.tutorialspoint.com/http/http_methods.htm)
* [HTTP redirection](https://moz.com/learn/seo/redirection)
* [Not found HTTP response code](https://en.wikipedia.org/wiki/HTTP_404)
* [Logs files on Linux](https://www.cyberciti.biz/faq/ubuntu-linux-gnome-system-log-viewer/)

**Learning objectives:**

Web server:

* What is the **main role** of a ``web server``
* What is a ``child process``
* Why web servers usually have a **parent process** and **child processes**
* What are the **main** ``HTTP requests``

DNS:

* What DNS stands for
* What is DNS main role

**Commands to search:**

* ``scp``
* ``curl``

DNS commands:

* ``A``
* ``CNAME``
* ``TXT``
* ``MX``

## Environment
 
* Language: Bash
* Operating System: Ubuntu 20.04 LTS
* Style guidelines: [Shellcheck](https://github.com/koalaman/shellcheck)
 > **Note:** The file shoul have executable permissions: ``chmod u+x [filename]`` --> run with ``./filename``

## Description of each file:

| Files          |Desription
|:----------------|:-------------------------------:|
|0-transfer_file |Bash script that transfers a file from our client to a server
|1-install_nginx_web_server |Web servers are the piece of software generating and serving HTML pages, let’s install one
|2-setup_a_domain_name | Set up a domain name using ``.TECH Domains``
|3-redirection |Configure your Nginx server so that /redirect_me is redirecting to another page.
|4-not_found_page_404 |Configure your Nginx server to have a custom 404 page that contains the string Ceci n'est pas une page.
|5-design_a_beautiful_404_page |Design a beautiful 404 page
|7-puppet_install_nginx_web_server.pp |Time to practice configuring your server with Puppet! Just as you did before, we’d like you to install and configure an Nginx server using Puppet instead of Bash.

## Authors :pen:

* [Agustin Flom](https://www.linkedin.com/in/agustin-f/)
