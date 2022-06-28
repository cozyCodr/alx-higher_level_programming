

0x05. Python - Exceptions
=========================

*   By Guillaume
*   Weight: 1
*   Ongoing project - started
    
    , must end by
    
    \- you're done with 0% of tasks.
*   Checker was released at
    
*   An auto review will be launched at the deadline

Resources
---------

**Read or watch**:

*   [Errors and Exceptions](/rltoken/Yj7sDOzmKwICSHr7WEAW3A "Errors and Exceptions")
*   [Learn to Program 11 Static & Exception Handling](/rltoken/xASzXarhF1sBhzYkJ14LvQ "Learn to Program 11 Static & Exception Handling") (_starting at minute 7_)

Learning Objectives
-------------------

At the end of this project, you are expected to be able to [explain to anyone](/rltoken/ER6JIfkhcpsfFWZNN_BBvg "explain to anyone"), **without the help of Google**:

### General

*   Why Python programming is awesome
*   What’s the difference between errors and exceptions
*   What are exceptions and how to use them
*   When do we need to use exceptions
*   How to correctly handle an exception
*   What’s the purpose of catching exceptions
*   How to raise a builtin exception
*   When do we need to implement a clean-up action after an exception

### Copyright - Plagiarism

*   You are tasked to come up with solutions for the tasks below yourself to meet with the above learning objectives.
*   You will not be able to meet the objectives of this or any following project by copying and pasting someone else’s work.
*   You are not allowed to publish any content of this project.
*   Any form of plagiarism is strictly forbidden and will result in removal from the program.

Requirements
------------

### General

*   Allowed editors: `vi`, `vim`, `emacs`
*   All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
*   All your files should end with a new line
*   The first line of all your files should be exactly `#!/usr/bin/python3`
*   A `README.md` file, at the root of the folder of the project, is mandatory
*   Your code should use the pycodestyle (version `2.8.*`)
*   All your files must be executable
*   The length of your files will be tested using `wc`

Tasks
-----

### 0\. Safe list printing

mandatory

Write a function that prints `x` elements of a list.

*   Prototype: `def safe_print_list(my_list=[], x=0):`
*   `my_list` can contain any type (integer, string, etc.)
*   All elements must be printed on the same line followed by a new line.
*   `x` represents the number of elements to print
*   `x` can be bigger than the length of `my_list`
*   Returns the real number of elements printed
*   You have to use `try: / except:`
*   You are not allowed to import any module
*   You are not allowed to use `len()`

    guillaume@ubuntu:~/0x05$ cat 0-main.py
    #!/usr/bin/python3
    safe_print_list = __import__('0-safe_print_list').safe_print_list
    
    my_list = [1, 2, 3, 4, 5]
    
    nb_print = safe_print_list(my_list, 2)
    print("nb_print: {:d}".format(nb_print))
    nb_print = safe_print_list(my_list, len(my_list))
    print("nb_print: {:d}".format(nb_print))
    nb_print = safe_print_list(my_list, len(my_list) + 2)
    print("nb_print: {:d}".format(nb_print))
    
    guillaume@ubuntu:~/0x05$ ./0-main.py
    12
    nb_print: 2
    12345
    nb_print: 5
    12345
    nb_print: 5
    guillaume@ubuntu:~/0x05$ 
    

**Repo:**

*   GitHub repository: `alx-higher_level_programming`
*   Directory: `0x05-python-exceptions`
*   File: `0-safe_print_list.py`

Done?! Help

×

#### Students who are done with "0. Safe list printing"

Check your code

×

#### Correction of "0. Safe list printing"

Start a new test Close

Requirement success

Requirement fail

Code success

Code fail

Efficiency success

Efficiency fail

Text answer success

Text answer fail

Skipped - Previous check failed

Get a sandbox

### 1\. Safe printing of an integers list

mandatory

Write a function that prints an integer with `"{:d}".format()`.

*   Prototype: `def safe_print_integer(value):`
*   `value` can be any type (integer, string, etc.)
*   The integer should be printed followed by a new line
*   Returns `True` if `value` has been correctly printed (it means the `value` is an integer)
*   Otherwise, returns `False`
*   You have to use `try: / except:`
*   You have to use `"{:d}".format()` to print as integer
*   You are not allowed to import any module
*   You are not allowed to use `type()`

    guillaume@ubuntu:~/0x05$ cat 1-main.py
    #!/usr/bin/python3
    safe_print_integer = __import__('1-safe_print_integer').safe_print_integer
    
    value = 89
    has_been_print = safe_print_integer(value)
    if not has_been_print:
        print("{} is not an integer".format(value))
    
    value = -89
    has_been_print = safe_print_integer(value)
    if not has_been_print:
        print("{} is not an integer".format(value))
    
    value = "School"
    has_been_print = safe_print_integer(value)
    if not has_been_print:
        print("{} is not an integer".format(value))
    
    guillaume@ubuntu:~/0x05$ ./1-main.py
    89
    -89
    School is not an integer
    guillaume@ubuntu:~/0x05$ 
    

