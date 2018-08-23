.. image:: https://travis-ci.org/sarcoma/Python_Terminal_Text_Templates.svg?branch=master
    :target: https://travis-ci.org/sarcoma/Python_Terminal_Text_Templates
.. image:: https://codecov.io/gh/sarcoma/Python_Terminal_Text_Templates/branch/master/graph/badge.svg
  :target: https://codecov.io/gh/sarcoma/Python_Terminal_Text_Templates

TextTemplate
============

Very simple text templating views for Python

Uses colour variables from AnsiColours package to style text.

Installation
------------

Install by running:

.. code:: python

    pip install text_template

::

Usage
-----



.. code:: python

    from text_template import TextTemplate as view

    print(view.render( \
        template='./a_view.txt', \
        variable="two", \
        another_variable='three' \
    ))

::

The view uses `$` and `${}` to parse the variables passed to the template for example:

.. code::

    # a_view.txt \
    One, $variable and ${another_variable} \
    New line here

::

License
-------

The project is licensed under the MIT license.
