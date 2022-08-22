# Load balancer:

**Resources:**

* [Load balancer](https://intranet.hbtn.io/concepts/46)
* [Web stack debugging](https://intranet.hbtn.io/concepts/68)
* [Introduction to load-balancing and HAproxy](https://www.digitalocean.com/community/tutorials/an-introduction-to-haproxy-and-load-balancing-concepts)
* [HTTP header](https://www.techopedia.com/definition/27178/http-header)
* [Debian/Ubuntu HAProxy packages](https://haproxy.debian.net/)

**Learning objectives:**

Let’s improve our web stack so that there is redundancy for our web servers. This will allow us to be able to accept more traffic by doubling the number of web servers, and to make our infrastructure more reliable. If one web server fails, we will still have a second one to handle requests.

For this project, you will need to write Bash scripts to automate your work. All scripts must be designed to configure a brand new Ubuntu server to match the task requirements.

## Environment
 
* Language: Bash
* Operating System: Ubuntu 20.04 LTS
* Style guidelines: [Shellcheck](https://github.com/koalaman/shellcheck)
 > **Note:** The file shoul have executable permissions: ``chmod u+x [filename]`` --> run with ``./filename``

## Description of each file:

| Files          |Desription
|:----------------|:-------------------------------:|
|0-custom_http_response_header |Configure Nginx so that its HTTP response contains a custom header (on web-01 and web-02).
|1-install_load_balancer |Install and configure HAproxy on your lb-01 server.
|2-puppet_custom_http_response_header.pp |Just as in task #0, we’d like you to automate the task of creating a custom HTTP header response, but with Puppet.

## Authors :pen:

* [Agustin Flom](https://www.linkedin.com/in/agustin-f/)
