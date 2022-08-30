# MySQL - Making a replica (backup of the database):

**Resources:**

* [Install MySQL 5.7 on Ubuntu 20.04](https://computingforgeeks.com/how-to-install-mysql-on-ubuntu-focal/)
* [What is a primary-replica cluster](https://www.digitalocean.com/community/tutorials/how-to-choose-a-redundancy-plan-to-ensure-high-availability#sql-replication)
* [MySQL primary replica setup](https://www.digitalocean.com/community/tutorials/how-to-set-up-replication-in-mysql)
* [Build a robust database backup strategy](https://www.databasejournal.com/ms-sql/developing-a-sql-server-backup-strategy/)

**Connect to your MySQL server:**

```
$ sudo mysql
Welcome to the MySQL monitor.  Commands end with ; or \g.
Your MySQL connection id is 11
Server version: 8.0.25-0ubuntu0.20.04.1 (Ubuntu)

Copyright (c) 2000, 2021, Oracle and/or its affiliates.

Oracle is a registered trademark of Oracle Corporation and/or its
affiliates. Other names may be trademarks of their respective
owners.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

mysql>
mysql> quit
Bye
$
```

**Learning objectives:**

* What is the main role of a ``database``
* What is a ``database replica``
* What is the **purpose** of a ``database replica``
* Why **database backups** need to be stored in different physical locations
* What **operation** should you regularly perform to make sure that your database ``backup strategy`` actually works

**Commands:**

* mysqldump

## Environment

* Language: **MySQL**, **Bash**
* Operating System: Ubuntu 20.04 LTS
* Style guidelines: [MySql](https://dev.mysql.com/doc/refman/8.0/en/sql-statements.html), [Shellcheck](https://github.com/koalaman/shellcheck)
* ```Usage: cat [filename] | mysql -hlocalhost -uroot -p [database]```
> **Note:** The file shoul have executable permissions: ``chmod u+x [filename]`` --> run with ``./filename``

## Description of each file:

| Files          |Desription
|:----------------|:-------------------------------:|
|4-mysql_configuration_primary |Making primary database
|4-mysql_configuration_replica |Making replica of primary database
|5-mysql_backup |Backup of the database in case of a problem

## Authors

* [Agustin Flom](https://github.com/agusfl)
