# Bash - Processes and signals:

**Resources:**

* [Linux PID](http://www.linfo.org/pid.html)
* [Linux process](https://www.thegeekstuff.com/2012/03/linux-processes-environment/)
* [Linux signal](https://www.thegeekstuff.com/2012/03/linux-signals-fundamentals/)

**Learning objectives:**

* What is a PID
* What is a process
* How to find a process’ PID
* How to kill a process
* What is a signal
* What are the 2 signals that cannot be ignored

**Commands to search:**

* ps
* pgrep
* pkill
* kill
* exit
* trap

## Environment
 
* Language: Bash
* Operating System: Ubuntu 20.04 LTS
* Style guidelines: [Shellcheck](https://github.com/koalaman/shellcheck)
 > **Note:** The file shoul have executable permissions: ``chmod u+x [filename]`` --> run with ``./filename``

## Description of each file:

| Files          |Desription
|:----------------|:-------------------------------:|
|0-what-is-my-pid |Bash script that displays its own PID number.
|1-list_your_processes |Bash script that displays a list of currently running processes --> use of command: ``ps``.
|2-show_your_bash_pid |Similar to last task but only display lines containing the ``bash`` word --> use of command: ``grep``.
|3-show_your_bash_pid_made_easy |Same task that the last one but without using the command **ps** --> use of command ``pgrep``.
|4-to_infinity_and_beyond |Bash script that displays ``To infinity and beyond`` indefinitely.
|5-dont_stop_me_now |Bash script that stops: ``4-to_infinity_and_beyond process`` (you need to open another terminal to try this). 
|6-stop_me_if_you_can |Same task that the last one but without using the command **kill**.
|7-highlander | Bsah script that displays a test indefinitely and catches the ``SIGTERM`` signal.
|8-beheaded_process |Bash script that kills the process: ``7-highlander``.
|100-process_and_pid_file |Bash script that create a file, displays some test and delete the file, use of the following signals: ``SIGTERM, SIGINT and SIGQUIT``.
|101-manage_my_process, manage_my_process |Manage background processes.
|102-zombie.c |C program that creates 5 zombie processes.


## Authors :pen:

* [Agustin Flom](https://www.linkedin.com/in/agustin-f/)
