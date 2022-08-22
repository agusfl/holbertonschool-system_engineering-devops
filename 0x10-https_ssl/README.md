# HTTPS SSL:

**Resources:**

* [DNS](https://intranet.hbtn.io/concepts/12)
* [Web stack debugging](https://intranet.hbtn.io/concepts/68)
* [What is HTTPS?](https://www.instantssl.com/http-vs-https)
* [What are the 2 main elements that SSL is providing](https://www.sslshopper.com/why-ssl-the-purpose-of-using-ssl-certificates.html)
* [HAProxy SSL termination on Ubuntu16.04](https://devops.ionos.com/tutorials/install-and-configure-haproxy-load-balancer-on-ubuntu-1604/)
* [SSL termination](https://en.wikipedia.org/wiki/TLS_termination_proxy)
* [Bash function](https://tldp.org/LDP/abs/html/complexfunct.html)


**Learning objectives:**

* What is HTTPS SSL 2 main roles
* What is the purpose encrypting traffic
* What SSL termination means

**Commands to search:**

* ```awk```
* ```dig```

## Environment
 
* Language: Bash
* Operating System: Ubuntu 20.04 LTS
* Style guidelines: [Shellcheck](https://github.com/koalaman/shellcheck)
 > **Note:** The file shoul have executable permissions: ``chmod u+x [filename]`` --> run with ``./filename``

## Description of each file:

| Files          |Desription
|:----------------|:-------------------------------:|
|0-world_wide_web |Configure your domain zone so that the subdomain www points to your load-balancer IP (lb-01). Let’s also add other subdomains to make our life easier, and write a Bash script that will display information about subdomains.
|1-haproxy_ssl_termination |“Terminating SSL on HAproxy” means that HAproxy is configured to handle encrypted traffic, unencrypt it and pass it on to its destination.
Create a certificate using certbot and configure HAproxy to accept encrypted traffic for your subdomain www..
|100-redirect_http_to_https |A good habit is to enforce HTTPS traffic so that no unencrypted traffic is possible. Configure HAproxy to automatically redirect HTTP traffic to HTTPS.

## Authors :pen:

* [Agustin Flom](https://www.linkedin.com/in/agustin-f/)
