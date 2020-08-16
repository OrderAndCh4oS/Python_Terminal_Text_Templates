[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

# TextTemplate

Very simple text templating views for Python

Uses colour variables from AnsiColours package to style text.

## Installation

Install by running: `pip install text_template`

## Usage

```python
from text_template import TextTemplate as view

print(view.render( \
    template='./a_view.txt', \
    variable="two", \
    another_variable='three' \
))
```

The view uses `$` and `${}` to parse the variables passed to the template for example:

*a_view.txt*

```
One, $variable and ${another_variable} \
New line here 
```

The template automatically passes in `ANSI Colours <https://github.com/sarcoma/Python_ANSI_Colours>`_ as arguments, you can wrap text with `${blue}some blue text${colour_end}` for example.

*a_view_with_ansi_colours.txt*

```
${blue}I'm Blue${colour_end}
${red}I'm Red${colour_end}
```

## License

The project is licensed under the MIT license.
