import unittest

import pkg_resources

from text_template import TextTemplate as view

a_view = pkg_resources.resource_filename('tests', 'tests/a_view.txt')
a_view_with_ansi_colours = pkg_resources.resource_filename('tests', 'tests/a_view_with_ansi_colours.txt')

class TestTextTemplate(unittest.TestCase):
    def test_view(self):
        self.assertEqual(view.render(
            template=a_view,
            variable="two",
            another_variable='three'
        ), "One, two and three\nNew line here")

    def test_colour(self):
        self.assertEqual(view.render(
            template=a_view_with_ansi_colours
        ), "\033[0;36mI'm Blue\033[0m\n\033[0;31mI'm Red\033[0m")


if __name__ == '__main__':
    unittest.main()