**Repo:**

*   GitHub repository: `alx-higher_level_programming`
*   Directory: `0x05-python-exceptions`
*   File: `1-safe_print_integer.py`

Done?! Help

×

#### Students who are done with "1. Safe printing of an integers list"

Check your code

×

#### Correction of "1. Safe printing of an integers list"

Start a new test Close

Requirement success

Requirement fail

Code success

Code fail

Efficiency success

Efficiency fail

Text answer success

Text answer fail

Skipped - Previous check failed

Get a sandbox

### 2\. Print and count integers

mandatory

Write a function that prints the first `x` elements of a list and only integers.

*   Prototype: `def safe_print_list_integers(my_list=[], x=0):`
*   `my_list` can contain any type (integer, string, etc.)
*   All integers have to be printed on the same line followed by a new line - other type of value in the list must be skipped (in silence).
*   `x` represents the number of elements to access in `my_list`
*   `x` can be bigger than the length of `my_list` - if it’s the case, an exception is expected to occur
*   Returns the real number of integers printed
*   You have to use `try: / except:`
*   You have to use `"{:d}".format()` to print an integer
*   You are not allowed to import any module
*   You are not allowed to use `len()`

    guillaume@ubuntu:~/0x05$ cat 2-main.py
    #!/usr/bin/python3
    safe_print_list_integers = \
        __import__('2-safe_print_list_integers').safe_print_list_integers
    
    my_list = [1, 2, 3, 4, 5]
    
    nb_print = safe_print_list_integers(my_list, 2)
    print("nb_print: {:d}".format(nb_print))
    
    my_list = [1, 2, 3, "School", 4, 5, [1, 2, 3]]
    nb_print = safe_print_list_integers(my_list, len(my_list))
    print("nb_print: {:d}".format(nb_print))
    
    nb_print = safe_print_list_integers(my_list, len(my_list) + 2)
    print("nb_print: {:d}".format(nb_print))
    
    guillaume@ubuntu:~/0x05$ ./2-main.py
    12
    nb_print: 2
    12345
    nb_print: 5
    12345Traceback (most recent call last):
      File "./2-main.py", line 14, in <module>
        nb_print = safe_print_list_integers(my_list, len(my_list) + 2)
      File "/0x05/2-safe_print_list_integers.py", line 7, in safe_print_list_integers
        print("{:d}".format(my_list[i]), end="")
    IndexError: list index out of range
    guillaume@ubuntu:~/0x05$ 
    

**Repo:**

*   GitHub repository: `alx-higher_level_programming`
*   Directory: `0x05-python-exceptions`
*   File: `2-safe_print_list_integers.py`

Done?! Help

×

#### Students who are done with "2. Print and count integers"

Check your code

×

#### Correction of "2. Print and count integers"

Start a new test Close

Requirement success

Requirement fail

Code success

Code fail

Efficiency success

Efficiency fail

Text answer success

Text answer fail

Skipped - Previous check failed

Get a sandbox

### 3\. Integers division with debug

mandatory

Write a function that divides 2 integers and prints the result.

*   Prototype: `def safe_print_division(a, b):`
*   You can assume that `a` and `b` are integers
*   The result of the division should print on the `finally:` section preceded by `Inside result:`
*   Returns the value of the division, otherwise: `None`
*   You have to use `try: / except: / finally:`
*   You have to use `"{}".format()` to print the result
*   You are not allowed to import any module

    guillaume@ubuntu:~/0x05$ cat 3-main.py
    #!/usr/bin/python3
    safe_print_division = __import__('3-safe_print_division').safe_print_division
    
    a = 12
    b = 2
    result = safe_print_division(a, b)
    print("{:d} / {:d} = {}".format(a, b, result))
    
    a = 12
    b = 0
    result = safe_print_division(a, b)
    print("{:d} / {:d} = {}".format(a, b, result))
    
    guillaume@ubuntu:~/0x05$ ./3-main.py
    Inside result: 6.0
    12 / 2 = 6.0
    Inside result: None
    12 / 0 = None
    guillaume@ubuntu:~/0x05$ 
    

**Repo:**

*   GitHub repository: `alx-higher_level_programming`
*   Directory: `0x05-python-exceptions`
*   File: `3-safe_print_division.py`

Done?! Help

×

#### Students who are done with "3. Integers division with debug"

Check your code

×

#### Correction of "3. Integers division with debug"

Start a new test Close

Requirement success

Requirement fail

Code success

Code fail

Efficiency success

Efficiency fail

Text answer success

Text answer fail

Skipped - Previous check failed

Get a sandbox

### 4\. Divide a list

mandatory

Write a function that divides element by element 2 lists.

*   Prototype: `def list_division(my_list_1, my_list_2, list_length):`
*   `my_list_1` and `my_list_2` can contain any type (integer, string, etc.)
*   `list_length` can be bigger than the length of both lists
*   Returns a new list (length = `list_length`) with all divisions
*   If 2 elements can’t be divided, the division result should be equal to `0`
*   If an element is not an integer or float:
    *   print: `wrong type`
