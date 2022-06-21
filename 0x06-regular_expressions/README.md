# Bash script using Ruby - Regular Expressions:

**Resources:**

* [Regular expressions - basics](https://www.slideshare.net/neha_jain/introducing-regular-expressions)
* [Regular expressions - advanced](https://www.slideshare.net/neha_jain/advanced-regular-expressions-80296518)
* [Rubular is your best friend](https://rubular.com/)
* [Use a regular expression against a problem: now you have 2 problems](https://blog.codinghorror.com/regular-expressions-now-you-have-two-problems/)
* [Learn Regular Expressions with simple, interactive exercises](https://regexone.com/)

**Background Context:**

For this project, you have to build your regular expression using Oniguruma, a regular expression library that which is used by Ruby by default. Note that other regular expression libraries sometimes have different properties.

Because the focus of this exercise is to play with regular expressions (regex), here is the Ruby code that you should use, just replace the regexp part, meaning the code in between the //:

``#!/usr/bin/env ruby``
``puts ARGV[0].scan(/127.0.0.[0-9]/).join``

## Environment
 
* Language: Bash script using Ruby
* The first line of all your Bash scripts should be exactly ``#!/usr/bin/env ruby``
* Operating System: Ubuntu 20.04 LTS
 > **Note:** The file shoul have executable permissions: ``chmod u+x [filename]`` --> run with ``./filename``

## Description of each file:

| Files          |Desription
|:----------------|:-------------------------------:|
|0-simply_match_school.rb |Script to match ``School``.
|1-repetition_token_0.rb |Script to match ``hbttn`` that can have a letter 't' between 2 and 5 times.
|2-repetition_token_1.rb |Script to match ``htn`` or ``hbtn``.
|3-repetition_token_2.rb |Script to match ``hbtn`` and the t can be between 1 and 4.times.
|4-repetition_token_3.rb |Script to match ``hbtn`` and the t can be between 1 and 4 times without using square brackets.
|5-beginning_and_end.rb |Script to match: The regular expression must be exactly matching a string that starts with ``h`` ends with ``n`` and can have any single character in between.
|6-phone_number.rb |Script to match: The regular expression must be exactly matching a string that starts with ``h`` ends with ``n`` and **can have any single character in between**.
|7-OMG_WHY_ARE_YOU_SHOUTING.rb |Script to match: The regular expression must be only matching: ``capital letters``.
|100-textme.rb |Your script should output: ``[SENDER],[RECEIVER],[FLAGS]``.


## Authors :pen:

* [Agustin Flom](https://www.linkedin.com/in/agustin-f/)