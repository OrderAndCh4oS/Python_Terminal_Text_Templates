TextTemplate
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

    print(view.render(
            template='./a_view.txt',
            variable="two",
            another_variable='three'
        ))

The view uses `$` and `${}` to parse the variables passed to the template for example:

    # a_view.txt

    One, $variable and ${another_variable}
    New line here

License
-------

The project is licensed under the MIT license.