*   If the division can’t be done (`/0`):
    *   print: `division by 0`
*   If `my_list_1` or `my_list_2` is too short
    *   print: `out of range`
*   You have to use `try: / except: / finally:`
*   You are not allowed to import any module

    guillaume@ubuntu:~/0x05$ cat 4-main.py
    #!/usr/bin/python3
    list_division = __import__('4-list_division').list_division
    
    my_l_1 = [10, 8, 4]
    my_l_2 = [2, 4, 4]
    result = list_division(my_l_1, my_l_2, max(len(my_l_1), len(my_l_2)))
    print(result)
    
    print("--")
    
    my_l_1 = [10, 8, 4, 4]
    my_l_2 = [2, 0, "H", 2, 7]
    result = list_division(my_l_1, my_l_2, max(len(my_l_1), len(my_l_2)))
    print(result)
    
    guillaume@ubuntu:~/0x05$ ./4-main.py
    [5.0, 2.0, 1.0]
    --
    division by 0
    wrong type
    out of range
    [5.0, 0, 0, 2.0, 0]
    guillaume@ubuntu:~/0x05$ 
    

**Repo:**

*   GitHub repository: `alx-higher_level_programming`
*   Directory: `0x05-python-exceptions`
*   File: `4-list_division.py`

Done?! Help

×

#### Students who are done with "4. Divide a list"

Check your code

×

#### Correction of "4. Divide a list"

Start a new test Close

Requirement success

Requirement fail

Code success

Code fail

Efficiency success

Efficiency fail

Text answer success

Text answer fail

Skipped - Previous check failed

Get a sandbox

### 5\. Raise exception

mandatory

Write a function that raises a type exception.

*   Prototype: `def raise_exception():`
*   You are not allowed to import any module

    guillaume@ubuntu:~/0x05$ cat 5-main.py
    #!/usr/bin/python3
    raise_exception = __import__('5-raise_exception').raise_exception
    
    try:
        raise_exception()
    except TypeError as te:
        print("Exception raised")
    
    guillaume@ubuntu:~/0x05$ ./5-main.py
    Exception raised
    guillaume@ubuntu:~/0x05$ 
    

**Repo:**

*   GitHub repository: `alx-higher_level_programming`
*   Directory: `0x05-python-exceptions`
*   File: `5-raise_exception.py`

Done?! Help

×

#### Students who are done with "5. Raise exception"

Check your code

×

#### Correction of "5. Raise exception"

Start a new test Close

Requirement success

Requirement fail

Code success

Code fail

Efficiency success

Efficiency fail

Text answer success

Text answer fail

Skipped - Previous check failed

Get a sandbox

### 6\. Raise a message

mandatory

Write a function that raises a name exception with a message.

*   Prototype: `def raise_exception_msg(message=""):`
*   You are not allowed to import any module

    guillaume@ubuntu:~/0x05$ cat 6-main.py
    #!/usr/bin/python3
    raise_exception_msg = __import__('6-raise_exception_msg').raise_exception_msg
    
    try:
        raise_exception_msg("C is fun")
    except NameError as ne:
        print(ne)
    
    guillaume@ubuntu:~/0x05$ ./6-main.py
    C is fun
    guillaume@ubuntu:~/0x05$ 
    

**Repo:**

*   GitHub repository: `alx-higher_level_programming`
*   Directory: `0x05-python-exceptions`
*   File: `6-raise_exception_msg.py`

Done?! Help

×

#### Students who are done with "6. Raise a message"

Check your code

×

#### Correction of "6. Raise a message"

Start a new test Close

Requirement success

Requirement fail

Code success

Code fail

Efficiency success

Efficiency fail

Text answer success

Text answer fail

Skipped - Previous check failed

Get a sandbox

[Done with the mandatory tasks? Unlock 4 advanced tasks now!](/projects/245/unlock_optionals)

×

#### Recommended Sandbox

Copyright © 2022 ALX, All rights reserved.

×

#### Markdown Guide

#### Emphasis

\*\***bold**\*\*
\*_italics_\*
~~strikethrough~~

#### Headers

\# Big header
## Medium header
### Small header
#### Tiny header

#### Lists

\* Generic list item
\* Generic list item
\* Generic list item

1. Numbered list item
2. Numbered list item
3. Numbered list item

#### Links

\[Text to display\](http://www.example.com)

#### Quotes

\> This is a quote.
> It can span multiple lines!

#### Images

CSS style available: `width, height, opacity`

!\[\](http://www.example.com/image.jpg)
!\[\](http://www.example.com/image.jpg | width: 200px)
!\[\](http://www.example.com/image.jpg | height: 124px | width: 80px | opacity: 0.6)

#### Tables

| Column 1 | Column 2 | Column 3 |
| -------- | -------- | -------- |
| John     | Doe      | Male     |
| Mary     | Smith    | Female   |

_Or without aligning the columns..._

| Column 1 | Column 2 | Column 3 |
| -------- | -------- | -------- |
| John | Doe | Male |
| Mary | Smith | Female |


