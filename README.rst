Template
========

Very simple text templating views for Python

Uses colour variables from AnsiColours package to style text.

Installation
------------

Install by running:

    pip install text_template

Usage
-----

    from text_template import TextTemplate as view

    # Red text

    view.render("a_view.txt")

The view uses `$` and `${}` to parse the variables passed to the template for example:

    # a_view.txt

    This is plain text with a ${varible_here} and $another_variable_here

License
-------

The project is licensed under the MIT license.