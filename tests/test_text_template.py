import pytest

import pkg_resources

from text_template import TextTemplate as view

a_view = pkg_resources.resource_filename('tests', 'tests/a_view.txt')
a_view_with_ansi_colours = pkg_resources.resource_filename('tests', 'tests/a_view_with_ansi_colours.txt')


def test_view():
    assert view.render(
        template=a_view,
        variable="two",
        another_variable='three'
    ) == "One, two and three\nNew line here\n"


def test_colour():
    assert view.render(
        template=a_view_with_ansi_colours
    ) == "\033[0;36mI'm Blue\033[0m\n\033[0;31mI'm Red\033[0m\n"


def test_exception():
    with pytest.raises(OSError) as excinfo:
        view.render(template='no_file.txt')

    assert 'Template was not found: no_file.txt' in excinfo.value

