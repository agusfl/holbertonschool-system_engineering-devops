# Bash - Application server:

**Resources:**

* [Application server vs web server](https://www.nginx.com/resources/glossary/application-server-vs-web-server/)
* [How to Serve a Flask Application with Gunicorn and Nginx on Ubuntu 16.04 (As mentioned in the video, do not install Gunicorn using virtualenv, just install everything globally)](https://www.digitalocean.com/community/tutorials/how-to-serve-flask-applications-with-gunicorn-and-nginx-on-ubuntu-16-04)
* [Running Gunicorn](https://docs.gunicorn.org/en/latest/run.html)
* [Be careful with the way Flask manages slash in route - strict_slashes](https://werkzeug.palletsprojects.com/en/0.14.x/routing/)
* [Upstart documentation](https://upstart.ubuntu.com/cookbook/)

## Environment
 
* Language: Bash
* Operating System: Ubuntu 20.04 LTS
* Style guidelines: [Shellcheck](https://github.com/koalaman/shellcheck)
 > **Note:** The file shoul have executable permissions: ``chmod u+x [filename]`` --> run with ``./filename``

## Description of each file:

| Files          |Desription
|:----------------|:-------------------------------:|
|2-app_server-nginx_config |Building on your work in the previous tasks, configure Nginx to serve your page from the route /airbnb-onepage/
|3-app_server-nginx_config |Building on what you did in the previous tasks, let’s expand our web application by adding another service for Gunicorn to handle.
|4-app_server-nginx_config |Let’s serve what you built for AirBnB clone v3 - RESTful API on web-01.
|5-app_server-nginx_config |Let’s serve what you built for AirBnB clone - Web dynamic on web-01.
|gunicorn.service |Once you’ve got your application server configured, you want to set it up to run by default when Linux is booted.
|4-reload_gunicorn_no_downtime |One of the most important metrics for any Internet-based business is its uptime. It is the percentage of the time over a given period that the service/product is accessible to customers.

## Authors :pen:

* [Agustin Flom](https://www.linkedin.com/in/agustin-f/)
