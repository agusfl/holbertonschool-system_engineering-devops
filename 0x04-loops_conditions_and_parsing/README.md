# Loops, conditions and parsing

Learning objectives:

* How to create SSH keys
* What is the advantage of using #!/usr/bin/env bash over #!/bin/bash
* How to use while, until and for loops
* How to use if, else, elif and case condition statements
* How to use the cut command
* What are files and other comparison operators, and how to use them

## Environment
 
* Language: Bash
* Operating System: Ubuntu 20.04 LTS
* Style guidelines: [Shellcheck](https://github.com/koalaman/shellcheck)
 > **Note:** The file shoul have executable permissions: ``chmod u+x [filename]`` --> run with ``./filename``

## Description of each file:

| Files          |Desription
|:----------------|:-------------------------------:|
|0-RSA_public_key.pub |Create a SSH RSA key pair.
|1-for_best_school |Bash script that displays **Best School** 10 times using a ``for loop``.
|2-while_best_school |Bash script that displays **Best School** 10 times using a ``while loop``.
|3-until_best_school |Bash script that displays **Best School** 10 times using ``until loop``.
|4-if_9_say_hi |Using ``if statement`` in bash, write a script that displays **Best School** 10 times, but for the 9th iteration, displays Best School and then **Hi** on a new line.
|5-4_bad_luck_8_is_your_chance |Use of ``if``, ``elif``, ``else`` statements in a bash script with a ``while loop``.
|6-superstitious_numbers |Use of ``case statement`` in a bash script with a ``while loop`` to display numbers from 1 to 20 with different conditions.
|7-clock |Use of nested ``while loops`` that displays the time for **12 hours** and **59 minutes**.
|8-for_ls |Bash script that displays the content of the **current directory** in a list format where only the part of the name after the first **dash** is displayed (see example) - you must use a ``for loop``. | Use of command: ``cut``
|9-to_file_or_not_to_file |Bash script that gives you information about the ``school`` file.
|10-fizzbuzz | Bash script for ``FizzBuzz`` excercise.
|100-read_and_cut |Bash script that displays the content of the dile ``/etc/passwd`` - script should only display: username, user ID, home directory path for the user. --> see format of the file /etc/passwd.
|101-tell_the_story_of_passwd |Bash script that displays the content of the file ``/etc/passswd`` using a ``while loop`` + ``IFS``. --> see format for printing.
|102-lets_parse_apache_logs |Apache parsing
|103-dig_the-data |Sort parsed data from last task (102).

## Authors :pen:

* [Agustin Flom](https://www.linkedin.com/in/agustin-f/)

