import unittest

from text_template import TextTemplate as view


class TestTextTemplate(unittest.TestCase):
    def test_view(self):
        self.assertEqual(view.render(
            template='./a_view.txt',
            variable="two",
            another_variable='three'
        ), "One, two and three\nNew line here")

    def test_colour(self):
        self.assertEqual(view.render(
            template='./a_view_with_ansi_colours.txt'
        ), "\033[0;36mI'm Blue\033[0m\n\033[0;31mI'm Red\033[0m")


if __name__ == '__main__':
    unittest.main()
